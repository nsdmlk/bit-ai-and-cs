# Introduction to Behaviorist AI

[Module map](OUTLINE.md) · Next: [What is an agent?](AGENT.md)

**Status:** revised with AI-assisted technical checks; awaiting team peer review.

**Prerequisites:** none beyond basic familiarity with a computer program. Hardware and Networks provide useful context, but no robotics or machine-learning background is assumed.

## Learning objectives

After this chapter, you should be able to:

1. Identify an agent, its actions and its reward signal.
2. Explain why a learner considers several steps rather than only the next reward.
3. Distinguish supervised learning from reinforcement learning.
4. Suggest and critique a simple reward scheme.

## 1. Learning through interaction

In this project, the **Behaviorist AI** module focuses on **reinforcement learning (RL)**. The name connects our topic with learning from consequences; it is a course framing, rather than a claim that RL explains all animal behavior.

An RL agent chooses actions, observes what happens, and uses experience to improve its decisions. Its objective is to maximize an accumulated reward called **return**. An action with a small immediate reward may lead to a much better outcome later.

For example, a maze agent may need to take a step away from the exit to get around a wall. Judging only the next step would miss that opportunity. RL formalizes this problem of learning from consequences over time. [Dayan and Watkins, *Reinforcement Learning*, introduction](https://www.gatsby.ucl.ac.uk/~dayan/papers/dw01.pdf).

## 2. The interaction loop

There are two main parts:

- **Agent:** the decision-maker.
- **Environment:** the system with which it interacts.

At time step $t$:

1. The agent receives an observation of the environment.
2. It selects an action $A_t$.
3. The environment responds with a new observation and reward $R_{t+1}$.
4. The learner uses that experience to update its estimates or policy.

An **episode** is one run of a task, such as an attempt to reach a maze exit. A **policy** is the rule used to select an action. Learning changes that rule or the estimates used by it.

For our small maze examples, we assume the agent can see its full **state**, such as its grid position. A camera image can instead be a partial observation: one photograph may not reveal an object's velocity. [Spinning Up, key concepts and states/observations](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html).

## 3. Different kinds of learning

| Approach | Typical feedback | Example |
|---|---|---|
| Supervised learning | Input examples with target labels | Learn from labeled animal photographs to classify a new photograph |
| Unsupervised learning | Data without target labels for that task | Group similar examples or discover structure |
| Reinforcement learning | Rewards associated with interaction | Learn a maze policy from attempted moves and their consequences |

Supervised learning aims to make useful predictions on new examples. Memorizing training examples without generalizing is a possible failure, not its definition. [Goodfellow, Bengio and Courville, *Deep Learning*, §§5.1.3 and 5.2](https://www.deeplearningbook.org/contents/ml.html).

## 4. Worked example: reward and a maze

Consider one illustrative episodic maze. Use these rules:

- Ordinary move: −1.
- Wall collision: −5; the agent stays in place.
- Reaching the exit: +10; the episode ends.

For this short example, add rewards without discounting. A route with three ordinary moves and then the exit returns $-3+10=7$. A route with six ordinary moves and then the exit returns $-6+10=4$.

The shorter collision-free route receives more reward. These values are a design choice; they are not results from a trained robot.

Positive reward merely for moving closer is not automatically sufficient. An agent might collect rewards without completing the intended task. Reward shaping can even change which policy is optimal, so the behavior must be checked against the real goal. [Ng, Harada and Russell, 1999, introduction and reward-shaping examples](https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf).

## 5. Connecting hardware, networks and AI

Sensors and processors provide observations and run control software. A GPU can accelerate a large neural network; it is not required for every RL example. A network connection can support monitoring or remote computation, while some decisions run locally.

A published quadruped study trained locomotion policies in simulation and transferred them to real robots, while addressing differences between simulation and reality. This is a specific research example, rather than evidence about our own implementation. [Tan et al., 2018](https://arxiv.org/abs/1804.10332).

## 6. Check yourself

1. **INTRO-1:** Using the maze rules above, calculate the return for two ordinary moves, one collision and then the exit.
2. **INTRO-2:** Is an image classifier trained on labeled cat photographs necessarily using RL? Explain.
3. **INTRO-3:** Propose a reward scheme for reaching an exit quickly. Explain one behavior you would check before calling it successful.

[Explained answers](ANSWER-KEY.md#intro-1)

## 7. Scope boundaries

- **Detailed:** interaction, rewards and return, learning paradigms, a worked reward example.
- **Brief:** partial observations, simulation and connections with hardware/networks.
- **Out of scope:** psychological theories of learning, optimization proofs, production robot training.

[Next: What is an agent?](AGENT.md)
