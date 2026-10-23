
# Q-Learning: How Agents Learn from Experience

In the previous section, we learned that an agent learns by taking actions, receiving rewards, and observing the environment. But how does it actually *remember* what it learned? How does it know which action is best in a specific situation?

The answer is **Q-Learning**.

## 1. The Concept of "Q"

Imagine you are playing a video game. You are at a specific point on the map (the **State**). You have a choice: jump left or jump right (the **Actions**).

How do you decide? You think about the future. "If I jump right, I usually get a coin. If I jump left, I fall into lava."

In Reinforcement Learning, we assign a number to every possible (State, Action) pair. This number is called the **Q-value** (or Quality-value).

- **High Q-value:** "This action is probably a good idea here."
- **Low Q-value:** "This action is a bad idea."

The agent keeps a giant table (a **Q-table**) that stores these numbers.

## 2. The Bellman Equation (Intuitively)

How does the agent update the Q-table when it learns something new? It uses the **Bellman Equation**.

Don't let the math scare you. Here is the core idea in plain English:

> **The value of doing an action now equals the immediate reward you get, PLUS the maximum value you can get from the next state.**

If you find a treasure chest right now, that's a great reward. But if moving one step forward leads to a room full of treasure chests, the Q-value for moving forward should be even higher.

Mathematically, it looks like this:

$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
$$

- **$s, a$**: current state and action.
- **$r$**: immediate reward.
- **$s'$**: the next state.
- **$\alpha$**: Learning rate (how much we update our old belief).
- **$\gamma$**: Discount factor (how much we care about *future* rewards vs immediate ones).

## 3. On-Policy vs. Off-Policy

When the agent updates its Q-table, does it learn by *doing* or by *watching*?

- **On-Policy:** The agent updates the Q-value using the exact action it just took. (Example: **SARSA**). It learns the value of the policy it is currently following.
- **Off-Policy:** The agent updates the Q-value using the *best possible* action for the next state, even if it didn't take that action this time. (Example: **Q-Learning**). It learns the optimal policy, even if it is currently exploring randomly.

Q-learning is off-policy, which makes it very powerful.

## 4. The Problem: Too Many States (Enter DQN)

A Q-table works great for simple games like a 4x4 grid. But what if the state is an image from a camera with millions of pixels? A table would be too massive to fit in memory.

To solve this, we replace the Q-table with a **Neural Network**. The network takes the State as input and outputs the Q-values for all possible actions.

This is called **Deep Q-Network (DQN)**.

- We use a neural network (which requires **GPUs** for fast computation, linking back to our Hardware module).
- The network learns to approximate the Q-values instead of memorizing them in a table.

## 5. Where We Stop

We have now reached the limit of what we can cover in this module.

To go further, you would need to learn about:

- **Policy Gradient methods** (like PPO) — used in modern LLMs.
- **Actor-Critic methods** (like SAC) — used in advanced robotics.

These require a deep understanding of calculus, linear algebra, and neural network architecture, and are active research areas. For now, just understand the loop: **Observe -> Act -> Reward -> Update.**

## 6. Check Your Understanding

**Question:** Imagine a robot using Q-learning. It is at State A. It takes Action X and receives a reward of +10. The next state is State B, which has a maximum Q-value of 50. The discount factor ($\gamma$) is 0.9.
If the old Q-value for (State A, Action X) was 20, what is the new Q-value? (Assume learning rate $\alpha = 1$ for simplicity).

*(Answer: New Q = Old Q + 1 * [Reward + 0.9 * max Q(next) - Old Q] = 20 + [10 + 0.9 * 50 - 20] = 20 + [10 + 45 - 20] = 20 + 35 = 55. The agent now values this action much more!)*
