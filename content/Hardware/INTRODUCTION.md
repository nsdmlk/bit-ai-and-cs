# Hardware — A Micro-Textbook for Beginners

This is the first draft of our Hardware content. It lives in the repo as `/content/Hardware/INTRODUCITON.md` and will become the foundation for the Study Guide, slides, videos, and test bank.

---

## Learning Objectives

After this section, a beginner should be able to:
1. Explain what the fetch–decode–execute cycle is and why it repeats.
2. Trace `ADD R1, R2` through every phase, naming the registers and buses involved.
3. Name the core CPU components (PC, IR, ALU, registers, control unit, memory) and state each one's role.
4. Calculate execution time with the formula and explain why a higher clock does not always mean "faster."
5. Describe at a high level why pipelining helps.

---

## 1. What a CPU Actually Does

A program is a sequence of **instructions** sitting in memory. The **stored-program concept** means both code and data live in the same memory, and the CPU simply reads instructions one after another and obeys them.

Key point for beginners: **the CPU does not know about variables.** It knows *registers* and *memory addresses*. When you write `a = b + c`, the compiler turns it into instructions that move values between memory and registers, add them, and store the result back.

Example: `a = b + c` on a simple RISC processor becomes roughly:

```
load  R1, [b]      # load b into register R1
load  R2, [c]      # load c into register R2
add   R3, R1, R2   # R3 = R1 + R2
store [a], R3      # write R3 back to memory
```

If `b` and `c` are already in registers, one `add` is enough.

---

## 2. What a CPU Is Made Of

| Component | What it is | Job |
|---|---|---|
| **PC** (Program Counter) | Register | Holds the address of the next instruction |
| **IR** (Instruction Register) | Register | Holds the current instruction |
| **General-purpose registers** | 16–32 of them | Hold operands and results — the fastest storage in the machine |
| **ALU** | Circuit | Performs arithmetic (add, subtract) and logic (AND, OR) |
| **Control Unit** | Logic | Decodes the instruction and tells every other part what to do |
| **Memory** (RAM) | Large array of cells | Stores both instructions and data, addressed by number |
| **Buses** | Wires | Carry addresses, data, and control signals |

Two buses matter most: the **address bus** (CPU → memory: "give me the contents at this address") and the **data bus** (memory → CPU: the actual value).

---

## 3. The Cycle: Fetch → Decode → Execute

Every instruction goes through the same loop. It is driven by the **clock** — 3 GHz means ~0.33 ns per tick.

**Fetch:**
1. PC holds the address of the next instruction.
2. The CPU puts that address on the address bus.
3. Memory returns the instruction on the data bus.
4. The instruction is loaded into IR.
5. PC is incremented — it now points to the following instruction.

**Decode:**
The control unit reads IR and works out: what operation is this, which registers are the operands, where does the result go.

**Execute:**
Operands are read from registers, fed into the ALU, the operation is performed, and the result is written back to a register. For memory instructions, this phase works with the buses instead.

Then the cycle repeats with the next PC value.

---

## 4. Worked Example: Tracing `ADD R1, R2`

Suppose `ADD R1, R2` (meaning "R1 = R1 + R2") sits at address `0x100`. PC = `0x100`. R1 = 5, R2 = 3.

**Fetch:**
- PC = `0x100` → address bus.
- Memory returns the instruction → IR.
- PC becomes `0x104` (next instruction, assuming 4-byte instructions).

**Decode:**
- Control unit reads IR: operation ADD, sources R1 and R2, destination R1.
- Prepares R1 and R2 as ALU inputs.

**Execute:**
- ALU receives 5 and 3, computes 8.
- Result 8 is written back to R1.

**Result:** R1 = 8, R2 = 3, PC = `0x104`.

**Second example — a memory load:** `LOAD R1, [0x200]` ("load into R1 the value at address 0x200"):
- Fetch — same as usual.
- Decode — control unit sees: this is a load, needs address `0x200` and destination R1.
- Execute — address `0x200` goes on the address bus, memory returns the value on the data bus, the value is written into R1. The ALU is not involved.

This is why RISC architectures isolate memory access into separate load/store instructions — it keeps the Execute phase simple.

---

## 5. Performance: Why "More GHz" ≠ "Faster"

A common beginner misconception: 4 GHz is always faster than 3 GHz. Not true. The real quantity is **execution time**:

> **Execution time = instruction count × CPI × clock period**

where **CPI** = average cycles per instruction, and clock period = 1 / clock frequency.

Three levers, and clock speed is only one of them:
- **Instruction count** — how many instructions the program needs (depends on compiler, architecture, algorithm).
- **CPI** — how many cycles each instruction takes on average (depends on pipeline, cache hits, stalls).
- **Clock period** — how long one cycle lasts (limited by manufacturing and heat).

**Worked calculation.** Program A: 2,000,000 instructions, CPI = 2.0, clock = 2 GHz.
- Clock period = 1 / (2 × 10⁹) s = 0.5 ns.
- Time = 2,000,000 × 2.0 × 0.5 ns = **2,000,000 ns = 2 ms**.

Now a 3 GHz CPU but with CPI = 3.0 for the same 2,000,000 instructions:
- Clock period ≈ 0.333 ns.
- Time = 2,000,000 × 3.0 × 0.333 ns ≈ **2 ms**.

Same result. The faster clock was cancelled out by worse CPI. **This is the main takeaway of the section.**

---

## 6. A Brief Look at Pipelining

If each instruction goes through fetch, decode, execute in sequence, the CPU sits idle during parts of each phase. **Pipelining** overlaps phases of *different* instructions: while the first executes, the second decodes, the third fetches. Like an assembly line — throughput goes up even though each individual instruction still takes the same number of cycles.

Here we only cover the idea and a simple timing diagram. Pipeline hazards are **out of scope** for this section.

---

## 7. Common Misconceptions

- **"The CPU understands variables."** No — it understands registers and addresses; the compiler links variables to them.
- **"Higher GHz is always faster."** Execution time also depends on instruction count and CPI (Section 5).
- **"More RAM = faster CPU."** More RAM means more data fits; it does not speed up individual instructions.
- **"RISC vs CISC — one is simply better."** Modern x86 chips split complex instructions into RISC-like micro-operations internally, so the line is blurred.

---

## 8. Check Yourself

1. **Trace.** Given `SUB R3, R4`, R3 = 10, R4 = 4. Walk through fetch/decode/execute, state the final register values and the new PC (4-byte instructions, instruction at `0x200`).
2. **Calculate.** A program has 5,000,000 instructions, CPI = 1.5, clock = 2.5 GHz. What is the execution time?
3. **Explain in your own words** (2–3 sentences): why does a 3 GHz CPU with CPI = 4 lose to a 2 GHz CPU with CPI = 1?
4. **Spot the error:** "I upgraded RAM from 8 GB to 32 GB, so my loop should now run 4× faster." What is wrong?

*Answers are in the test bank (separate file); the study guide(soon) will include short explanations.*

---

## 9. Scope Boundaries

- **Detailed:** CPU components, the three phases, two traces, the execution-time formula with calculations.
- **Brief:** pipelining (why it helps), RISC vs CISC, storage hierarchy (mention only).
- **Out of scope:** pipeline hazards, superscalar/out-of-order execution, cache replacement policies, instruction encoding details.

---

## 10. References (to complete and verify)

- Course materials for the Hardware module (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapters on the processor and performance (insert edition/pages).
