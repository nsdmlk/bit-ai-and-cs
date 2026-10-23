# The stored-program idea

**Learning objective:** after this section, a beginner should be able to explain what the stored-program idea is and why code and data can live in the same memory.

## 1. Why this matters

You write code in a text file, but the CPU never sees text. It sees numbers. The stored-program idea is what connects your code to those numbers: instructions are stored in memory just like data. Without this idea, computers as we know them would not exist.

## 2. Explanation

The **stored-program idea** says: **both instructions and data live in the same memory**, and the CPU reads instructions one after another and obeys them.

Before this idea, early computers had to be rewired for each new task. With it, a program is just data in memory — you load a new program, and the same machine can do something completely different.

Here is what this means in practice:

- Memory is a large array of numbered cells.
- Some cells hold **data** (numbers, text, values).
- Some cells hold **instructions** (encoded as numbers).
- The CPU does not care which is which. It just reads the next cell the PC points to and executes it.

That is why a program is called a **sequence of instructions sitting in memory**. The CPU walks through them one by one.

## 3. Diagram

[DIAGRAM: one memory block divided into two regions — "code" and "data" — with the PC pointing into the code region. Caption: "Code and data live in the same memory".]

## 4. Example

A tiny program that adds two numbers:
