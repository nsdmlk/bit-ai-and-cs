
# What is an Agent?

Before we dive into Q-Learning and DQN, we need to understand the main character of Behaviorist AI: **The Agent**.

## 1. Definition

An **agent** is an autonomous entity that observes its environment, makes decisions, and takes actions to achieve a goal.

In Computer Science, an agent is just a piece of software (or a physical robot) that runs a loop:

1. **Perceive:** Gather information from the environment.
2. **Think:** Process the information and decide what to do.
3. **Act:** Execute an action that changes the environment.

## 2. Examples of Agents

Agents are everywhere, and they don't have to look like humans:

- **A chess program:** The environment is the chessboard. The actions are the legal moves.
- **A self-driving car:** The environment is the road and traffic. The actions are steering, braking, and accelerating.
- **A trading bot:** The environment is the stock market. The actions are buying or selling.
- **A robot vacuum cleaner:** The environment is your living room. The actions are moving forward, turning, and vacuuming.

## 3. The Agent-Environment Loop

The relationship between the agent and the environment is a continuous feedback loop.

*(Visual Idea for Slides: Draw a box labeled "Agent" on the left, and a box labeled "Environment" on the right. Draw an arrow from Environment to Agent labeled "State / Observation". Draw an arrow from Agent to Environment labeled "Action". Finally, an arrow from Environment back to Agent labeled "Reward".)*

1. The Environment sends a **State** (e.g., "You are at the edge of the maze").
2. The Agent receives this state and chooses an **Action** (e.g., "Move North").
3. The Environment transitions to a new state and calculates a **Reward** (e.g., "-1 point for hitting a wall").
4. The Agent receives the new state and reward, and the loop repeats.

## 4. Why "Behaviorist"?

The term comes from psychology. Behaviorism is the theory that all behaviors are learned through interaction with the environment, usually through a system of rewards and punishments.

We don't try to program the exact rules of the maze into the agent's code. Instead, we let the agent *behave* (take actions), see what happens, and learn from the result.

## 5. Check Your Understanding

**Question:** In the context of a robotic arm learning to pick up a block, what is the "Agent" and what is the "Environment"?

*(Answer: The Agent is the control software or AI that calculates the motor movements of the robotic arm. The Environment is the physical table, the block, and the camera observing the scene.)*
