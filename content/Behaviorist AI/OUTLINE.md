# Behaviorist AI — Module Map and Development Status

**Audience:** beginners with basic computing familiarity.

**Status:** revised with AI-assisted technical checks; awaiting team peer review.

## Purpose and reading order

Explain how reward-bearing experience can improve decisions, while distinguishing this learning process from perception, fixed calculations and path planning.

| Order | Chapter | Main outcome | Current material |
|---|---|---|---|
| 1 | [Introduction](INTRODUCTION.md) | Recognize interaction and evaluate a reward scheme | Explanation, maze arithmetic, activity and answers |
| 2 | [Agents](AGENT.md) | Identify state, observation, action, reward and policy | Glossary, original diagram and boundary exercise |
| 3 | [Q-learning](Q-LEARNING.md) | Trace and calculate a tabular learning update | Stage 1 anchor: complete procedure, worked episode, terminal update and learner activity |
| 4 | [On/off-policy](POLICY-RULE.md) | Compare behavior and target policies | SARSA/Q-learning numerical comparison and conditional cliff example |
| 5 | [DQN](DQN.md) | Explain value approximation, replay and target networks | Plain-language training cycle; qualified hardware and research examples |
| 6 | [Robotics](ROBOT.md) | Separate reported implementation, evidence and proposed RL | Team-account case study plus original coordinate example |

Chapter links specify prerequisites and scope boundaries. [Explained answers](ANSWER-KEY.md) support attempts at the chapter questions. Inline source links identify the specific definitions, algorithm claims and external examples used.

## Stage 1 developed topic

The Q-learning chapter is the main developed topic. It supplies:

- Explicit assumptions and measurable objectives.
- Definitions before the update rule.
- ε-greedy exploration and a complete learning procedure.
- A two-step illustrative episode retaining the correct result 55.
- A terminal update with no future-value term.
- Changed-number questions with explained answers.
- Specific academic/official sources and an original flow diagram.

The other chapters provide context and further learning. Their presence does not mean all final presentation or video deliverables are complete.

## Evidence and authorship boundaries

The existing personal log retained in the private submission records Ilya’s authorship of the initial reinforcement-learning introduction. It does not establish authorship of every later chapter or identify the owner of the earlier FTC code.

This revision was prepared with AI assistance and checked against the linked technical sources. It is not a completed human peer review. Chapter ownership, reviewer names and review outcomes should be recorded when the team confirms or performs them.

The robotics chapter labels the FTC implementation as a team member's account. Original Java code, training evidence, the dataset count and end-to-end performance have not been independently verified by this revision.

## Original teaching assets

- [Agent/environment loop](assets/agent-environment-loop.svg).
- [Q-learning target/update flow](assets/q-learning-update.svg).

Both diagrams and the small arithmetic/geometry exercises were created for this revision. They are illustrations rather than experimental evidence.

## Next review tasks

1. Have a team member attempt the Q-learning activity before reading the key; record actual feedback.
2. Check the rendered mathematics, diagrams and navigation in the submission format.
3. Confirm chapter ownership and attach an authentic review outcome.
4. Ask the FTC case owner to confirm historical details and provide a small attributable exhibit if available.
5. Use these sources and exercises when preparing the later slides, videos and mini-lecture.

These are pending tasks. No past approvals or experimental results are implied.

## Connection with the rest of the project

[Hardware](../Hardware/INTRODUCTION.md) explains how computations run. [Networks](../Networks/INTRODUCTION.md) explains how devices communicate. This module explains a learning objective and decision process that can run on that infrastructure; a network connection or GPU is not compulsory for every example.
