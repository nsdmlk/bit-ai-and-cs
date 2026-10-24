# Network cards, latency, and bandwidth

**Learning objective:** after this section, a beginner should be able to explain what a network card does, and the difference between latency and bandwidth.

## 1. Why this matters

Computers rarely work alone. They send and receive data over networks — web pages, messages, cloud storage, AI training data. The hardware that connects a computer to a network is the **network card**, and the two numbers that describe its performance are **latency** and **bandwidth**. Confusing these two is a common beginner mistake.

## 2. Explanation

A **network card (NIC — Network Interface Card)** is the hardware that connects a computer to a network. It sends data out and receives data in. Every computer that talks to a network has one (sometimes built into the motherboard).

Two different measures describe network performance:

**Latency** — how long it takes for one piece of data to travel from one point to another. Measured in milliseconds (ms). Low latency means quick responses.

**Bandwidth** — how much data can be sent per second. Measured in megabits or gigabits per second (Mbps, Gbps). High bandwidth means more data at once.

The difference matters:

- **Latency** is about **speed of a single message**.
- **Bandwidth** is about **volume of data**.

An analogy: a highway.

- **Latency** is how long one car takes to drive from A to B.
- **Bandwidth** is how many cars can drive side by side per hour.

Adding more lanes (bandwidth) does not make any single car faster (latency). That is why a high-bandwidth connection can still feel slow if latency is high.

## 3. Diagram

<img width="1942" height="809" alt="微信图片_20261024203107_2532_8" src="https://github.com/user-attachments/assets/0f3f582b-1ee3-4511-91c3-d886a2561792" />

## 4. Example

You download a large file and make a video call.

- **Download:** bandwidth matters most. A high-bandwidth connection moves the file quickly.
- **Video call:** latency matters most. Even with high bandwidth, a high-latency connection makes the conversation feel delayed.

Same network, different needs. That is why "fast internet" is not one number — it is both latency and bandwidth.

## 5. Check yourself

1. What does a network card do?
2. What is latency? What is bandwidth?
3. Which matters more for a video call? For downloading a large file?
4. What is the highway analogy for latency and bandwidth?
5. Why can a high-bandwidth connection still feel slow?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on I/O and networks.
