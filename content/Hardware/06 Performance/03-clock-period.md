# Clock period: the length of one cycle

**Learning objective:** after this section, a beginner should be able to explain what clock period is, how it relates to clock frequency, and why it is only one of three performance factors.

## 1. Why this matters

Clock speed is usually given in GHz, but the formula for execution time uses **clock period** — the length of one cycle. If you do not know how to convert between the two, you cannot calculate execution time.

## 2. Explanation

**Clock period** is the time one clock cycle takes. It is the inverse of clock frequency:
clock period = 1 / clock frequency

Examples:

- 2 GHz = 2 × 10⁹ cycles per second → clock period = 1 / (2 × 10⁹) s = 0.5 ns.
- 3 GHz → clock period ≈ 0.333 ns.
- 4 GHz → clock period = 0.25 ns.

So a higher frequency means a *shorter* period — each cycle takes less time. That is why higher GHz usually helps: each cycle is shorter.

But remember: execution time is not just the clock period. It is:
execution time = instruction count × CPI × clock period


A shorter clock period helps, but if instruction count or CPI goes up, the gain can disappear. That is exactly what we saw in the previous files.

## 3. Diagram

[DIAGRAM: a timeline with three cycles marked at 2 GHz (0.5 ns each) next to three cycles at 4 GHz (0.25 ns each). Caption: "Higher frequency = shorter period".]

## 4. Example

A program needs 10,000,000 cycles.

- On a 2 GHz CPU: time = 10,000,000 × 0.5 ns = 5 ms.
- On a 4 GHz CPU: time = 10,000,000 × 0.25 ns = 2.5 ms.

Same number of cycles, half the time — because each cycle is half as long. That is the benefit of a higher clock. But if the 4 GHz CPU needed 20,000,000 cycles due to worse CPI, the gain would vanish.

## 5. Check yourself

1. What is clock period? How does it relate to clock frequency?
2. What is the clock period of a 3 GHz CPU?
3. Why does a higher frequency mean a shorter period?
4. Does a shorter clock period always make a program faster? Why or why not?
5. Convert: a 2.5 GHz clock has what period?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on performance.
