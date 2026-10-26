# Review Record

## AI-assisted revision — 26 October 2026

**Scope:** source text, exercises, references, diagrams, navigation and packaging structure across the three parts. **Reviewer type:** AI assistance, not another team member.

| What was checked | Concrete finding | Correction |
|---|---|---|
| Hardware model and memory | LOAD was described as never using an ALU; registers appeared as an address-based cache lookup level | Explicit toy absolute-address model plus real address-generation caveat; separate register operands from cache/memory accesses |
| Hardware timing | CPI was confused with one instruction's latency and pipeline timing was universalized | Average CPI defined over completed instructions; ideal timing assumptions and fill/drain stated |
| Networks worked request | HTTPS trace omitted TLS; UDP described with no header | Add TCP then TLS/server validation before HTTP exchange; specify UDP's 8-byte header |
| AI learning procedure | Q-learning lacked a complete episode and terminal distinction; policy labels implied safety | Add ε-greedy procedure, nonterminal and terminal numerical updates; distinguish target/behavior policies from safety |
| Checklist and evidence | Checklist asserted unrelated AI topics and completed reviews without supporting records | Replace with evidence-based statuses; leave human reviews and historical gaps pending |
| Supporting assets | Hardware images referenced remote attachment URLs rather than packaged files | Replace with original local teaching SVGs; record provenance and explicit assumptions |

The private report records automated checks and rendered-output inspection separately. Source corrections above are review outcomes from AI assistance. They do not satisfy the assignment's requirement for another team member to review the developed material.

## Historical team review — 25 October 2026

**When and where:** evening, B1.  
**Participants:** the full team.  
**Review leads:** Emir Babayev and Alimzhan Nurpeissov.

**What was checked:** the first submission's project architecture, content organisation,
and continuation structure against the teacher's Stage 1 requirements.

**Concrete finding:** the team had concentrated heavily on writing the topic content but
had not built and presented the required project framework and continuation structure.

**Correction:** the team redesigned the repository architecture, whole-project outline,
module maps, answer keys, QA records, asset provenance, resource map, and current project
plan. Other members revised the structures for their own modules in parallel.

**Status:** this is a genuine historical architecture review. It is not a substitute
for checking the revised Hardware, Networks, and Behaviourist AI learning anchors. A
separate final content review remains pending below.

## Current content review status

The completed historical review is recorded in [team review record](peer-review-record.md).
It covers the project architecture and presentation of the work. It does not claim that
every current chapter, calculation, citation, or exported page has received a separate
independent content check. The three anchor checks remain explicit tasks in `TASKS.md`;
their result must be recorded only after the reviewer actually completes them.
