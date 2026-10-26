#!/usr/bin/env python3
"""Check portable Markdown references/assets using only Python's standard library."""
from pathlib import Path
import re,json,argparse,urllib.parse,xml.etree.ElementTree as ET

def slug(s):
 s=re.sub(r'<[^>]*>','',s)
 s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',s)
 s=s.replace('`','').replace('*','').lower().strip()
 return re.sub(r'[^\w\- ]','',s).replace(' ','-')

def validate(root):
 errors=[]; links=0; images=0; files=list(root.rglob('*.md')); anchors={}
 for p in files:
  if '.git' in p.parts: continue
  text=p.read_text(); names=set(); seen={}
  for h in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
   a=slug(h); n=seen.get(a,0); seen[a]=n+1; names.add(a+(f'-{n}' if n else ''))
  names.update(re.findall(r'<a\s+(?:id|name)=["\x27]([^"\x27]+)',text))
  anchors[p.resolve()]=names
 for p in files:
  if '.git' in p.parts: continue
  text=p.read_text()
  if text.count('```')%2: errors.append(f'{p.relative_to(root)}: unbalanced code fence')
  refs=list(re.finditer(r'(!?)\[[^\]]*\]\((<[^>]+>|[^)]+)\)',text))
  for m in refs:
   target=m.group(2).strip().strip('<>'); links+=1
   if m.group(1):images+=1
   if target.startswith(('http:','https:','mailto:')):
    if m.group(1):errors.append(f'{p.relative_to(root)}: remote image {target}')
    continue
   target=target.split(' "')[0]
   path,_,fragment=target.partition('#')
   dest=(p.parent/urllib.parse.unquote(path)).resolve() if path else p.resolve()
   if not dest.exists():errors.append(f'{p.relative_to(root)}: missing {target}')
   elif fragment and dest.suffix=='.md' and urllib.parse.unquote(fragment) not in anchors.get(dest,set()):
    errors.append(f'{p.relative_to(root)}: missing anchor {target}')
  if 'github.com/user-attachments/assets/' in text:errors.append(f'{p.relative_to(root)}: remote attachment dependency')
  if re.search(r'\b182026\d{4}\b',text): errors.append(f'{p.relative_to(root)}: private student identifier')
 for p in root.rglob('*.svg'):
  try:ET.parse(p)
  except ET.ParseError as e:errors.append(f'{p.relative_to(root)}: invalid SVG: {e}')
 if (root/'personal_logs').exists():errors.append('Personal logs present in public snapshot')
 return dict(markdown_files=len(files),references_checked=links,image_insertions=images,svg_files=len(list(root.rglob('*.svg'))),errors=errors)

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);parser.add_argument('--json',type=Path)
 args=parser.parse_args();result=validate(args.root.resolve())
 if args.json:args.json.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2));raise SystemExit(bool(result['errors']))
