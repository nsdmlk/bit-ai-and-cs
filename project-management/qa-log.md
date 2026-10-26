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

## Team peer review — pending

No reviewer name, date, approval or outcome has been entered because no completed review of this revision has been supplied. Use the [peer-review form](peer-review-template.md) and append the real outcome below after review. A review may confirm correctness; it need not invent a defect.
