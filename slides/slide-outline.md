# Stage 1 Slide Deck Outline

## Deck purpose

The deck is a visual companion to the Markdown learning content. It does not replace
the explanations, answer keys, or references. It gives beginners a short route through
the three parts of the module and prepares them for the activities in the Study Guide.

## Audience and delivery

- **Audience:** first-year students with basic computer familiarity and school-level
  arithmetic.
- **Recommended length:** 12–15 minutes for the first presentation.
- **Format:** 16:9 editable PowerPoint with presenter notes.
- **Teaching rule:** one main claim per slide; explain the example before revealing the
  answer.
- **Shared example:** a robot receives an observation, computes an action, and receives
  a reward. The Hardware and Networks slides provide the system context; the AI slides
  explain the learning loop.

## Slide-by-slide plan

| # | Title | Main message | Visual and interaction | Source |
|---:|---|---|---|---|
| 1 | From bits to behaviour | Hardware, networks, and learning are connected parts of one system | Three-part route; ask what happens between a sensor reading and an action | `CONTENT-OUTLINE.md` |
| 2 | Start with the machine, then follow the data | The learning sequence moves from computation to communication to behaviour | Three cards: Hardware, Networks, Behaviourist AI; explain prerequisites | `CONTENT-OUTLINE.md` |
| 3 | Every instruction follows a repeatable cycle | The CPU fetches, decodes, and executes instructions | Three-stage flow; ask where the PC changes | `content/Hardware/03 Fetch Decode Execute/` |
| 4 | A trace makes the state visible | `ADD R1, R2` changes register values in a predictable sequence | Step-by-step trace with PC, IR, registers; pause before answer | `content/Hardware/03 Fetch Decode Execute/05-worked-examples.md` |
| 5 | Performance is total work, not just GHz | CPU time depends on cycles, CPI, and clock period | Formula cards and a 4 ms worked example; ask which processor wins | `content/Hardware/06 Performance/` |
| 6 | Layers keep network responsibilities separate | Encapsulation separates application, transport, network, link, and physical work | Layer stack; learners label data, segment, packet, frame, and bits | `content/Networks/OSI-MODEL.md` |
| 7 | IP and TCP answer different questions | IP routes; TCP provides a delivery contract; UDP trades guarantees for overhead | Three comparison cards; ask which layer owns ports | `content/Networks/TCP-AND-UDP.md` |
| 8 | A web request is a stack of decisions | DNS, TCP, TLS, and HTTP have different jobs in one request | Request-flow diagram; trace a fresh HTTPS connection | `content/Networks/INTRODUCTION.md` |
| 9 | Learning begins with an agent–environment loop | An agent observes a state, acts, and receives feedback | Loop diagram; ask what counts as a state and a reward | `content/Behaviorist AI/INTRODUCTION.md` |
| 10 | Q-learning stores value for state–action pairs | The update combines immediate reward and future value | Q-value equation revealed term by term; calculate a changed number | `content/Behaviorist AI/Q-LEARNING.md` |
| 11 | One robot crosses all three modules | Sensor, hardware, network, agent, action, and reward form one chain | End-to-end annotated robot path; group labeling activity | `CONTENT-OUTLINE.md` |
| 12 | Can you explain the chain? | Understanding means naming responsibilities and assumptions | Three retrieval questions; learners answer before reveal | Module answer keys |
| 13 | The module turns a black box into a trace | Follow data and name the responsibility at each step | Final map and next reading paths | All three module outlines |

## Speaker-note requirements

Every slide must include:

1. the one-sentence teaching objective;
2. one clarification of a common misconception;
3. the question to ask the audience;
4. the expected answer or transition;
5. the Markdown source used for the slide.

## Visual requirements

- Use local SVG diagrams from the relevant module where they clarify a process.
- Keep labels and formulas as editable slide text, not text inside a screenshot.
- Use consistent colours: Hardware green, Networks gold, Behaviourist AI coral.
- Keep diagrams readable from the back of a classroom; do not compress a complete
  chapter onto one slide.
