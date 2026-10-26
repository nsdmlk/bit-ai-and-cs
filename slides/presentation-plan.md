# Presentation Plan — Hardware, Networks & Behaviourist AI

## Purpose

Present the module as one coherent learning system rather than three unrelated topic
lists. The presenter should show how an observation becomes a computation, travels as
data, and affects a learned action.

## Recommended timing

| Segment | Slides | Time | Presenter focus |
|---|---:|---:|---|
| Opening question and route | 1–2 | 1:30 | What happens between a sensor reading and an action? |
| Hardware foundation | 3–5 | 3:30 | Trace one instruction and explain performance assumptions |
| Network path | 6–8 | 3:30 | Follow one HTTPS request through responsibilities |
| Behaviourist AI | 9–10 | 3:00 | Explain state, action, reward, and one Q-learning update |
| Integration and check | 11–13 | 2:30 | Connect all parts and test understanding |

Total: approximately 14 minutes. Adjust to the teacher's actual presentation limit if
one is supplied separately.

## Presenter roles

| Role | Responsibility | Suggested owner |
|---|---|---|
| Opening and coordination | Introduce the question, audience, and route; manage transitions | Emir / team coordinator |
| Hardware | Explain slides 3–5 and answer CPU questions | Emir, Hardware lead |
| Networks | Explain slides 6–8 and trace the request | Networks/content owner |
| Behaviourist AI | Explain slides 9–10 and the numerical update | AI/content owner |
| Integration | Run the robot activity and close | Team coordinator with Quality lead |
| Quality check | Watch timing, check terminology, collect questions | Alimzhan, Quality lead |

## Delivery script

### Opening

“Our module follows one question: how can a system receive information, compute a
response, communicate it, and improve its future actions? We begin inside the machine,
then follow data across a network, and finish with an agent learning from reward.”

### Hardware transition

“Before an agent can learn, some physical system must execute instructions. We will
trace one instruction instead of treating the CPU as a black box.”

### Network transition

“The result or observation may need to move between computers. The next question is not
‘what is the Internet?’ but ‘which responsibility belongs to which layer?’”

### AI transition

“Once the agent receives an observation, it must choose an action. Reinforcement
learning evaluates consequences over time rather than receiving a correct label for
every action.”

### Closing

“The key skill is tracing: identify the current state, the responsible component, and
the assumption that makes the example simple.”

## Rehearsal checklist

- Each presenter can explain their slide without reading the body text.
- The ADD trace uses the same PC and register assumptions as the Markdown.
- The HTTPS trace includes DNS, TCP, TLS, and HTTP in the correct order.
- The Q-learning example states whether the transition is terminal or nonterminal.
- All audience questions have answers in the corresponding Markdown answer key.
- The presentation fits the teacher's time limit with a 10% margin.
- The exported `.pptx` opens on a second computer and local assets remain available.
