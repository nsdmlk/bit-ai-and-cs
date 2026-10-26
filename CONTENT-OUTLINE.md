# Whole-Project Outline and Status

**Selected module:** Hardware, Networks & Behaviorist AI. **Snapshot:** revision prepared on 26 October 2026.

**Purpose:** explain how physical computation, communication and learning fit together without implying that every learning agent needs a GPU or an Internet connection.

## Outcomes

After this resource, a beginner should be able to:

1. Trace a simple instruction using PC, IR, registers and memory under an explicit teaching model.
2. Calculate a small CPU-time example and distinguish latency from throughput.
3. Explain how a configured host resolves a name and exchanges protected web data across networks.
4. Compare the roles of IP, TCP/UDP, DNS, DHCP, HTTP/TLS and SSH.
5. Identify an agent, environment, state/observation, action, reward and policy.
6. Calculate a Q-learning update, including a true terminal transition, and distinguish an RL proposal from demonstrated learning.

## Learning sequence

| Part | Topics and dependencies | Main activity | Status and open work |
|---|---|---|---|
| [Hardware](content/Hardware/OUTLINE.md) | Physical groups → CPU → fetch/decode/execute → memory → program execution → performance → ideal pipelining → AI/network hardware → review | Instruction traces; independent performance calculation; 179 explained check/reflection answers | Revised with AI assistance; final content peer review and course-scope confirmation pending |
| [Networks](content/Networks/OUTLINE.md) | Overview → layers → network scale → IP/routes → transport → DNS → DHCP → HTTP/TLS → SSH | HTTPS trace; subnet comparison; lease-expiry scenario; 30 explained answers | Revised with AI assistance; final content peer review pending |
| [Behaviorist AI](content/Behaviorist%20AI/OUTLINE.md) | RL introduction → agent loop → tabular Q-learning → policy distinction → DQN → qualified robotics account | Nonterminal/terminal updates; policy-target comparison; coordinate exercise | Revised with AI assistance; team peer review and historical robotics evidence pending |

The detailed maps list every chapter, prerequisites, boundaries and examples. Each part has a separate answer key. Attempt the questions before opening the key.

## Prerequisites and connections

Begin with ordinary computer use and school arithmetic. Hardware performance requires multiplication, division and scientific notation, introduced in its map. Networks uses the address/prefix concepts developed within that part. AI starts with finite states and actions; it explains the formula symbols before using them. DQN is conceptual and does not require training a model.

Read the Hardware part first, then Networks, then AI for the full sequence. The parts are also usable separately by following their maps. The final hardware sections connect computation and communication; the AI robotics chapter then distinguishes perception, geometric planning and proposed learning.

## Developed Stage 1 anchors

- **Hardware Sections 02–03:** defined machine assumptions; PC/IR and register explanations; worked ADD/LOAD traces; independent questions and explanations.
- **Networks Introduction and HTTP/TLS:** a fresh HTTP/1.1 connection over TCP, with route selection, DNS, TCP and TLS in sequence; an original figure, assumptions and answer key.
- **AI Q-learning:** definitions, exploration, complete procedure, numerical episode, terminal update, original figure and changed-number activity.

Substantive text exists beyond these anchors. The status labels describe the revision's checking stage, not final human approval.

## Boundaries and uncertainties

The supplied assignment requires a whole-module map but does not include the official course module syllabus or the full Shared Assignment Rules Section 6. The team must compare this scope with those documents. CUDA and assembler appear as conceptual examples, not full programming tutorials. Advanced routing protocols, production SSH administration, deep-learning derivations and reproduction of the earlier FTC robot remain out of scope.

Pending work and proposed dates are in the [task list](project-management/TASKS.md). The [resource map](docs/RESOURCE-MAP.md) explains how these chapters become the later Study Guide, slides and tutorials.
