# Storyboard 03 — How an Agent Learns from Reward

## Objective

Learners will identify state, action, reward, Q-value, and the difference between a
nonterminal and terminal Q-learning update.

| Time | Screen / visual | Narration | Learner action |
|---|---|---|---|
| 0:00–0:20 | Robot at a fork | “How can an agent improve without being told every correct action?” | Suggest what feedback could be. |
| 0:20–0:50 | Agent–environment loop | Define observation/state, action, reward, and next state. | Label the loop. |
| 0:50–1:30 | Exploration card | Explain ε-greedy choice: sometimes explore, otherwise use the best known action. | Distinguish exploration from exploitation. |
| 1:30–2:10 | Q-table | A Q-value estimates the usefulness of an action in a state. | Read high and low values. |
| 2:10–3:00 | Equation reveal | Introduce immediate reward, discount, next-state maximum, learning rate, and old value. | Translate each symbol into words. |
| 3:00–3:50 | Worked calculation | Use old Q=20, reward=10, gamma=0.9, next max=50, alpha=1; get 55. | Calculate before the reveal. |
| 3:50–4:30 | Terminal contrast | At a terminal state there is no future value term. | State which term disappears. |
| 4:30–5:20 | Q-table versus DQN | Explain why image states make a table impractical and why DQN approximates values. | Name the scaling problem. |
| 5:20–6:00 | Final activity | Change the reward and predict the direction of the update. | Explain the reasoning. |

## Required source links

`content/Behaviorist AI/INTRODUCTION.md`, `AGENT.md`, `POLICY-RULE.md`,
`Q-LEARNING.md`, and `DQN.md`.

## Review checks

Keep alpha=1 visible as a simplifying assumption. Do not describe Q-learning as a
guaranteed safe policy or claim that the robotics example demonstrates trained results.
