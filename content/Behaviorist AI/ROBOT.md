# Robotics Case Study: Perception, Navigation and a Possible RL Extension

Previous: [DQN](DQN.md) · [Module map](OUTLINE.md) · [Explained answers](ANSWER-KEY.md#robot-1)

**Status:** revised with AI-assisted technical checks; awaiting team peer review.

**Prerequisites:** the agent/environment loop; the distinction between fixed calculations and learning from reward.

**Evidence status:** the FTC example below is a team member's account of an earlier project. This teaching repository does not currently include the original Java implementation, model or training evidence. The account is not independently verified by this revision.

## Learning objectives

After this chapter, you should be able to:

1. Separate perception, localization, path planning and mechanism control.
2. Distinguish the reported implementation from intended behavior and a proposed RL extension.
3. Explain why target positions require compatible coordinate frames and units.
4. Identify evidence needed to check a robotics claim.

## 1. What the team account describes

A team member reports building a computer-vision system during high school for an FTC (FIRST Tech Challenge) robot. The account describes:

- A recognizer trained using approximately **10,000 photographs of game elements**.
- A **Limelight 3** camera supplying visual information.
- Java integration through a **Vision** class.
- **Pedro Pathing** for generating paths toward collection targets.
- Coordination with slides, wrist and claw mechanisms.

These are reported historical details. The current repository contains the description, not the referenced code or an independently checked dataset count. Keep the approximate image count attached to the account until its meaning is confirmed.

![Sample detection from the reported vision system](<content/Behaviorist AI/sample.gif>)

*Figure 1. Sample of the reported vision system. Supplied by the team member; not independently verified.*

## 2. How the components connect

| Component | Its job | Status in this case |
|---|---|---|
| Perception | Detect relevant game elements | Reported in the team account |
| Localization | Estimate robot position and heading | Reported integration |
| Target calculation | Convert observations into a collection target | Reported Vision-class responsibility; source not included |
| Path generation | Construct a route toward the target | Reported Pedro Pathing integration |
| Mechanism control | Extend slides, orient wrist and close claw | Described autonomous sequence; measured completion not documented here |
| Reinforcement learning | Improve a policy using reward-bearing experience | Proposed extension, not demonstrated by the description |

The intended data flow is:

**camera observations → detection filtering → calibrated target → path generation → robot movement → mechanism control**

![Robot algorithm overview](<content/Behaviorist AI/robot_algorithm.gif>)

*Figure 2. The robot algorithm as a sequence of stages. Illustrates the intended data flow, not a verified code review.*

The described Vision class receives detections, filters unwanted colors, calculates a target using the estimated pose and offsets, generates a path and caches the last suitable target. This is a description of the reported design, not a verified code review.

The official Limelight guide documents color and neural-network pipelines, Java results and result age. Those capabilities make such integration plausible; they do not prove which pipeline or model the earlier project used. Current FTC examples use the Limelight3A name, so the owner should confirm the exact historical camera and software version. [Limelight FTC programming guide](https://docs.limelightvision.io/docs/docs-limelight/apis/ftc-programming).

## 3. A detection is not yet a field position

Camera pixels, angular offsets and field distances are different quantities. You cannot add image coordinates directly to a robot's field position.

First define:

- The sensor's outputs and units.
- The camera mounting relative to the robot.
- How detection data becomes a displacement in distance units.
- The coordinate frame of that displacement.
- Any offset between camera, robot centre, claw and collection target.

Let $\mathbf p_{\mathrm{robot}}$ be a two-dimensional field position and $\Delta\mathbf p_{\mathrm{field}}$ be a calibrated displacement expressed in the **same field frame and units**:

$$
\mathbf p_{\mathrm{target}}=
\mathbf p_{\mathrm{robot}}+\Delta\mathbf p_{\mathrm{field}}.
$$

This addition assumes the sensor conversion has already happened. It does not perform that conversion. A **pose** contains position and heading; the position vector in this equation contains only two spatial coordinates.

If the displacement is instead expressed relative to the robot, rotate it into the field frame first:

$$
\mathbf p_{\mathrm{target}}=
\mathbf p_{\mathrm{robot}}+
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
\mathbf d_{\mathrm{robot}}.
$$

For this formula, the robot's positive x-axis points forward, its positive y-axis points left, and $\theta$ is its counterclockwise heading from the field's positive x-axis. The displacement already includes the necessary calibrated offsets.

![Second autonomous run](<content/Behaviorist AI/auto2.gif>)

*Figure 3. Autonomous run showing the robot moving toward a target. Supplied by the team member; the coordinate frames shown may differ from the teaching model above.*

This is a teaching model, not a claim about the missing Vision code. Actual FTC and Pedro frames may differ; use the coordinate conventions and units of the version being integrated. [Pedro coordinate reference](https://pedropathing.com/docs/pathing/reference/coordinates).

## 4. Worked geometry example

Use an illustrative field frame with centimetres. The robot position is $(20,30)$ and a calibrated target lies 10 cm forward in the robot frame.

- Heading 0°: forward points along field +x, giving target $(30,30)$.
- Heading 90°: forward points along field +y, giving target $(20,40)$.

The target changes when the robot turns even though the robot-relative displacement stays the same. These numbers are original teaching examples, not measurements from the FTC project. Convert units when integrating a library with other distance conventions.

## 5. Fresh observations and control stages

Keeping a previous target can be useful if a detection temporarily disappears. It also needs an explicit validity rule. Check its age, whether it still matches the selection criteria, and whether robot motion or object motion has invalidated it.

If the cached target is no longer valid, detect again or follow a defined fallback rather than treating old data as a new observation. The Limelight API exposes result staleness, but no threshold for the historical project is documented here. [Limelight results and freshness](https://docs.limelightvision.io/docs/docs-limelight/apis/ftc-programming#8-is-the-data-fresh).

Path generation also does not automatically extend slides or close a claw. The intended collection sequence is detect → locate → navigate → extend → orient → grab. Each stage needs its own conditions and coordination. The current account does not provide a measured success rate for this complete sequence.

![Target tracking](<content/Behaviorist AI/tracking.gif>)

*Figure 4. Target tracking during a run.*

![Autonomous collection run](<content/Behaviorist AI/auto.gif>)

*Figure 5. Autonomous run through the collection sequence. This shows one run, not a measured success rate.*

## 6. Where reinforcement learning could fit

The described approach combines computer vision with predefined geometric calculations and path generation. It does **not** demonstrate an RL agent updating a policy from rewards.

A future RL experiment could define observations from localization and detections, a small action set, a reward for successful collection and an episode termination rule. It would then need evidence of experience collection, learning updates and evaluation.

Simulation can reduce the cost of trying actions, but successful simulation behavior does not guarantee transfer to hardware. Published sim-to-real work treats that gap as an engineering problem. [Tan et al., 2018](https://arxiv.org/abs/1804.10332).

## 7. What would verify the account?

The project owner could supply:

1. An attributed original code excerpt or stable repository link for Vision and the mechanism integration.
2. The exact robot/year, camera model, software versions and pipeline type.
3. A dataset summary explaining the image count, labels, model and separate evaluation data, if a trained recognizer was used.
4. A genuine screenshot, execution trace or recording showing which steps ran, with any measured results clearly described.

Do not invent these items or infer a result from the intended sequence. A small authentic exhibit can support a beginner case study; a full reproducible robotics release is a larger deliverable.

## 8. Check yourself

1. **ROBOT-1:** Does using a camera, neural recognizer and planned path establish that a robot learns through RL? Explain.
2. **ROBOT-2:** In the geometry example, what is the target for heading 90°? Why cannot raw image pixels be substituted for the calibrated displacement?
3. **ROBOT-3:** Name one condition for reusing a cached target and one piece of evidence that would support the earlier implementation account.

[Explained answers](ANSWER-KEY.md#robot-1)

## 9. Scope boundaries

- **Detailed:** component roles, implementation/evidence boundaries, compatible frames and a worked coordinate example.
- **Brief:** result freshness, mechanism coordination and a possible RL extension.
- **Out of scope:** reproducing the historical robot, full camera calibration, a complete control implementation or claims of measured training performance.

[Return to the module map](OUTLINE.md)
