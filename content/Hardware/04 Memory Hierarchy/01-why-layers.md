# Why memory has layers

**Learning objective:** after this section, a beginner should be able to explain why memory is organized in layers and why the CPU cannot use just one kind of memory.

## 1. Why this matters

The CPU is extremely fast. RAM is much slower. If the CPU had to wait for RAM every time it needed a value, it would spend most of its life doing nothing. The memory hierarchy is the trick that hides this gap.

## 2. Explanation

There is a trade-off in memory:

- **Fast memory is small and expensive.**
- **Large memory is slow and cheap.**

You cannot have a huge memory that is also as fast as the CPU. So computers use **several layers** instead of one.

| Layer | Size | Speed | What it holds |
|---|---|---|---|
| Registers | Tiny (16–32 slots) | Fastest | Values the CPU is using right now |
| Cache (L1/L2/L3) | Small (KB–MB) | Very fast | Recently used data and instructions |
| RAM | Large (GB) | Fast | The program and its active data |
| SSD/disk | Very large (TB) | Slow | Everything that must be saved |

The idea is simple: **the closer to the CPU, the faster and smaller the storage.** The CPU keeps what it needs most in the fast layers, so it does not have to wait for the slow ones.

This is why a computer can feel fast even though RAM is much slower than the CPU: the fast layers (registers and cache) hide most of the waiting.

## 3. Diagram

<img width="1536" height="1024" alt="微信图片_20261024132957_2475_8" src="https://github.com/user-attachments/assets/5ec48369-8704-4e22-a80a-7213aa149420" />


## 4. Example

You run a loop that sums an array of 1,000 numbers.

- The **array** lives in RAM.
- The **current numbers** being added are copied into **cache**, then into **registers**.
- The CPU adds them in the ALU.
- The **result** stays in a register, then is written back to RAM.

Most of the work happens in registers and cache, not RAM. That is the hierarchy at work.

## 5. Check yourself

1. Why can't a computer have one memory that is both huge and fast?
2. List the four layers from fastest to slowest.
3. Which layer is closest to the CPU? Which is farthest?
4. Why does the hierarchy make a computer feel faster than RAM alone would?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on memory hierarchy.
