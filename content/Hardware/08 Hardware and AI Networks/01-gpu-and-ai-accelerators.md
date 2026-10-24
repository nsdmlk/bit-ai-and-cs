# GPU and AI accelerators

**Learning objective:** after this section, a beginner should be able to explain what a GPU is, why AI workloads use it, and what an AI accelerator is.

## 1. Why this matters

A modern AI model runs on thousands of small calculations at once. A normal CPU is not built for that. That is why AI uses **GPUs** and **accelerators** — hardware designed for doing many things in parallel. This file connects everything you learned about the CPU to the hardware that powers AI.

## 2. Explanation

The **CPU** is designed to run a few complex tasks quickly, one after another, with lots of branching and decision-making. It has a few powerful cores.

The **GPU (Graphics Processing Unit)** is designed differently: it has **thousands of small cores** that all work at the same time. It is not good at complex logic, but it is excellent at doing the same simple operation on many pieces of data at once.

This matters for AI because AI is mostly **matrix math**: multiplying and adding huge arrays of numbers. The same operation is applied to millions of values. That is exactly what a GPU is good at.

An **AI accelerator** (like a TPU, NPU, or other specialized chip) takes this further: it is designed specifically for the operations AI models use most. It trades general-purpose flexibility for speed on a narrow set of tasks.

So the picture is:

- **CPU** — few powerful cores, good for general work.
- **GPU** — thousands of small cores, good for parallel math.
- **AI accelerator** — specialized hardware for AI operations.

This is why training a large AI model on a CPU would take months, but on a GPU or accelerator it takes days.

## 3. Diagram

<img width="1774" height="887" alt="微信图片_20261024203104_2530_8" src="https://github.com/user-attachments/assets/fc3de4af-5ec7-4352-9d3b-53c6c4998bce" />


## 4. Example

Suppose you want to multiply two large matrices (a common AI operation).

- On a **CPU**: the cores process the values a few at a time. Correct, but slow.
- On a **GPU**: thousands of cores process thousands of values at once. Much faster for this kind of work.
- On an **AI accelerator**: the hardware is built for exactly this operation, so it is even faster — but only for this kind of task.

The CPU is not "worse" — it is simply built for a different job.

## 5. Check yourself

1. How is a GPU different from a CPU?
2. Why is AI mostly "matrix math"?
3. What is an AI accelerator, and how is it different from a GPU?
4. Why can a GPU train an AI model much faster than a CPU?
5. Is a GPU always better than a CPU? Why or why not?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on parallelism.
