# Execute: actually do it

**Learning objective:** after this section, a beginner should be able to explain what happens during the execute phase, for both arithmetic and memory instructions.

## 1. Why this matters

Fetch gets the instruction, decode understands it — execute is where the work actually happens. This is the phase where values change and results appear.

## 2. Explanation

Execute answers one question: **do the operation.**

For an **arithmetic instruction** (like `ADD`):

1. Operands are read from registers.
2. They are fed into the **ALU**.
3. The ALU performs the operation.
4. The result is written back to a register.

For a **memory instruction** (like `LOAD` or `STORE`):

1. The address is put on the **address bus**.
2. Memory reads or writes the value on the **data bus**.
3. The value is written into a register (for `LOAD`) or taken from a register (for `STORE`).

Notice: for memory instructions, the **ALU is not involved**. That is why RISC architectures separate load/store from arithmetic — it keeps the execute phase simple.

In kitchen terms: the cook actually chops, stirs, or plates. The work happens here.

## 3. Diagram

[DIAGRAM: two paths — (a) registers → ALU → register for arithmetic; (b) register → address bus → memory → data bus → register for load. Caption: "Execute: arithmetic vs memory instructions".]

## 4. Example

**Arithmetic:** `ADD R1, R2`, R1 = 5, R2 = 3.

- ALU receives 5 and 3.
- ALU computes 8.
- Result 8 goes back to R1.

**Memory:** `LOAD R1, [0x200]`.

- Address `0x200` goes on the address bus.
- Memory returns the value on the data bus.
- The value is written into R1.
- The ALU is not used.

Same phase, different paths — depending on the instruction.

## 5. Check yourself

1. What question does execute answer?
2. What happens during execute for an `ADD` instruction?
3. What happens during execute for a `LOAD` instruction?
4. Why is the ALU not involved in `LOAD`?
5. In the kitchen analogy, what does execute match?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on the processor.
