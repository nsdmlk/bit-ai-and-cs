# Worked example: `a = b + c`

**Learning objective:** after this section, a beginner should be able to translate a simple line of code into instructions and trace how the values change.

## 1. Why this matters

This is the smallest complete example of "how a program runs": one line of code, four instructions, concrete values. If you can follow this, you can follow any larger program.

## 2. Explanation

We will trace `a = b + c` with `b = 4`, `c = 6`, and `a` initially 0. Suppose:

- `b` is at memory address `0x300`
- `c` is at memory address `0x304`
- `a` is at memory address `0x308`

The compiler produces:
ad R1, [0x300] # R1 = b
load R2, [0x304] # R2 = c
add R3, R1, R2 # R3 = R1 + R2
store [0x308], R3 # a = R3

We will walk through what happens at each instruction.

## 3. Diagram

<img width="1774" height="887" alt="微信图片_20261024195641_2493_8" src="https://github.com/user-attachments/assets/b3012ada-c58f-4990-b0bc-979faff360bb" />

## 4. Example

**Step 1:** `load R1, [0x300]`
- Address `0x300` goes on the address bus.
- Memory returns 4.
- R1 = 4.

**Step 2:** `load R2, [0x304]`
- Address `0x304` goes on the address bus.
- Memory returns 6.
- R2 = 6.

**Step 3:** `add R3, R1, R2`
- ALU receives R1 = 4 and R2 = 6.
- ALU computes 10.
- R3 = 10.

**Step 4:** `store [0x308], R3`
- Address `0x308` goes on the address bus.
- Value 10 (from R3) goes on the data bus.
- Memory at `0x308` now holds 10.

**Final state:**
- `a` = 10 (at address `0x308`)
- R1 = 4, R2 = 6, R3 = 10

One line of code → four instructions → one result. That is how every program works, just repeated millions of times.

## 5. Check yourself

1. Why are there two `load` instructions before the `add`?
2. What are the values of R1, R2, R3 after step 3?
3. What does the `store` instruction do?
4. If `b` and `c` were already in registers, how many instructions would be needed?
5. What is the final value of `a`?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on instructions.
