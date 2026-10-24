# Worked examples: putting it all together

**Learning objective:** after this section, a beginner should be able to solve mixed problems that combine tracing, memory, performance, and pipelining.

## 1. Why this matters

Each file so far focused on one topic. Real questions mix topics. This file gives you mixed examples, so you can practise using several ideas at once — which is exactly what the test bank and the Study Guide will ask.

## 2. Explanation

When you face a mixed problem, follow this checklist:

1. **What is being asked?** Tracing? A calculation? An explanation?
2. **Which topics are involved?** The cycle, memory, performance, pipelining?
3. **What are the given values?** PC, registers, instruction count, CPI, clock.
4. **Which formula or pattern applies?** Trace pattern, execution time formula, pipeline overlap.
5. **Write each step.** Do not skip; the steps are the answer.

The examples below show this checklist in action.

## 3. Diagram

[DIAGRAM: a decision flowchart — "What is asked?" → branches "trace / calculate / explain" → each branch points to the right pattern or formula. Caption: "How to approach a mixed problem".]

## 4. Example

### Example 1 — trace + memory

`LOAD R1, [0x200]` sits at `0x100`. PC = `0x100`. Memory at `0x200` holds 42.

**Fetch:** PC `0x100` → memory → IR; PC becomes `0x104`.
**Decode:** control unit sees: load, address `0x200`, destination R1.
**Execute:** address `0x200` → address bus; memory returns 42 → data bus; R1 = 42.
**Result:** R1 = 42, PC = `0x104`. The ALU was not used.

### Example 2 — performance calculation

Program: 4,000,000 instructions, CPI = 1.5, clock = 2 GHz.

- Clock period = 1 / (2 × 10⁹) = 0.5 ns.
- Time = 4,000,000 × 1.5 × 0.5 ns = 3,000,000 ns = 3 ms.

### Example 3 — comparing two CPUs

CPU A: 3 GHz, CPI = 3. CPU B: 2 GHz, CPI = 1. Same program of 3,000,000 instructions.

- CPU A: period ≈ 0.333 ns → time = 3,000,000 × 3 × 0.333 ≈ 3 ms.
- CPU B: period = 0.5 ns → time = 3,000,000 × 1 × 0.5 = 1.5 ms.

CPU B is faster despite the lower clock, because its CPI is much better.

### Example 4 — pipeline throughput

1,000 instructions, 3 phases each.

- Without pipeline: 1,000 × 3 = 3,000 cycles.
- With a 3-stage pipeline (ideal): about 1,000 + 2 = 1,002 cycles.

Latency per instruction is unchanged; throughput is about 3× higher.

## 5. Check yourself

1. Trace `ADD R2, R3` with R2 = 4, R3 = 9, instruction at `0x400`. Final values and PC?
2. Program: 2,000,000 instructions, CPI = 2, clock = 4 GHz. Execution time?
3. CPU A: 4 GHz, CPI = 2. CPU B: 2 GHz, CPI = 0.5. Same program. Which is faster? Show the calculation.
4. Why does a pipeline not reduce latency but still make the program faster?
5. In Example 1, why is the ALU not used?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapters on the processor, performance, and pipelining.
