# Common misconceptions

**Learning objective:** after this section, a beginner should be able to recognize and correct the most common beginner mistakes about hardware.

## 1. Why this matters

Most beginner errors are not calculation errors — they are wrong mental models. Fixing the model is faster than fixing every individual mistake. This file lists the misconceptions that come up again and again.

## 2. Explanation

**"The CPU understands variables."**
No. The CPU understands registers and memory addresses. The compiler links variables to them. When you write `a = b + c`, the CPU only sees loads, adds, and stores.

**"Higher GHz is always faster."**
No. Execution time = instruction count × CPI × clock period. A faster clock can be cancelled out by worse CPI. Compare benchmarks, not GHz.

**"More RAM makes the CPU faster."**
No. More RAM means more data fits in memory, so the computer can keep more programs open. It does not make individual instructions faster. If a program is CPU-bound, extra RAM will not speed it up.

**"Cache is just extra RAM."**
No. Cache is a different layer: small, very fast, and managed automatically by the hardware. It holds recently used data to avoid going to RAM.

**"Pipelining makes each instruction faster."**
No. Pipelining keeps latency the same but increases throughput — more instructions finish per unit of time.

**"A GPU is always better than a CPU."**
No. A GPU is better for parallel math (like AI). A CPU is better for complex, branchy, general-purpose work. They are built for different jobs.

**"Latency and bandwidth are the same thing."**
No. Latency is how long one message takes; bandwidth is how much data can flow per second. High bandwidth does not fix high latency.

## 3. Diagram

<img width="1774" height="887" alt="微信图片_20261024203558_2538_8" src="https://github.com/user-attachments/assets/61e4a4c1-df85-4b4c-8581-66d130cc41df" />


## 4. Example

A friend says: "I upgraded from 3 GHz to 4 GHz, so my program must be 33% faster."

What is wrong:
- The program's instruction count and CPI may be different on the new CPU.
- A 33% higher clock does not guarantee 33% less time.
- You would need to measure or calculate execution time, not compare GHz.

Correct answer: "Maybe faster, but not necessarily by 33%. Check instruction count, CPI, and benchmark results."

## 5. Check yourself

1. Why does the CPU not understand variables?
2. Why is higher GHz not always faster?
3. Does more RAM make the CPU faster? Why or why not?
4. Does pipelining reduce latency? What does it increase?
5. What is the difference between latency and bandwidth?
6. Which misconception have you held yourself? How would you correct it now?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapters on the processor and performance.
