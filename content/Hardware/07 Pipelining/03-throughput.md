# Throughput: why the pipeline is faster overall

**Learning objective:** after this section, a beginner should be able to explain what throughput is, how pipelining increases it, and why latency and throughput are different.

## 1. Why this matters

Pipelining does not make one instruction faster — so why is the CPU faster overall? The answer is **throughput**: how many instructions finish per unit of time. Understanding throughput explains the real benefit of pipelining.

## 2. Explanation

Two different measures:

- **Latency** — how long one instruction takes from start to finish.
- **Throughput** — how many instructions finish per unit of time.

Pipelining **does not reduce latency**. Each instruction still goes through fetch, decode, and execute, and still takes the same number of cycles.

But pipelining **increases throughput**. Because phases overlap, the CPU can finish one instruction every cycle (in the ideal case), instead of one every three cycles.

An analogy: a highway with more lanes does not make any single car faster. Each car still drives at the same speed. But **more cars arrive per hour** — the throughput is higher.

That is why pipelining matters: most programs run millions of instructions, so finishing them more often makes the whole program much faster, even if each individual instruction takes the same time.

## 3. Diagram

<img width="1774" height="887" alt="微信图片_20261024202545_2527_8" src="https://github.com/user-attachments/assets/4395a0bf-a307-4371-a4e6-c142fb75a8d3" />


## 4. Example

A program with 1,000 instructions, 3 phases each.

- **Without pipeline:** 1,000 × 3 = 3,000 cycles.
- **With a 3-stage pipeline (ideal):** roughly 1,000 + 2 = 1,002 cycles.

Each instruction still takes 3 cycles (latency unchanged), but the total time is about **3× shorter** because the CPU finishes one instruction per cycle after the pipeline fills. That is the throughput gain.

(In practice, hazards and stalls reduce the gain — but the idea is the same.)

## 5. Check yourself

1. What is latency? What is throughput?
2. Does pipelining reduce latency? Why or why not?
3. How does pipelining increase throughput?
4. In the example, how many cycles does the pipelined version take? The non-pipelined version?
5. What is the highway analogy for throughput?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on pipelining.
