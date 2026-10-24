# Instruction count and CPI

**Learning objective:** after this section, a beginner should be able to explain what instruction count and CPI are, and why both matter for performance.

## 1. Why this matters

Clock speed is only one of three factors that decide execution time. The other two — instruction count and CPI — are just as important, and they are the ones beginners usually forget.

## 2. Explanation

**Instruction count** is the number of instructions a program needs to run. It depends on:

- **The algorithm** — a better algorithm needs fewer instructions.
- **The compiler** — a better compiler can produce fewer instructions.
- **The instruction set** — some architectures need more instructions to do the same thing.

**CPI (Cycles Per Instruction)** is the average number of clock cycles each instruction takes. It depends on:

- **The instruction type** — a simple add may take 1 cycle; a memory load may take many.
- **The pipeline** — a good pipeline can bring CPI close to 1.
- **Cache hits and misses** — a cache miss makes the instruction wait, raising CPI.

The key idea: **fewer instructions and fewer cycles per instruction both make a program faster**, even if the clock stays the same.

A useful way to think about it:

- Instruction count = "how many steps does the program take?"
- CPI = "how many cycles does each step cost?"

Both multiply together to give the total number of cycles.

## 3. Diagram

<img width="2172" height="724" alt="微信图片_20261024201240_2508_8" src="https://github.com/user-attachments/assets/6922df06-a4de-420f-a3ee-e56ea38cd7d0" />


## 4. Example

Two versions of the same program:

- **Version A:** 1,000,000 instructions, CPI = 2 → 2,000,000 cycles.
- **Version B:** 1,500,000 instructions, CPI = 1 → 1,500,000 cycles.

Version B has *more* instructions but *fewer* total cycles, because each instruction is cheaper. On the same clock, Version B is faster. This is why counting only instructions — or only CPI — is not enough.

## 5. Check yourself

1. What is instruction count? What three things affect it?
2. What is CPI? What three things affect it?
3. How do instruction count and CPI combine to give total cycles?
4. Can a program with more instructions be faster? Why?
5. Why does a cache miss raise CPI?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on performance.
