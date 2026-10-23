# Buses: the roads between parts

**Learning objective:** after this section, a beginner should be able to explain what a bus is, and the difference between the address bus and the data bus.

## 1. Why this matters

The CPU, memory, and other parts need to exchange information. They do it over **buses** — sets of wires that carry signals. If you do not know the buses, you cannot understand how the CPU talks to memory.

## 2. Explanation

A **bus** is a set of wires that carries information between parts of a computer. Think of it as a road: things travel along it from one place to another.

Two buses matter most:

**Address bus** — carries **addresses**. Direction: CPU → memory. The CPU says: "give me what is at this address."

**Data bus** — carries **data** (values and instructions). Direction: memory → CPU (and back). Memory says: "here is the value."

The difference is simple:

- **Address bus** = "which place?" (a location)
- **Data bus** = "what is in it?" (the content)

In kitchen terms: the address bus is the cook pointing at a shelf; the data bus is the hand bringing the item back.

There is also a **control bus**, which carries signals like "read" or "write" — telling memory whether the CPU wants to read a value or write one. For now, the two main buses (address and data) are enough.

## 3. Diagram

<img width="1942" height="809" alt="diagram7" src="https://github.com/user-attachments/assets/4087e417-bec6-473b-87ff-203acd91dd84" />


## 4. Example

The CPU wants to read the instruction at address `0x100`:

- The CPU puts `0x100` on the **address bus**.
- Memory finds the cell at `0x100`.
- Memory puts the contents of that cell on the **data bus**.
- The CPU reads the value from the data bus.

Two buses, two jobs: one says *where*, the other carries *what*.

## 5. Check yourself

1. What is a bus?
2. What does the address bus carry? In which direction?
3. What does the data bus carry? In which direction?
4. What is the difference between "which place" and "what is in it"?
5. In the kitchen analogy, what matches the address bus?

## 6. References

- Course materials (insert lecture/slide numbers).
- Patterson & Hennessy, *Computer Organization and Design* — chapter on the processor.
