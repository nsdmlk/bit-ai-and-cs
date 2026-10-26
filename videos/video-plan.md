# Video Tutorial Plan — Stage 1 / First Production Set

## Purpose

The videos convert the same reviewed Markdown examples into short demonstrations. They
must teach, not merely read the repository aloud. Each episode introduces terms,
demonstrates one process, pauses for a learner task, and reveals an explained answer.

## Planned first set

| Episode | Working title | Length | Anchor | Deliverable for the first version |
|---:|---|---:|---|---|
| 1 | How a CPU Runs One Instruction | 4–5 min | `ADD R1, R2` and `LOAD` trace | Script, storyboard, screen/slide plan, first recording when available |
| 2 | How an HTTPS Request Travels | 4–5 min | DNS → TCP → TLS → HTTP | Script, storyboard, local request-flow visual, first recording when available |
| 3 | How an Agent Learns from Reward | 5–6 min | Q-learning update and terminal transition | Script, storyboard, equation reveal, first recording when available |
| 4 | One Robot, Three Modules | 3–4 min | Sensor → hardware → network → state → action → reward | Script, storyboard, integration activity, first recording when available |

The Markdown scripts and storyboards are ready for production. They do not claim that
MP4 files have been recorded, compressed, or independently reviewed.

## Standard episode structure

| Part | Duration | Required content |
|---|---:|---|
| Hook | 0:00–0:20 | A question or observable problem |
| Learning objective | 0:20–0:40 | Tell learners what they will be able to explain |
| Vocabulary | 0:40–1:20 | Define unfamiliar terms before using them |
| Demonstration | 1:20–3:30 | Work through one consistent example |
| Pause activity | 3:30–4:30 | Ask learners to predict, calculate, or label |
| Answer and recap | Final 30–60 sec | Explain the reasoning and point to the Markdown source |

## Production roles

| Role | Responsibility | Suggested owner |
|---|---|---|
| Video lead | Recording schedule, file naming, edit checklist | Adil Shamshiev |
| Content lead | Script accuracy and alignment with Markdown | Dmitrii / module owners |
| Hardware consultant | CPU trace and performance terminology | Emir Babayev |
| Visual design | Diagrams, slide capture, readable overlays | Ivan Maidachenko |
| Quality review | Full watch, terminology, answer, and audio check | Alimzhan Nurpeissov |
| Coordination | Versioning, source links, package inventory | Ilya / Emir |

## Technical plan

- Record at 1080p when possible; keep text readable at 720p.
- Use a clean microphone track and remove long silences, clicks, and duplicated takes.
- Keep each episode focused on one learning outcome.
- Use the same colours and labels as the PPT deck.
- Export a review copy and a final compressed MP4 only after the full video has been
  watched.
- Name files `01-cpu-instruction-trace-v1.mp4`, `02-https-request-v1.mp4`, and so on.
- Keep scripts, source diagrams, review notes, and final MP4s together in the private
  submission package.

## Video QA checklist

- [ ] Every term is defined before use.
- [ ] The demonstration matches the Markdown numbers and assumptions.
- [ ] The activity appears on screen and has enough pause time.
- [ ] The answer explains reasoning, not only the final value.
- [ ] Audio is understandable throughout the full file.
- [ ] Text and diagrams are readable on a laptop screen.
- [ ] The final file is watched from beginning to end by a reviewer.
- [ ] Duration, size, filename, reviewer, and findings are recorded in the private QA log.
