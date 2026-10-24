# Summary map: how it all fits together

**Learning objective:** after this section, a beginner should be able to describe the whole Hardware part in one page and see how the nine topics connect.

## 1. Why this matters

Nine files can feel like nine separate topics. They are not — they are one story. This file is the one-page map: if you understand this, you understand the whole Hardware part.

## 2. Explanation

Here is the story in order.

**1. What is hardware.** A computer has five parts: CPU, RAM, storage, I/O, network. Software is the recipe; hardware is the kitchen.

**2. Inside the CPU.** The CPU has PC (next instruction), IR (current instruction), registers (values), ALU (math), control unit (manager), and buses (address and data).

**3. Fetch–decode–execute.** The CPU repeats one loop: fetch the next instruction, decode what it means, execute it. The clock drives the loop.

**4. Memory hierarchy.** Registers → cache → RAM → disk. Closer to the CPU = faster and smaller. The hierarchy hides the speed gap.

**5. How programs run.** Code is compiled into instructions. The CPU does not understand variables — only registers and addresses.

**6. Performance.** Execution time = instruction count × CPI × clock period. GHz is one lever, not the whole story.

**7. Pipelining.** Overlap phases of different instructions. Latency stays the same; throughput goes up.

**8. Hardware, AI, and networks.** AI uses GPUs and accelerators for parallel math. Networks use NICs; latency and bandwidth describe their performance. Everything runs on the same hardware foundations.

**9. Practice and summary.** Mixed examples, misconceptions, and self-check questions.

The thread that ties it all together: **small parts, each with one job, working together in a loop, as fast as the hardware allows.**

## 3. Diagram

[DIAGRAM: a mind map with "Hardware" in the center and nine branches — the nine topics — with one-line descriptions. Caption: "The whole Hardware part on one page".]

## 4. Example

You are asked: "Why is my Python loop slow?"

Using the map, you can answer at several levels:
- **Instruction level:** the loop compiles into many instructions (instruction count).
- **Memory level:** the data may not fit in cache, causing misses (CPI goes up).
- **Performance level:** the clock is only one factor; instruction count and CPI matter too.
- **Parallel level:** a GPU could do the same math much faster if the work is parallel.

One question, several layers of the map. That is how the topics connect.

## 5. Check yourself

1. Name the nine topics in order.
2. Which topic explains why GHz is not the whole story?
3. Which topic explains the difference between registers and RAM?
4. Which topic connects hardware to AI and networks?
5. In your own words: what is the one thread that ties all nine topics together?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — all chapters referenced above.
