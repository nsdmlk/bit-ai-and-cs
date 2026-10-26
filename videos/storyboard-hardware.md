# Storyboard 01 — How a CPU Runs One Instruction

## Objective

Learners will trace fetch, decode, and execute and state the final values of R1, R2,
and the PC.

| Time | Screen / visual | Narration | Learner action |
|---|---|---|---|
| 0:00–0:20 | Title: “How does a CPU run one instruction?” | Introduce the black-box problem. | Predict what must change when an ADD runs. |
| 0:20–0:40 | Three-stage route | “We will fetch, decode, and execute one instruction.” | Repeat the three stages. |
| 0:40–1:20 | PC, memory, IR diagram | Define PC and IR. State the simplified four-byte assumption. | Identify where the next instruction address is stored. |
| 1:20–2:00 | Fetch animation | At `0x100`, memory returns `ADD R1, R2`; PC advances to `0x104`. | Pause: what is now in IR? |
| 2:00–2:40 | Decode card | The control unit identifies operation, operands, and destination. | Name the two ALU inputs. |
| 2:40–3:20 | Execute card | The ALU computes 5+3 and writes 8 to R1. | Track R1 and R2. |
| 3:20–4:00 | Full trace table | Show the completed state transition. | Compare before and after. |
| 4:00–4:40 | Activity card | “If R1=7 and R2=2 at `0x300`, what are the final values?” | Solve independently. |
| 4:40–5:00 | Answer and caveat | R1=9, R2=2, PC=`0x304`; real instruction sizes vary. | Explain why PC advanced during fetch. |

## Required source links

`content/Hardware/03 Fetch Decode Execute/01-fetch.md`, `02-decode.md`,
`03-execute.md`, and `05-worked-examples.md`.

## Review checks

Do not imply that all CPUs use four-byte instructions. Do not say that the PC waits
until execute to advance. Keep the register values visible while narrating.
