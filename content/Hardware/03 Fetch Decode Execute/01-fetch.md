# Fetch: get the next instruction

**Learning objective:** after this section, a beginner should be able to describe the steps of the fetch phase and explain what the PC and the two buses do during it.

## 1. Why this matters

Before the CPU can do anything with an instruction, it has to get it. Fetch is the first phase of the cycle — the step where the CPU reads the next instruction from memory. If you understand fetch, you understand how the CPU keeps moving forward.

## 2. Explanation

Fetch answers one question: **what is the next instruction, and where is it?**

The steps are always the same:

1. **PC holds the address** of the next instruction.
2. The CPU puts that address on the **address bus**.
3. **Memory returns the instruction** on the **data bus**.
4. The instruction is loaded into **IR**.
5. **PC is incremented** — it now points to the following instruction.

Notice the order: the PC moves forward *before* the instruction is executed. That is why the PC always points to the *next* instruction, not the current one.

In kitchen terms: the cook looks at the next line of the recipe and reads it. The bookmark (PC) moves to the next line, and the current line (IR) is now in hand.

## 3. Diagram

<img width="1200" height="1200" alt="image" src="https://github.com/user-attachments/assets/45fc7835-45cd-4a2f-9839-09a03d25e32f" />


## 4. Example

Suppose the PC = `0x100`, and each instruction is 4 bytes.

- Address `0x100` goes on the address bus.
- Memory returns the instruction at `0x100` on the data bus.
- The instruction lands in IR.
- PC becomes `0x104`.

Now the CPU has the instruction in IR and is ready to decode it. The PC is already pointing at the next one.

## 5. Check yourself

1. What question does fetch answer?
2. List the five steps of fetch in order.
3. Why does the PC point to the *next* instruction, not the current one?
4. Which bus carries the address, and which carries the instruction?
5. In the kitchen analogy, what does fetch match?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on the processor.
