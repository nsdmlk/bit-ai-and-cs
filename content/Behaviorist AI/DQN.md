
# Deep Q-Network (DQN)

In Q-Learning, we used a **Q-table** to store the value of every state-action pair. But imagine a robot with a camera. The "state" is an image with millions of pixels. A Q-table would need billions of rows—it would not fit in any computer's memory.

How do we solve this? We replace the table with a **Neural Network**.

This is the core idea behind **Deep Q-Network (DQN)**.

## 1. From Table to Network

Instead of looking up a value in a table, we pass the state (e.g., the pixels of a game screen) into a neural network. The network outputs the Q-values for all possible actions.

- **Input:** The current state (e.g., a screenshot).
- **Output:** A vector of Q-values (e.g., [Move Left: 5.2, Move Right: 1.1, Jump: -3.0]).
- **The "Deep" part:** We use a Deep Neural Network (often a Convolutional Neural Network, CNN) to process the complex input.

## 2. Why Hardware Matters (The Link to Module 1)

Training a DQN requires millions of calculations. If we use a CPU (Central Processing Unit), it will take weeks.

This is why we need **GPUs** (Graphics Processing Units) and frameworks like **CUDA**. GPUs can perform thousands of matrix multiplications in parallel, making it possible to train DQN agents in hours instead of months. *(This is exactly why our module connects Hardware, Networks, and AI).*

## 3. Two Tricks that Make DQN Work

If you just replace the Q-table with a neural network, the training often fails. It becomes unstable. To fix this, the researchers who invented DQN (DeepMind, 2015) introduced two crucial tricks:

**Trick 1: Experience Replay**
The agent stores its experiences `(State, Action, Reward, Next State)` in a memory buffer. Instead of learning from one action immediately, it randomly samples a "batch" of past memories. This breaks the correlation between consecutive actions and stabilizes the neural network.

**Trick 2: Target Network**
We use two neural networks. The main network is learning. The "Target" network is a frozen copy that is updated only occasionally. This prevents the network from chasing a moving target while it learns.

## 4. Real-World Application

DQN was famously used to play classic Atari games (like Breakout and Pong) directly from the pixels on the screen, achieving superhuman performance without any human instructions on how to play. Today, the concepts from DQN are used in robotics, autonomous driving, and even in training Large Language Models (RLHF).

## 5. Check Your Understanding

**Question:** Why can't we use a standard Q-table for a robot that uses a high-resolution camera as its eyes?

*(Answer: The state space (all possible camera images) is too massive. A table would require an impossible amount of memory. A neural network can approximate the Q-values for unseen states.)*
