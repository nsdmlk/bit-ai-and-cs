# Deep Q-Networks: Replacing a Table with an Approximation

Previous: [On-policy and off-policy](POLICY-RULE.md) · [Module map](OUTLINE.md) · Next: [Robotics case study](ROBOT.md)

**Status:** revised with AI-assisted technical checks; awaiting team peer review.

**Prerequisites:** a Q-table, a Q-learning target, exploration and task termination.

## Learning objectives

After this chapter, you should be able to:

1. Explain why a separate table entry for every camera input becomes impractical.
2. Describe a DQN's input and discrete-action outputs.
3. Explain the different roles of replay memory, the online network and target network.
4. Distinguish a published DQN result from our own unperformed experiments.

## 1. From table to network

A camera can produce an enormous number of distinct images. The problem is not simply the number of pixels: it is the number of possible input configurations. Storing a separate value for every image–action pair is impractical.

A **deep Q-network (DQN)** instead approximates action values using shared neural-network parameters. For an illustrative action set {left, right, stop}, one forward calculation might output {5.2, 1.1, −3.0}. A greedy policy would choose left; an exploratory policy might choose something else.

This standard architecture assumes a finite, discrete action set. It does not directly enumerate every possible continuous motor command.

An individual screenshot may omit motion information. The Atari DQN used a representation based on recent frames. Approximation can support generalization across inputs, but does not guarantee correct values on unseen situations. [David Silver, Value Function Approximation, slides 37–38](https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-6-value-function-approximation-.pdf).

## 2. Why two networks and a memory?

Neural-network Q-learning can be unstable. The 2015 DQN system combined two mechanisms:

- **Experience replay:** store transitions, then mix past experiences by sampling minibatches. This reduces correlations between consecutive training samples and permits reuse.
- **Separate target network:** compute targets with a copy whose parameters change less often than the online network's. This reduces the movement of the targets during learning.

These mechanisms help stabilize training; they do not guarantee success in every problem. DQN was presented in 2013 and developed in the 2015 Nature paper. Replay was not invented by that paper. [Mnih et al., 2013](https://arxiv.org/abs/1312.5602); [Mnih et al., 2015, main text and Methods](https://deepmind-media.storage.googleapis.com/dqn/DQNNaturePaper.pdf).

## 3. One training cycle in plain language

1. Select an action using the behavior policy.
2. Store the observation, action, reward, next observation and whether the task truly terminated.
3. Sample a mixed batch from replay memory.
4. Compute a target for each sample using the target network; a terminal sample uses reward alone.
5. Adjust the **online network** so its action-value predictions move toward those targets.
6. Periodically copy its parameters into the **target network**.

The online network is adjusted directly by training. The target network supplies a more slowly changing reference. Some implementations use gradual copying instead; our description follows the periodic-copy idea.

For example, a nonterminal sample with reward 2, discount 0.9 and largest target-network estimate 5 has target 6.5. If it terminates the task, its target is 2. [PyTorch DQN tutorial, replay and optimization](https://docs.pytorch.org/tutorials/intermediate/reinforcement_q_learning.html).

## 4. Hardware helps, but scale matters

Training time depends on the task, simulation, network, software and hardware. GPUs can accelerate large neural-network computations. Small teaching examples can run on a CPU; the official PyTorch tutorial includes a CPU fallback.

**CUDA** is NVIDIA's platform for GPU computing, with programming tools and libraries. It is not a requirement for every neural network, and a CPU-versus-GPU time claim needs a specified experiment. [PyTorch device selection](https://docs.pytorch.org/tutorials/intermediate/reinforcement_q_learning.html); [NVIDIA CUDA](https://developer.nvidia.com/cuda).

## 5. What the research demonstrated

Atari DQN learned from visual inputs and reward signals, without a separately written playing strategy for each game. Its performance varied across games; it exceeded the human tester on some. These are published research results, not measurements produced by our team. [Mnih et al., 2015, Atari evaluation](https://deepmind-media.storage.googleapis.com/dqn/DQNNaturePaper.pdf).

Other RL methods also learn from rewards. For example, InstructGPT's feedback-training study used **PPO**, which is a different method from DQN. Mentioning RLHF does not establish that it uses DQN. [Ouyang et al., 2022, training overview](https://arxiv.org/html/2203.02155v1#S3.SS1).

## 6. Check yourself

1. **DQN-1:** Why does a high-resolution camera make a Q-table difficult to use?
2. **DQN-2:** What does mixing replay samples help with?
3. **DQN-3:** Which network is trained directly, and which computes the target?
4. **DQN-4:** Does DQN require a GPU? What information would support a meaningful runtime comparison?

[Explained answers](ANSWER-KEY.md#dqn-1)

## 7. Scope boundaries

- **Detailed:** value approximation, discrete outputs, replay and target-network roles.
- **Brief:** hardware scaling, Atari results and the distinction from PPO/RLHF.
- **Out of scope:** backpropagation derivations, loss-function details, continuous-action algorithms and implementing a production training system.

[Next: Robotics case study](ROBOT.md)
