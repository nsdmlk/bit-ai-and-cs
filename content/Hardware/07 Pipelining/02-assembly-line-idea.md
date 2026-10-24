# The assembly-line idea

**Learning objective:** after this section, a beginner should be able to explain what pipelining is, using the assembly-line analogy, and why it makes the CPU faster.

## 1. Why this matters

Pipelining is the trick that fixes the idle-time problem from the previous file. It is one of the main reasons a modern CPU can run billions of instructions per second. The idea is simple — and the assembly-line analogy makes it easy to grasp.

## 2. Explanation

**Pipelining** means overlapping the phases of different instructions.

Instead of doing fetch → decode → execute for one instruction, then starting the next, the CPU works on several instructions at once, each in a different phase:

- While instruction 1 **executes**, instruction 2 **decodes**, and instruction 3 **fetches**.
- Next cycle: instruction 1 finishes, instruction 2 executes, instruction 3 decodes, instruction 4 fetches.
- And so on.

This is exactly how an **assembly line** works. A car factory does not build one car at a time, start to finish. Each station does one step, and many cars move through the line at once. Each car still goes through every station, but a new car rolls off the line much more often.

The key point: **each instruction still takes the same number of cycles**, but the CPU finishes one instruction per cycle (in the ideal case) instead of one every three cycles. That is the speedup.

Pipelining does not make a single instruction faster. It makes the **whole stream** of instructions faster.

## 3. Diagram

[DIAGRAM: a pipeline timing chart with rows for instructions 1–5 and columns for cycles. Each instruction shifts one phase to the right, forming a staircase pattern: I1 does F,D,E; I2 starts F one cycle later; etc. Caption: "Pipelining as an assembly line — phases overlap across instructions".]

## 4. Example

Three instructions, three phases, with a 3-stage pipeline:

- Cycle 1: I1 fetch.
- Cycle 2: I1 decode, I2 fetch.
- Cycle 3: I1 execute, I2 decode, I3 fetch.
- Cycle 4: I2 execute, I3 decode.
- Cycle 5: I3 execute.

Total: **5 cycles** for 3 instructions, instead of 9. Each instruction still took 3 cycles, but they overlapped — so the CPU finished them much sooner.

## 5. Check yourself

1. What does pipelining overlap?
2. Does pipelining make a single instruction faster? Why or why not?
3. In the example, how many cycles do 3 instructions take with a pipeline? Without?
4. What is the assembly-line analogy for pipelining?
5. Why does the CPU finish instructions more often with a pipeline?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on pipelining.
