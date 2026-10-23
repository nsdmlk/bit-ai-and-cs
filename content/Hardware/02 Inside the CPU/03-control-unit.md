# The control unit: the manager of the CPU

**Learning objective:** after this section, a beginner should be able to explain what the control unit does and why the CPU needs a "manager".

## 1. Why this matters

The CPU has many parts: registers, ALU, buses, memory. Someone has to tell each part what to do and when. That someone is the control unit. Without it, the parts would not work together.

## 2. Explanation

The **control unit** is the part of the CPU that **reads the instruction and tells the other parts what to do**.

Here is what it does:

1. It reads the current instruction from IR.
2. It works out what the instruction means: what operation, which registers, where the result goes.
3. It sends **control signals** to the other parts: "read this register", "tell the ALU to add", "write the result here".

The control unit does not do math itself. It does not store values. It **directs**. It is the manager: it does not cook, but it tells the cook what to do next.

This is the "decode" part of the fetch–decode–execute cycle. The control unit is what turns an instruction into a set of actions.

## 3. Diagram

<img width="1536" height="1024" alt="diagram6" src="https://github.com/user-attachments/assets/e0d96864-e1f8-4c82-9e2f-9c265f641d8b" />


## 4. Example

Instruction in IR: `ADD R1, R2`.

- The control unit reads it and understands: "this is an add, sources are R1 and R2, destination is R1".
- It sends a signal to the registers: "put R1 and R2 on the ALU inputs".
- It sends a signal to the ALU: "add".
- It sends a signal to the register file: "write the ALU result into R1".

The control unit did no math and stored no values. It just told everyone what to do — and that is exactly its job.

## 5. Check yourself

1. What does the control unit do?
2. Does the control unit do math? Why or why not?
3. In `ADD R1, R2`, what signals does the control unit send?
4. Which phase of the cycle is the control unit most active in?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on the processor.
