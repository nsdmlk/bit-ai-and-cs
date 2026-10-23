# Registers and the ALU: where values live and where math happens

**Learning objective:** after this section, a beginner should be able to explain what registers are, what the ALU does, and why the CPU needs both.

## 1. Why this matters

The CPU works with values: numbers, addresses, intermediate results. Those values have to live somewhere, and the math has to happen somewhere. Registers are the "somewhere" for values; the ALU is the "somewhere" for math. Together they are the working core of the CPU.

## 2. Explanation

**Registers** are small, very fast storage slots inside the CPU. A typical CPU has 16–32 general-purpose registers. They hold the values the CPU is working on right now: operands, results, addresses.

Registers are the **fastest storage in the machine**. Much faster than RAM, much much faster than disk. That is why the CPU keeps its active values there.

**ALU (Arithmetic Logic Unit)** is a circuit that performs operations on values:

- **Arithmetic**: add, subtract, multiply, divide.
- **Logic**: AND, OR, NOT, compare.

The ALU takes inputs from registers, performs the operation, and produces a result. That result is then written back to a register.

The flow is simple:

> **registers → ALU → register**

Values come from registers, the ALU computes, the result goes back to a register. This is the core of every calculation the CPU does.

## 3. Diagram

[DIAGRAM: two registers (R1, R2) feeding into the ALU, with the ALU output going to a third register (R3). Arrows labeled "operands" and "result". Caption: "Registers feed the ALU; the result goes back to a register".]

## 4. Example

`ADD R1, R2` (meaning "R1 = R1 + R2"):

- R1 = 5, R2 = 3.
- The ALU receives 5 and 3 as inputs.
- The ALU computes 5 + 3 = 8.
- The result 8 is written back to R1.

After the instruction: R1 = 8, R2 = 3. The ALU did the math; the registers held the values.

## 5. Check yourself

1. What are registers, and why are they fast?
2. What does the ALU do? Give two examples of operations.
3. In `ADD R1, R2`, what goes into the ALU, and where does the result go?
4. Why can't the CPU keep all its values in registers?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on the processor.
