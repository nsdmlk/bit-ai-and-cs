# RAM: the working memory

**Learning objective:** after this section, a beginner should be able to explain what RAM is, what it holds, and how it differs from registers and disk.

## 1. Why this matters

When you run a program, it does not run from the disk. It runs from RAM. Understanding RAM explains why "more RAM" can help some workloads, and why it does not make the CPU itself faster.

## 2. Explanation

**RAM (Random Access Memory)** is the main working memory of the computer. It is:

- **Large** — gigabytes, not kilobytes.
- **Fast** — much faster than disk, but slower than cache.
- **Temporary** — when the power goes off, RAM is empty.
- **Addressable** — every byte has an address, and the CPU can read or write any address directly.

When you start a program, it is loaded from disk into RAM. While it runs, its code and active data live in RAM. The CPU reads instructions and data from RAM (through cache) and writes results back.

The key difference:

- **Registers** hold values the CPU is using *right now* (tiny, fastest).
- **RAM** holds the program and its active data (large, fast).
- **Disk** holds everything permanently (huge, slow).

## 3. Diagram

<img width="2172" height="724" alt="微信图片_20261024132954_2473_8" src="https://github.com/user-attachments/assets/69bfb574-83dd-45f9-ad83-62ec217c8c5c" />


## 4. Example

You open a text editor.

- The editor's program file is on **disk**.
- When you launch it, it is loaded into **RAM**.
- As you type, the text is kept in **RAM**.
- The CPU reads and modifies the text through **cache** and **registers**.
- When you save, the file goes back to **disk**.

If the power goes off before saving, RAM is lost — but the disk copy remains.

## 5. Check yourself

1. What does RAM hold while a program runs?
2. How is RAM different from registers? From disk?
3. Why is RAM called "temporary"?
4. Why does a program run from RAM and not from disk?
5. Does more RAM make the CPU faster? Why or why not?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on memory hierarchy.
