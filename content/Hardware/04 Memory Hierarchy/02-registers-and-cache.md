# Registers and cache: the fast layers

**Learning objective:** after this section, a beginner should be able to explain what registers and cache are, and why they are the fastest memory in the machine.

## 1. Why this matters

The CPU cannot wait for RAM on every operation. To keep running fast, it keeps the values it needs most in the two fastest layers: registers and cache. Understanding these two explains why some programs run much faster than others.

## 2. Explanation

**Registers** are the fastest storage in the machine. They live *inside* the CPU. A typical CPU has 16–32 general-purpose registers. They hold the values the CPU is working on right now: operands, results, addresses.

Registers are tiny. You cannot fit an array in them. But for the values the CPU uses in the next microsecond, they are perfect.

**Cache** is the next layer. It is small memory (kilobytes to megabytes) that sits between the CPU and RAM. It holds **recently used data and instructions**, so the CPU can grab them again quickly.

Cache is organized in levels:

- **L1** — smallest, fastest, closest to the CPU.
- **L2** — bigger, a bit slower.
- **L3** — biggest of the caches, shared, slower than L1/L2.

The idea: when the CPU needs a value, it first checks registers, then L1, then L2, then L3, then RAM. Each step down is slower. If the value is in a cache, it is a **hit**; if not, a **miss**, and the CPU has to go to RAM.

## 3. Diagram

<img width="1774" height="887" alt="微信图片_20261024132956_2474_8" src="https://github.com/user-attachments/assets/40a333f9-0825-446a-87fd-68f2a932eca9" />


## 4. Example

A loop reads the same array element many times.

- First read: not in cache → **miss** → value comes from RAM.
- Next reads: value is now in **cache** → **hits** → much faster.
- The values being added sit in **registers** during the addition.

This is why loops that reuse the same data run faster than loops that constantly read new data.

## 5. Check yourself

1. Where do registers live? Why are they the fastest?
2. What is cache, and what does it hold?
3. What is the difference between a cache hit and a cache miss?
4. Why do loops that reuse data run faster?
5. Order these from fastest to slowest: RAM, L1 cache, registers, L3 cache.

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on memory hierarchy.
