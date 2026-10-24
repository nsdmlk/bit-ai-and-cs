# The compiler: from code to instructions

**Learning objective:** after this section, a beginner should be able to explain what a compiler does and why the CPU does not understand variables.

## 1. Why this matters

You write `a = b + c`. The CPU has never seen a variable in its life. Something has to translate your code into the instructions the CPU can execute. That something is the **compiler**.

## 2. Explanation

A **compiler** is a program that translates high-level code (like Python, C, or Java) into **instructions** the CPU can execute.

The key point for beginners: **the CPU does not know about variables.** It knows **registers** and **memory addresses**. The compiler's job is to connect the two:

- A variable like `b` becomes a **memory address** (or a register).
- An operation like `+` becomes an **instruction** (like `ADD`).
- An assignment like `a = …` becomes a **store** instruction.

So the compiler takes your readable code and produces a list of small, exact steps the CPU can follow. That is why the same line of code can become several instructions.

Different compilers can produce different instruction lists for the same code. One may use more instructions, another fewer. This is one reason why **instruction count** matters for performance — we will see that in the Performance file.

## 3. Diagram

<img width="2103" height="748" alt="微信图片_20261024195642_2494_8" src="https://github.com/user-attachments/assets/ef7f52aa-8185-4b38-98a2-f80e60f54577" />


## 4. Example

Your code:
a = b + c

After compiling (on a simple RISC processor), roughly:

load R1, [b] # load b into register R1
load R2, [c] # load c into register R2
add R3, R1, R2 # R3 = R1 + R2
store [a], R3 # write R3 back to memory

Four instructions for one line. The CPU only does small steps; the compiler is what turns a big step into small ones.

If `b` and `c` are already in registers, the compiler can skip the loads and emit just one `add`.

## 5. Check yourself

1. What does a compiler do?
2. Why does the CPU not understand variables?
3. What do variables become after compilation?
4. Why can the same code produce different numbers of instructions on different compilers?
5. In the example, why might the compiler skip the two `load` instructions?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on instructions.
