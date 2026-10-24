# Repeat and the clock: why the cycle never stops

**Learning objective:** after this section, a beginner should be able to explain why the fetch–decode–execute cycle repeats and what the clock does.

## 1. Why this matters

A program is not one instruction — it is millions or billions of them. The CPU runs them by repeating the same three phases over and over. The **clock** is what keeps this loop moving at a steady pace.

## 2. Explanation

After execute finishes, the cycle **repeats** with the next PC value. The CPU goes back to fetch, reads the next instruction, decodes it, executes it, and so on. This loop never stops while the program runs.

What drives the loop is the **clock**. The clock is a signal that ticks at a fixed rate. Each tick is one **cycle**. A 3 GHz clock ticks about 3 billion times per second — about 0.33 nanoseconds per cycle.

The clock does not decide *what* to do. It decides *when* to move to the next step. It is the heartbeat: every phase of the cycle is timed by it.

In kitchen terms: the clock is the rhythm of the kitchen — the pace at which the cook moves from one step to the next.

## 3. Diagram

<img width="2048" height="768" alt="微信图片_20261024110611_2435_8" src="https://github.com/user-attachments/assets/129a9a8e-8c45-412a-8387-3acb83e6c7b7" />


## 4. Example

A program with 1,000 instructions:

- Instruction 1: fetch, decode, execute.
- Instruction 2: fetch, decode, execute.
- …
- Instruction 1,000: fetch, decode, execute.

Each phase takes some number of clock cycles. The total time is the sum of all cycles across all instructions. That is why the clock rate matters — but, as we will see in the Performance file, it is not the only thing that matters.

## 5. Check yourself

1. Why does the cycle repeat?
2. What does the clock do? What does it *not* do?
3. A 3 GHz clock ticks how many times per second? How long is one cycle?
4. In the kitchen analogy, what does the clock match?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on the processor.
