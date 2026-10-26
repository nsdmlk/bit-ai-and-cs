# Behaviorist AI — Explained Answers

[Module map](OUTLINE.md)

**Status:** revised with AI-assisted technical checks; awaiting team peer review.

Try each chapter's questions before reading its answers. These are solutions to illustrative teaching tasks, not results from a trained robot.

## INTRO-1

Two ordinary moves give −2, one collision gives −5 and reaching the exit gives +10. The undiscounted return is $-2-5+10=3$. Count each event once; reaching the exit ends the episode.

## INTRO-2

No. An image classifier trained on supplied cat labels is a supervised-learning example. RL would require a task involving actions, reward-bearing consequences and a learning procedure that uses them. A neural network by itself does not identify the learning paradigm.

## INTRO-3

One possible scheme gives −1 for an ordinary move, −5 for a collision and +10 at the terminal exit. Test whether the learned behavior actually reaches the exit rather than exploiting a reward loophole. Other schemes are valid if their objective and consequences are clear; a positive reward for proximity is not a universal requirement.

## AGENT-1

One consistent choice defines the agent as the learning controller. The arm's physical body, block, table and surrounding world are its environment. Camera images and joint measurements are observations; motor commands are actions. Other boundaries can be valid if the roles stay consistent.

## AGENT-2

It is an agent because it observes and chooses an action. The described rule alone does not establish RL: it could remain unchanged rather than being learned from reward-bearing experience.

## AGENT-3

A single image may show position without showing the direction or speed of motion. Changes between frames can reveal motion, although additional assumptions or measurements may still be needed.

## QL-1

The successor is nonterminal, so include its largest estimated action value:

$$
\text{target}=4+0.8(15)=16.
$$

$$
Q_{\mathrm{new}}=5+0.5(16-5)=10.5.
$$

The learning rate moves halfway from the old estimate 5 toward target 16. The target 16 and updated estimate 10.5 are different quantities.

## QL-2

The true terminal successor contributes no later value, so the target is 4:

$$
Q_{\mathrm{new}}=5+0.5(4-5)=4.5.
$$

The discount and stated next-action estimate do not enter this terminal update.

## QL-3

The currently highest estimate may reflect little or misleading experience. Exploration supplies information about alternatives. It is a trade-off: choosing the currently preferred action can yield reward now, while trying another action can improve later decisions. In ε-greedy selection, the random-choice branch can also choose the current greedy action.

## QL-4

The worked episode updated Q(A,X), from 20 to 55, and processed Q(B,left), which remained 50 because its target already equaled 50. Q(A,Y) and Q(B,right) were untouched. One episode does not establish that all estimates or the resulting policy are optimal.

## POLICY-1

SARSA uses Q(B,left) = 2, the next action selected by its current policy. Its target is $1+0.9(2)=2.8$. Q-learning uses the largest next-action estimate, Q(B,right) = 8, giving $1+0.9(8)=8.2$. Both use the same experienced reward and transition.

## POLICY-2

Both use target −3. There is no future-value term after true task termination, regardless of the nonterminal next-action rule.

## POLICY-3

No. On-policy describes where the learning data comes from relative to the policy being learned about. It does not guarantee safe actions, an appropriate reward, accurate sensors or suitable control restrictions. The cliff example illustrates a particular task and exploration setting.

## DQN-1

The number of possible images, and therefore image–action pairs, is enormous. It is not merely one row per pixel. A network shares parameters to approximate values across inputs, though its predictions can still be wrong.

## DQN-2

Consecutive observations are often closely related. Mixed sampling reduces the correlation among training samples and allows experiences to be reused. It does not guarantee that all samples are independent or that training succeeds.

## DQN-3

The online network is adjusted directly to reduce its prediction error. The separate target network computes targets and receives copies of parameters periodically in the described version. The slower-changing target helps reduce instability.

## DQN-4

No. Small examples can run on a CPU, while GPUs can help with larger workloads. A useful comparison specifies the task, network, number of training steps, software, hardware, stopping rule and measured result. An unsupported “hours versus weeks” statement is not a benchmark.

## ROBOT-1

No. Perception can use a trained recognizer while navigation follows fixed calculations. An RL claim needs evidence that reward-bearing interaction is used to improve a policy or value estimates. The chapter explicitly labels RL as a possible extension to the reported FTC account.

## ROBOT-2

At heading 90°, forward points along field +y. Adding the rotated displacement (0,10) cm to (20,30) cm gives (20,40) cm. Raw pixels have different units and a different coordinate frame; calibration and conversion must happen before addition.

## ROBOT-3

For example, reuse a target only while it is recent and still valid for the robot's current state. An attributed source excerpt from the actual Vision class, linked to a genuine execution trace or screenshot, could help substantiate the implementation account. Manufacturer documentation confirms capabilities, not the team's historical result.

For sources and assumptions, return to the relevant chapter. Additional defensible answers are possible for the design and system-boundary questions.
