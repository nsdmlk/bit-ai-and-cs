# Why "more GHz" is not the same as "faster"

**Learning objective:** after this section, a beginner should be able to explain why a higher clock speed does not automatically mean a faster CPU.

## 1. Why this matters

"4 GHz is faster than 3 GHz" sounds obvious. It is also wrong. This is one of the most common beginner misconceptions, and it leads to bad decisions — both when buying a computer and when optimizing a program.

## 2. Explanation

The **clock speed** (in GHz) tells you how many cycles the CPU completes per second. A 3 GHz CPU completes about 3 billion cycles per second.

But a cycle is not a fixed amount of work. Different CPUs do different amounts of work per cycle, and different programs need different numbers of cycles per instruction.

The real quantity is **execution time** — how long the program actually takes. It depends on three things:

- **Instruction count** — how many instructions the program needs.
- **CPI** — average cycles per instruction.
- **Clock period** — how long one cycle lasts (1 / clock frequency).

Clock speed is only one of the three. A faster clock can be cancelled out by worse CPI or a larger instruction count.

This is why two CPUs with the same GHz can perform very differently, and why a 3 GHz CPU can sometimes beat a 4 GHz one.

## 3. Diagram

[DIAGRAM: three levers — instruction count, CPI, clock period — all feeding into a single box labeled "execution time". Caption: "Speed depends on three things, not one".]

## 4. Example

Program A: 2,000,000 instructions.

- CPU 1: 2 GHz, CPI = 2.0 → time ≈ 2 ms.
- CPU 2: 3 GHz, CPI = 3.0 → time ≈ 2 ms.

CPU 2 has the higher clock, but the same execution time. The faster clock was cancelled out by worse CPI. That is the whole point of this file.

## 5. Check yourself

1. What does GHz actually measure?
2. Why is a cycle not a fixed amount of work?
3. Name the three factors that decide execution time.
4. Can a 3 GHz CPU be faster than a 4 GHz CPU? Why?
5. What would you look at instead of GHz to compare two CPUs?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on performance.
