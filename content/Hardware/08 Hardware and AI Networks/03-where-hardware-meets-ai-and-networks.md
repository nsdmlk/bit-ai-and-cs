# Where hardware meets AI and networks

**Learning objective:** after this section, a beginner should be able to explain how the hardware topics connect to the AI and networks parts of the project.

## 1. Why this matters

Our project covers three areas: hardware, behavioral AI, and networks. They are not separate — they meet in specific places. This file shows those meeting points, so you can see the whole picture instead of three isolated topics.

## 2. Explanation

Here is where hardware meets the other two parts.

**Hardware ↔ AI:**

- AI models are mostly **matrix math**, so they run best on hardware built for parallel work: **GPUs** and **AI accelerators**.
- The **memory hierarchy** matters: AI models are huge, and moving data between RAM, cache, and the chip is often the bottleneck.
- **Performance** matters: instruction count, CPI, and clock period apply to AI workloads too — but on a GPU, the "instructions" are parallel operations on many values.

**Hardware ↔ Networks:**

- The **network card (NIC)** is the hardware that connects a computer to a network.
- **Latency and bandwidth** describe network performance, and they depend on hardware: the NIC, the cables, the switches.
- **Buses** inside the computer connect the NIC to the CPU and memory — the same buses you learned about in the CPU files.
- In data centers, networks connect thousands of machines; the hardware of those networks decides how fast AI training can run across many GPUs.

**The common thread:** every AI model runs on hardware, and every network message travels through hardware. Software decides *what* to do; hardware decides *how fast* it can be done.

## 3. Diagram

[DIAGRAM: three overlapping circles — Hardware, AI, Networks — with the overlaps labeled: "GPUs/accelerators", "memory bottlenecks", "NICs", "latency/bandwidth", "buses". Caption: "Where the three parts meet".]

## 4. Example

Training an AI model across multiple machines:

- **Hardware:** each machine has GPUs and a NIC.
- **AI:** the model is split across GPUs, which do the matrix math in parallel.
- **Networks:** the GPUs exchange data over the network — latency and bandwidth decide how fast they can cooperate.

If the network is slow (high latency, low bandwidth), the GPUs sit idle waiting for data. The AI is only as fast as the hardware and network allow.

## 5. Check yourself

1. Why do AI workloads use GPUs and accelerators?
2. How does the memory hierarchy matter for AI?
3. What hardware connects a computer to a network?
4. How do latency and bandwidth affect AI training across machines?
5. In your own words: why are hardware, AI, and networks not separate topics?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapters on parallelism and I/O.
