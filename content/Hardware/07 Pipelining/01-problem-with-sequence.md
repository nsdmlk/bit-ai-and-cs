# The problem with doing one thing at a time

**Learning objective:** after this section, a beginner should be able to explain why a CPU that does fetch, then decode, then execute, one instruction at a time, wastes time.

## 1. Why this matters

The basic fetch–decode–execute cycle works, but it is inefficient. Understanding *why* it is inefficient is the first step to understanding pipelining — one of the main reasons modern CPUs are fast.

## 2. Explanation

In the basic cycle, each instruction goes through three phases in sequence:

1. Fetch — get the instruction.
2. Decode — figure out what it means.
3. Execute — do it.

The problem: **during each phase, most of the CPU is idle.**

- During **fetch**, the ALU is doing nothing.
- During **decode**, the ALU is still doing nothing.
- During **execute**, the memory and fetch hardware are doing nothing.

So a CPU running one instruction at a time uses only a small part of its hardware at any moment. The rest waits.

In kitchen terms: the cook reads the recipe (fetch), thinks about it (decode), then cooks (execute). While reading and thinking, the stove is idle. While cooking, the cook is not reading the next line. A lot of waiting.

If we could overlap these phases — read the next line while cooking the current dish — the kitchen would produce more meals in the same time.

## 3. Diagram

<img width="2056" height="765" alt="微信图片_20261024202547_2528_8" src="https://github.com/user-attachments/assets/d6569d30-d2e8-49ba-96da-7bd750beba51" />


## 4. Example

Three instructions, each taking 3 cycles (one per phase):

- Instruction 1: fetch (cycle 1), decode (cycle 2), execute (cycle 3).
- Instruction 2: fetch (cycle 4), decode (cycle 5), execute (cycle 6).
- Instruction 3: fetch (cycle 7), decode (cycle 8), execute (cycle 9).

Total: **9 cycles** for 3 instructions. During cycle 1, the ALU is idle. During cycle 3, the fetch hardware is idle. That is the waste.

## 5. Check yourself

1. Why is the sequential cycle inefficient?
2. Which parts of the CPU are idle during fetch? During execute?
3. In the example, how many cycles do 3 instructions take?
4. In the kitchen analogy, what is idle while the cook reads the recipe?
5. What would you want to overlap to save time?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on pipelining.
