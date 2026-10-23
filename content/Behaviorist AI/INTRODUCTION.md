# Introduction to Behaviorist AI

---

## The Big Picture: Why Hardware, Networks, and AI Matter

So far, we have looked at **Hardware** (how computers calculate) and **Networks** (how computers talk to each other). But computers are just tools. What happens when we put hardware and networks together and give them a body? We get **robots**.

But how does a robot know what to do? How does it learn to walk, drive a car, or play a game without a human explicitly programming every single movement?

Welcome to **Behaviorist AI**.

## What is Behaviorist AI?

Behaviorist AI is based on the idea of *behaviorism* in psychology: we learn by interacting with the world. We take an action, see the result, and adjust our behavior based on rewards or punishments.

In Computer Science, this is called **Reinforcement Learning (RL)**.

Think of a puppy. You don't give the puppy a textbook on how to sit. You say "Sit." If it sits, you give it a treat (reward). If it doesn't, it gets nothing. Eventually, the puppy connects the action ("sitting") with the reward ("treat").

RL works the exact same way, but with numbers.

## The Core Loop: How an Agent Learns

Every RL system has two main characters:

1. **The Agent:** The learner or decision-maker (e.g., a robot, a software program, or a video game character).
2. **The Environment:** Everything the agent interacts with (e.g., a physical room, a chess board, or a video game level).

The interaction happens in a continuous loop:

1. The agent observes the **State** of the environment (e.g., "I am at a dead end").
2. The agent takes an **Action** (e.g., "Turn left").
3. The environment gives a **Reward** (e.g., +10 points for finding an exit, or -1 point for hitting a wall).
4. The environment moves to a **New State**.

## How is this different from other AI?

* **Supervised Learning:** You give the computer a picture of a cat and say "This is a cat." It learns by memorization.
* **Unsupervised Learning:** You give the computer a lot of data and say "Find patterns."
* **Reinforcement Learning (Behaviorist AI):** You don't tell the computer the answer. You just give it a goal (maximize the score) and let it figure it out through trial and error.

## Real-World Example: Robots

Why are we talking about this in a module about hardware and networks?

- **Hardware** (GPU) is needed to process the camera feed and calculate the millions of possible actions a robot arm can take.
- **Networks** (Wi-Fi, Bluetooth) are needed so the robot can send sensor data to a server or receive commands.
- **RL (Behaviorist AI)** is the brain that uses that hardware and network to learn how to pick up an object.

Companies like Boston Dynamics and Tesla use Reinforcement Learning in simulation (like MuJoCo) to train robots millions of times a day before deploying them in the real world.

## Check Your Understanding

**Question:** Imagine you are teaching a robot to navigate a maze. You want it to find the exit as fast as possible.
If the robot takes a step, what should happen to its reward if it moves *closer* to the exit? What should happen if it hits a wall?

*(Answer: Moving closer should give a positive reward to encourage the behavior. Hitting a wall should give a negative reward or zero to discourage it.)*

## References

- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*. MIT press.
