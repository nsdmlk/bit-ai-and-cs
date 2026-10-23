# PC and IR: where the CPU keeps its place

**Learning objective:** after this section, a beginner should be able to explain what the Program Counter and the Instruction Register are, and why the CPU needs both.

## 1. Why this matters

The CPU runs instructions one after another. To do that, it needs to answer two questions at every moment: "where is the next instruction?" and "what am I doing right now?" The CPU answers these with two small registers: PC and IR. Without them, it would lose its place.

## 2. Explanation

**PC (Program Counter)** is a register that holds the **address of the next instruction**. Think of it as a bookmark: it tells the CPU where to read next. After an instruction is fetched, the PC moves forward to point at the following one.

**IR (Instruction Register)** is a register that holds the **current instruction** — the one being worked on right now. Think of it as the line of the recipe you are reading at this moment.

The difference is simple:

- **PC** = "where to go next" (an address).
- **IR** = "what I am doing now" (an instruction).

Both are needed. The PC is how the CPU keeps moving forward; the IR is how it holds on to the instruction long enough to decode and execute it.

An important detail: the PC usually moves forward **before** the instruction is fully executed. That is why the PC points to the *next* instruction, not the current one.

## 3. Diagram

<img width="1536" height="1024" alt="diagram5" src="https://github.com/user-attachments/assets/a988bf7c-a200-40e8-8e3a-955931e8319b" />


## 4. Example

Suppose the program is at address `0x100` and each instruction is 4 bytes.

- PC = `0x100` → the CPU fetches the instruction at `0x100`.
- That instruction goes into IR.
- PC becomes `0x104` → it now points to the next instruction.
- The CPU decodes and executes what is in IR.
- Then the cycle repeats with PC = `0x104`.

At every moment: PC says where to look next, IR says what is being done now.

## 5. Check yourself

1. What does the PC hold? What does the IR hold?
2. Why does the PC point to the *next* instruction, not the current one?
3. What would happen if the CPU had no PC?
4. What would happen if the CPU had no IR?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on the processor.
