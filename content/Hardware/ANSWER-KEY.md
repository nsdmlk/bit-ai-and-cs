# Hardware — explained answer key

**Status:** Revised on 26 October 2026 with AI-assisted technical checks; awaiting team peer review.

[Reading order and learning goals](OUTLINE.md) · [Teaching-machine conventions](OUTLINE.md#teaching-machine-conventions)

Attempt each lesson's questions before opening its answers. The explanations below use the lesson's stated assumptions. Reflection/sample responses illustrate an acceptable approach and are not uniquely correct. Technical sources are listed with each linked lesson.

## H01-01

Lesson: [Why hardware matters](01%20What%20is%20Hardware/01-why-hardware-matters.md).

**1. In your own words: why does a program need hardware?**

Instructions represented by bits do not execute themselves. Physical circuits must fetch them, choose operations, move data and produce output; that is the role of hardware.

**2. What does "software is the recipe, hardware is the kitchen" mean?**

The recipe represents the operations described by software; the kitchen represents the equipment that carries them out. The analogy separates a description from the physical system performing it.

**3. Why does knowing hardware help you understand why a program is slow?**

Hardware knowledge suggests testable causes of slowness, such as many executed instructions, cache misses or time waiting for I/O. Measurement is still needed to decide which cause dominates a particular program.

**4. Give one example of a program you use, and name two hardware parts it depends on.**

Example: a video player uses working memory to buffer frames and a processor or decoder to produce pictures. The display is an output device, while a local file also depends on persistent storage. Other valid examples should connect each named part to a specific job.

## H01-02

Lesson: [The hardware groups used in this project](01%20What%20is%20Hardware/02-five-parts-of-a-computer.md).

**1. Name the hardware groups used in this project.**

CPU executes instructions; RAM holds active code/data; persistent storage retains saved files; I/O exchanges information with devices or users. A NIC provides networking as one kind of I/O. This is our project grouping, not five independent universal components.

**2. Which group is working memory, and which retains saved data without power?**

Ordinary DRAM is volatile working memory: it needs power to retain information. SSD/disk storage retains saved data without power. Persistent storage can still fail, so persistence is not a guarantee of permanent safety.

**3. What does I/O mean, and give two examples.**

I/O means input/output. A keyboard supplies input, a display supplies output, and a NIC can both receive and send data. Each connects the computation to something outside the CPU and main memory.

**4. Why is a computer "not one thing"?**

A computer works through cooperation: a CPU needs instructions and operands, memory holds them, and devices provide useful input/output. No single named part performs every role by itself.

**5. Which part connects your computer to the internet?**

A network interface controller (NIC), wired or wireless, connects the machine to a network. Reaching the wider Internet also depends on a working network path, routing and other configuration; having a NIC alone does not guarantee Internet access.

## H01-03

Lesson: [The kitchen analogy](01%20What%20is%20Hardware/03-kitchen-analogy.md).

**1. Which kitchen part matches the CPU? Which matches RAM?**

The cook models the CPU and the counter/fridge models working memory. The cook uses ingredients kept close by, just as instructions operate on values supplied by the memory hierarchy.

**2. Why is storage like a pantry, and not like the counter?**

The pantry models persistent capacity that is generally slower to access than working memory. The counter models the smaller active workspace. Real storage differs in technology and access method, so the walking distance is only an analogy.

**3. What do the buses match in the kitchen?**

The hands and transfer window model communication paths carrying addresses, data and control. The analogy helps show movement between parts; it does not describe a particular electrical bus protocol.

**4. In your own words: why does the analogy help you understand hardware?**

Illustrative response: I can remember the CPU as the cook and working memory as the counter, then ask which component holds or transforms a value. A good answer explains a useful connection, rather than only naming kitchen objects.

**5. Where does the analogy break down? Name one thing a kitchen cannot show.**

Example limit: real caches automatically retain blocks of bytes, and CPU instructions can overlap in a pipeline. A single cook does not show these mechanisms accurately. Electrical timing and memory permissions also need explanations beyond the analogy.

## H02-01

Lesson: [PC and IR: where the CPU keeps its place](02%20Inside%20the%20CPU/01-pc-and-ir.md).

**1. What does the PC hold? What does the IR hold?**

PC holds an instruction address; IR holds the fetched instruction in our teaching model. During decode/execute, PC has already advanced to the following sequential address, while IR retains the current instruction.

**2. Why does PC already point to the following instruction during execute in our teaching model?**

Our model deliberately advances PC during fetch. That preserves the following fetch address while the fetched instruction is decoded and executed. The timing and architectural meaning of PC are implementation/model dependent, and a branch can redirect it.

**3. What would happen if the CPU had no PC?**

It would need some other mechanism to identify which instruction to fetch. Removing the name PC does not remove the need to track control flow.

**4. What would happen if the CPU had no IR?**

Our teaching CPU would need another way to retain or supply the current instruction while decoding/executing it. A single IR is a simple model; real pipelines can retain several instructions in different internal structures.

## H02-02

Lesson: [Registers and the ALU: where values live and where math happens](02%20Inside%20the%20CPU/02-registers-and-alu.md).

**1. What are registers, and why are they fast?**

Registers are small storage locations in the CPU, directly named by instructions. Their on-chip implementation and short access paths make them suitable for operands and intermediate results. Exact timing depends on the processor.

**2. What does the ALU do? Give two examples of operations.**

An ALU performs arithmetic and logical operations, such as addition and bitwise AND. Multiplication/division may be handled by separate functional units; not every arithmetic operation must use the same circuit.

**3. In `ADD R1, R2`, what goes into the ALU, and where does the result go?**

The two-operand shorthand means R1 receives R1 + R2. The existing R1 and R2 values are the inputs, and the sum replaces R1; R2 is unchanged. For 5 and 3, the result is R1 = 8.

**4. Why can't the CPU keep all its values in registers?**

Only a limited number of architectural registers are available. Large arrays, program state and many live values require other memory; compilers choose what to keep in registers and explicitly load/store other values.

## H02-03

Lesson: [The control unit: the manager of the CPU](02%20Inside%20the%20CPU/03-control-unit.md).

**1. What does the control unit do?**

The control unit interprets the instruction and generates signals selecting data paths and actions, such as register reads, an ALU operation and a destination write. It coordinates execution rather than being the operand store.

**2. Does the control unit do math? Why or why not?**

In our functional division, the ALU and other execution units perform arithmetic on program values. The control unit selects and sequences those operations; real control circuitry can still contain internal state and logic.

**3. In `ADD R1, R2`, what signals does the control unit send?**

For ADD R1, R2, control selects R1 and R2 as inputs, chooses addition and enables writing the result into R1. No write to R2 is requested.

**4. What does the control unit determine during decode, and why are control signals also needed in other phases?**

Decode determines the operation, operands and destination. Control signals are also needed to fetch an instruction, read/write memory and commit a result, so control is not active only during decode.

## H02-04

Lesson: [Buses: the roads between parts](02%20Inside%20the%20CPU/04-buses.md).

**1. What is a bus?**

A bus/interconnect is a communication path plus rules for exchanging information. Our simple diagrams separate address, data and control signals; real systems may use packetised or combined channels.

**2. What does the address bus carry? In which direction?**

It carries a location to access. In the CPU-initiated memory read in the lesson, the address travels from CPU to memory. This direction describes that example, not every possible bus master.

**3. What does the data bus carry? In which direction?**

It carries the instruction or data value. A read transfers data from memory to CPU; a write transfers data from CPU to memory.

**4. What is the difference between "which place" and "what is in it"?**

The address identifies where to access; the data is the content being transferred. The address 0x100 and the instruction stored there are different kinds of information.

**5. In the kitchen analogy, what matches the address bus?**

Pointing at a particular shelf models choosing an address. Bringing the ingredient back models carrying its data. This separates location from content.

## H03-01

Lesson: [Fetch: get the next instruction](03%20Fetch%20Decode%20Execute/01-fetch.md).

**1. What question does fetch answer?**

Fetch obtains the instruction to process from the address indicated by PC. It prepares the instruction for decode; it does not yet perform its arithmetic or memory-data operation.

**2. List the five steps of fetch in order.**

In our teaching model: (1) PC supplies the instruction address; (2) CPU sends it on the address path; (3) memory returns instruction bits on the data path; (4) IR retains those bits; (5) PC advances by four for the following sequential instruction.

**3. Why does PC already point to the following instruction during execute in this teaching model?**

Because this teaching cycle updates PC during fetch, before execution. The fetched instruction remains in IR, so it is still available even after PC changes. Branches and other implementations require additional details.

**4. Which bus carries the address, and which carries the instruction?**

The address path carries the instruction location; the data path carries its encoded bits back. Both are needed to distinguish which location is requested from what it contains.

**5. In the kitchen analogy, what does fetch match?**

The cook reads the next recipe step and keeps it in mind, while moving the bookmark to the following step. This is only a model of sequencing and instruction retention.

## H03-02

Lesson: [Decode: figure out what the instruction means](03%20Fetch%20Decode%20Execute/02-decode.md).

**1. What question does decode answer?**

Decode interprets the encoded instruction: which operation should run, where the inputs come from and where the result should go.

**2. What three things does the control unit work out during decode?**

It determines the operation, the operands or address information, and the destination. These choices become control signals for the data paths and execution units.

**3. Does decode change the destination register or data memory in our model? What does it prepare?**

No program destination register or data-memory result changes yet in our model. Decode prepares signals and can read operands into internal working state; saying no values anywhere change would be too broad.

**4. In `LOAD R1, [0x200]`, what does the control unit work out?**

For LOAD R1, [0x200], the operation is a load, the supplied absolute address is 0x200, and R1 is the destination register. A real base-plus-offset form would additionally require address calculation.

**5. In the kitchen analogy, what does decode match?**

The cook interprets the current recipe step and selects ingredients/tools. The actual transformation happens in the execution analogy, after that preparation.

## H03-03

Lesson: [Execute: actually do it](03%20Fetch%20Decode%20Execute/03-execute.md).

**1. What question does execute answer?**

Execute performs the instruction operation, which may calculate a value, transfer data or redirect control flow. Here we show register arithmetic and data-memory transfers.

**2. What happens during execute for an `ADD` instruction?**

Read the named registers, supply their values to the arithmetic unit, add them, and write the result to the destination. With ADD R1, R2 and inputs 5 and 3, R1 becomes 8 and R2 remains 3.

**3. What happens during execute for a `LOAD` instruction?**

For LOAD R1, [0x200], request data at memory address 0x200 and transfer the returned value into R1. Our pseudocode supplies an absolute address; cache and address-generation details are abstracted away.

**4. What moves during `LOAD`, and how might a real processor calculate its memory address?**

A load moves data from memory to a register. A real processor may calculate the effective address from a base register plus an offset, using an ALU or dedicated address-generation unit. Our complete absolute address does not show that calculation.

**5. In the kitchen analogy, what does execute match?**

The cook actually transforms or moves the ingredients: chopping/stirring resembles computation, while bringing an ingredient to the workspace resembles a data transfer. The analogy does not describe the electrical implementation.

## H03-04

Lesson: [Repeat and the clock: why the cycle never stops](03%20Fetch%20Decode%20Execute/04-repeat-and-clock.md).

**1. Why does the cycle repeat?**

A program normally needs many instructions. After one is processed, the control-flow mechanism supplies the next instruction address, so the CPU repeats the cycle. Other software can run when this program finishes or waits.

**2. What does the clock do? What does it *not* do?**

The clock provides timing boundaries for state changes. It does not decide the operation or the meaning of a program; instructions and control logic do that. Our examples assume a constant rate, although real CPU frequency can vary.

**3. A 3 GHz clock ticks how many times per second? How long is one cycle?**

3 GHz is 3 × 10^9 cycles per second. One period is 1 / (3 × 10^9) seconds, approximately 0.333 × 10^-9 seconds = 0.333 ns.

**4. In the kitchen analogy, what does the clock match?**

The kitchen rhythm models when work steps advance. Unlike this simple analogy, a processor can have many operations in flight, and a phase need not correspond to exactly one tick.

## H03-05

Lesson: [Worked examples: tracing instructions](03%20Fetch%20Decode%20Execute/05-worked-examples.md).

**1. Trace `ADD R5, R6` with R5 = 7, R6 = 2, instruction at `0x300`. What are the final values and the new PC?**

The instruction at 0x300 is fetched into IR and PC advances to 0x304. Decode selects addition of R5 and R6, writing R5. Execute computes 7 + 2 = 9. Final values: R5 = 9, R6 = 2, PC = 0x304.

**2. Trace `LOAD R2, [0x400]`, located at instruction address `0x300`, with PC initially `0x300`. Memory at `0x400` holds 99. Assume a four-byte instruction. What is R2, and what is the new PC?**

Fetch starts at the separate instruction address 0x300 and advances PC to 0x304. Execute reads the value 99 at data address 0x400 into R2. Final values: R2 = 99, PC = 0x304. Do not confuse the data address with the instruction address.

**3. In all three examples, what stays the same? What changes?**

The same teaching sequence is fetch, decode and execute, with a four-byte sequential PC increment. The operation, operand locations, destination and computed/transferred value vary with the instruction.

**4. Why does the PC always increase by 4 in these examples?**

Each example explicitly uses a four-byte instruction in byte-addressed memory and contains no taken branch. Other instruction sizes or control transfers can produce a different next address.

## H04-01

Lesson: [Why memory has layers](04%20Memory%20Hierarchy/01-why-layers.md).

**1. Why can't a computer have one memory that is both huge and fast?**

Fast on-chip storage costs more area/cost per stored bit, while denser or persistent technologies usually have higher access latency. A useful machine combines technologies to balance capacity, cost and speed rather than assuming one technology can provide every advantage.

**2. List the four layers from fastest to slowest.**

For the typical hierarchy shown: registers, cache, RAM, then SSD/disk, ordered by increasing access latency. This is a broad teaching order; exact timings and device configurations vary.

**3. Which layer is closest to the CPU? Which is farthest?**

Registers and first-level caches are within the core; main memory and storage are farther along the access paths. Proximity alone does not determine speed: technology, circuitry and the access method also matter.

**4. Why does the hierarchy make a computer feel faster than RAM alone would?**

Locality means many accesses reuse the same or nearby locations. Registers and caches can supply these values with lower latency, reducing how often a load must wait for main memory.

## H04-02

Lesson: [Registers and cache: the fast layers](04%20Memory%20Hierarchy/02-registers-and-cache.md).

**1. Where do registers live? Why are they the fastest?**

Registers are inside the CPU and explicitly selected by instructions. Their small size and on-chip implementation allow rapid operand access; they are not a memory-address cache searched automatically by a load.

**2. What is cache, and what does it hold?**

Cache is a hardware-managed store of memory blocks, including data and instructions. It helps satisfy memory requests without reaching slower levels every time.

**3. What is the difference between a cache hit and a cache miss?**

A hit means the specified cache level contains the requested block. A miss means that level does not; another cache may still hit. Only a miss in all relevant caches necessarily proceeds toward main memory in this model.

**4. Why do loops that reuse data run faster?**

Reusing data soon gives temporal locality, so later loads may find the block in cache. Accessing nearby new elements can benefit from spatial locality too. Actual speed also depends on the rest of the loop and compiler behaviour.

**5. Order these from fastest to slowest: RAM, L1 cache, registers, L3 cache.**

Typical order by access latency: registers, L1 cache, L3 cache, RAM. This orders the requested choices; L2 normally lies between L1 and L3.

## H04-03

Lesson: [RAM: the working memory](04%20Memory%20Hierarchy/03-ram.md).

**1. What does RAM hold while a program runs?**

It holds working code/data made available to the running system. Registers and caches hold active values/blocks closer to execution, while the stored file remains on persistent storage.

**2. How is RAM different from registers? From disk?**

Registers are tiny and explicitly named by instructions; RAM is much larger working memory accessed through addresses and the cache system. SSD/disk retains saved files without power but usually has higher access latency.

**3. Why is RAM called "temporary"?**

Ordinary DRAM is volatile: maintaining its information requires power and refresh. Saved storage is non-volatile, although not immune to loss or failure.

**4. Why is code fetched through working memory rather than read directly from disk in our desktop example?**

The desktop memory system supplies instruction bytes at much lower latency than a disk and supports the fine-grained access needed for execution. The OS loads/maps code into working memory; embedded execution directly from flash is a different case.

**5. Does more RAM make the CPU faster? Why or why not?**

More RAM does not raise the processor clock or automatically lower instruction latency. It can improve whole-program performance if it avoids paging or allows a useful working set to remain resident; an already CPU-bound workload may not benefit.

## H04-04

Lesson: [Storage: the persistent layer](04%20Memory%20Hierarchy/04-storage.md).

**1. What does storage hold?**

Persistent storage retains saved operating-system files, applications and user data without power. It does not automatically save unsaved edits held only in memory.

**2. Why is storage slower than RAM?**

DRAM, flash SSDs and magnetic disks use different technologies/interfaces and access methods. SSD/disk accesses generally have higher latency than working-memory accesses; this is not simply because the device is larger.

**3. Why is storage still essential even though it is slow?**

Without persistent storage or another persistent source, saved files would not survive a loss of power. Working memory provides speed, while persistent storage provides retention.

**4. What happens when a program needs data from storage?**

In this desktop example, the system transfers requested file data into RAM buffers; the CPU can then work through registers/cache. Large files can be streamed in chunks instead of loaded completely at once.

**5. Order these by speed, fastest first: storage, RAM, cache, registers.**

Typical order from lowest access latency: registers, cache, RAM, storage. The comparison is about access latency, not a guarantee that every transfer or whole workload has that ranking.

## H05-01

Lesson: [The stored-program idea](05%20How%20Program%20Runs/01-stored-program-idea.md).

**1. What does the stored-program idea say?**

A program is represented by instructions stored in memory rather than by physically rewiring the machine for each task. Our shared-address-space example stores instruction bytes and data in the same overall memory system.

**2. Why is it useful that code and data live in the same memory?**

The same hardware can run different computations by loading different instruction sequences. The bit representation also lets programs be stored and moved as data; permissions still limit what may be executed or changed.

**3. How are instructions and data both represented, and why can memory permissions still distinguish executable and non-executable regions?**

Both are represented by bits. Whether an access fetches an instruction or reads data depends on the operation. Modern systems can mark pages non-executable or read-only, so a shared address space does not mean unrestricted execution of every cell.

**4. What does the PC point to in the example above?**

At the start PC = 0x100 identifies the first LOAD. In our fetch model it advances through 0x104, 0x108, 0x10C and then 0x110. The separate data addresses 0x300–0x308 do not become the PC just because data is loaded or stored.

## H05-02

Lesson: [The compiler: from code to instructions](05%20How%20Program%20Runs/02-compiler-and-instructions.md).

**1. What does a compiler do?**

A compiler translates a program to another representation. A native toolchain can produce CPU machine code; CPython and Java commonly involve bytecode and an interpreter or virtual machine. Translation steps depend on the language implementation.

**2. Why does the CPU not understand variables?**

Source names such as b are abstractions used by the language implementation. Native instructions refer to encoded operands such as register identifiers, addresses and constants rather than understanding the source variable name.

**3. What do variables become after compilation?**

In a native translation, live values may occupy registers or memory locations, or be optimised away. For languages using a runtime, values can also be represented by runtime objects. A one-to-one fixed source-variable/address mapping is not guaranteed.

**4. Why can the same code produce different numbers of instructions on different compilers?**

Compilers can choose different instruction sequences and optimisations, and target different instruction sets. Fewer instructions alone does not prove lower time because CPI and clock behaviour matter too.

**5. In the example, why might the compiler skip the two `load` instructions?**

If b/c already occupy suitable registers, fetching the same values from memory is unnecessary. The result needs ADD plus STORE when a must reach memory, or only ADD when a may remain in a register.

## H05-03

Lesson: [Worked example: `a = b + c`](05%20How%20Program%20Runs/03-example-a-equals-b-plus-c.md).

**1. Why are there two `load` instructions before the `add`?**

This illustrative translation assumes b and c start in memory, while ADD takes register operands. The loads bring 4 and 6 into R1 and R2 before the arithmetic instruction uses them.

**2. What are the values of R1, R2, R3 after step 3?**

R1 = 4, R2 = 6, R3 = 10. The three-operand form ADD R3, R1, R2 writes the sum into R3 without overwriting either input.

**3. What does the `store` instruction do?**

It copies R3 = 10 into the data-memory location 0x308. It does not move the instruction address or erase the register value.

**4. If `b` and `c` were already in registers, how many instructions are needed when `a` must be stored in memory? What if the result may remain in a register?**

With input values already in registers, ADD plus STORE gives two instructions if a must be written to memory. If the required result may stay in a register, only ADD is needed. The observable output requirement decides which case applies.

**5. What is the final value of `a`?**

a = 10, stored at address 0x308. The trace shows why: load 4, load 6, add them, then store the resulting 10.

## H06-01

Lesson: [Why "more GHz" is not the same as "faster"](06%20Performance/01-why-ghz-is-not-speed.md).

**1. What does GHz actually measure?**

GHz measures billions of clock cycles per second, not instructions, completed tasks or data bytes per second. The work performed in a cycle depends on the program and processor.

**2. Why is a cycle not a fixed amount of work?**

Different operations and implementations have different completion rates, and instructions may overlap. One tick is a timing interval rather than a fixed semantic task.

**3. Name the three factors that decide execution time.**

The model factors are dynamic instruction count, average cycles per completed instruction (CPI), and clock period. Their product gives CPU execution time at the assumed constant frequency.

**4. Can a 3 GHz CPU be faster than a 4 GHz CPU? Why?**

Yes. If the 3 GHz system needs sufficiently fewer total cycles, it can finish sooner. For example, lower CPI can outweigh a longer clock period; compare all factors for the same required task.

**5. What would you look at instead of GHz to compare two CPUs?**

Measure time for a representative workload and report the input and conditions. CPU-time analysis can help explain the result; elapsed-time benchmarks also include I/O and other waits. Clock rate alone is insufficient.

## H06-02

Lesson: [Instruction count and CPI](06%20Performance/02-instruction-count-and-cpi.md).

**1. What is instruction count? What three things affect it?**

Dynamic instruction count is the total instructions executed, counting repetitions. Algorithm/input, compiler choices and instruction set can all affect it. The number of written source lines or distinct encoded instructions is not the same quantity.

**2. What is CPI? What three things affect it?**

Average CPI is CPU cycles divided by completed instructions. Instruction mix, pipeline execution and memory stalls can affect it. It describes a rate over the measured run, not one instruction's individual latency.

**3. How do instruction count and CPI combine to give total cycles?**

Total CPU cycles = dynamic instruction count × average CPI, by the definition of average CPI. Multiplying those cycles by seconds per cycle produces CPU time.

**4. Can a program with more instructions be faster? Why?**

Yes. In the example, version B executes 1.5 million instructions × 1 cycle/instruction = 1.5 million cycles, less than A's 1 million × 2 = 2 million. At equal clock rate, B finishes first.

**5. Why does a cache miss raise CPI?**

A miss that delays progress adds cycles without a corresponding increase in completed useful instructions. Some delays can overlap with other work, so the actual CPI impact depends on the processor and workload.

## H06-03

Lesson: [Clock period: the length of one cycle](06%20Performance/03-clock-period.md).

**1. What is clock period? How does it relate to clock frequency?**

Clock period is seconds per cycle; frequency is cycles per second. For a constant clock, period = 1/frequency, so the units and quantities are reciprocals.

**2. What is the clock period of a 3 GHz CPU?**

1 / (3 × 10^9) s = approximately 0.333 ns. Keeping the unrounded fraction until the final answer avoids accumulating rounding error.

**3. Why does a higher frequency mean a shorter period?**

More cycles fit into each second, so each cycle must take less time. Doubling a constant frequency halves its period.

**4. Does a shorter clock period always make a program faster? Why or why not?**

Only if total required cycles do not rise enough to cancel the gain. CPU time equals total cycles × period; elapsed time can additionally contain waits outside CPU execution.

**5. Convert: a 2.5 GHz clock has what period?**

1 / (2.5 × 10^9) s = 0.4 × 10^-9 s = 0.4 ns.

## H06-04

Lesson: [Worked calculation: putting it all together](06%20Performance/04-worked-calculation.md).

**1. Write the execution time formula.**

CPU execution time = dynamic instruction count × average CPI × clock period = (dynamic instruction count × average CPI) / clock frequency. Use a consistent constant-clock model and distinguish I/O/scheduling waits.

**2. A program has 1,000,000 instructions, CPI = 2, clock = 2 GHz. What is the execution time?**

1,000,000 instructions × 2 cycles/instruction = 2,000,000 cycles. Divide by 2 × 10^9 cycles/s to get 0.001 s = 1 ms.

**3. A program has 3,000,000 instructions, CPI = 1.5, clock = 3 GHz. What is the execution time?**

3,000,000 × 1.5 = 4,500,000 cycles. Dividing by 3 × 10^9 cycles/s gives 0.0015 s = 1.5 ms.

**4. CPU A: 2 GHz, CPI = 1. CPU B: 4 GHz, CPI = 3. Which is faster for the same program? Show your calculation.**

Assuming equal dynamic instruction counts N: A takes N × 1/(2 × 10^9) = N × 0.5 ns; B takes N × 3/(4 × 10^9) = N × 0.75 ns. A is faster; B's time divided by A's time is 1.5.

**5. Why can two CPUs with different GHz have the same execution time?**

A higher frequency can be offset by a larger dynamic instruction count or average CPI. In the worked example both systems require 2 ms because the CPI/frequency ratio is equal.

## H07-01

Lesson: [The problem with doing one thing at a time](07%20Pipelining/01-problem-with-sequence.md).

**1. Why is the sequential cycle inefficient?**

With no overlap, later instructions wait while one instruction passes through each stage, leaving some stage resources unused. This is a limitation of the specified teaching design, not a claim that every CPU circuit is idle except one.

**2. Which parts of the CPU are idle during fetch? During execute?**

During fetch, some arithmetic execution resources may wait, although address updates can still use an adder. During execute, fetch resources may wait in the unpipelined model, but a load/store still uses memory. The exact resource use depends on the datapath.

**3. In the example, how many cycles do 3 instructions take?**

3 instructions × 3 cycles/instruction = 9 cycles, because the model does not overlap any stages. The timeline runs from cycle 1 through cycle 9.

**4. In the kitchen analogy, what is idle while the cook reads the recipe?**

The stove may wait while the cook reads the next step. This illustrates an unused execution resource; it does not imply a real fetch operation cannot use arithmetic circuitry.

**5. What would you want to overlap to save time?**

Fetch of a later instruction, decode of another and execution of an earlier one can overlap if resources and dependencies allow it. That is the basic pipeline idea.

## H07-02

Lesson: [The assembly-line idea](07%20Pipelining/02-assembly-line-idea.md).

**1. What does pipelining overlap?**

It overlaps stages belonging to different instructions. Several instructions are in flight, but each occupies a different stage in the ideal single-issue teaching pipeline.

**2. Does pipelining make a single instruction faster? Why or why not?**

The goal is higher throughput. With the same one-cycle stages and same clock period, an instruction still spans three cycles; real pipeline overhead or clock changes may alter its latency.

**3. In the example, how many cycles do 3 instructions take with a pipeline? Without?**

The non-overlapping version takes 9 cycles. The ideal pipeline takes 5: I1 finishes in cycle 3, I2 in cycle 4 and I3 in cycle 5. The initial fill explains why three instructions do not finish in only three cycles.

**4. What is the assembly-line analogy for pipelining?**

Each factory station performs a stage on a different car. After the line fills, cars finish more often even though each car still passes through all stations. Idle stations, unbalanced work or missing parts limit the real gain.

**5. Why does the CPU finish instructions more often with a pipeline?**

Different stages work concurrently on different instructions, so after filling, the ideal line completes one per cycle. This improves the rate of completion without shortening each instruction's three-stage path in this model.

## H07-03

Lesson: [Throughput: why the pipeline is faster overall](07%20Pipelining/03-throughput.md).

**1. What is latency? What is throughput?**

Latency is start-to-finish time for one operation. Throughput is completed operations per time interval. Their units differ: time/operation versus operations/time.

**2. In our ideal model, what happens to latency? Why might a real pipeline differ?**

In our equal-clock, three-stage ideal model, latency stays at three cycles. Real pipeline registers add overhead and a real clock may change, so actual instruction latency need not remain identical.

**3. How does pipelining increase throughput?**

It overlaps work on multiple instructions. Once full, the ideal pipeline completes one instruction each cycle instead of waiting three cycles between completions.

**4. In the example, how many cycles does the pipelined version take? The non-pipelined version?**

For n = 1,000 and three one-cycle stages: non-overlapping execution takes 3n = 3,000 cycles; the ideal pipeline takes n + 2 = 1,002 cycles. Equal clock period is required to compare those counts directly as time.

**5. What is the highway analogy for throughput?**

Additional lanes illustrate more cars arriving per hour without shortening the route taken by one car. This models the difference between throughput and latency, although an assembly line more closely matches stage overlap.

## H08-01

Lesson: [GPU and AI accelerators](08%20Hardware%20and%20AI%20Networks/01-gpu-and-ai-accelerators.md).

**1. How is a GPU different from a CPU?**

A CPU has general-purpose cores suited to low-latency control-heavy work as well as parallel execution. A GPU exposes many parallel arithmetic resources to achieve high throughput on suitable data-parallel workloads. GPU execution lanes are not directly equivalent to CPU cores.

**2. Why do large neural networks contain much matrix arithmetic, and why does that not describe every AI algorithm?**

Neural-network layers often combine large arrays through multiply/add operations, exposing parallel work. AI also includes small tabular methods, search and control logic, so it is inaccurate to identify all AI with large matrix calculations.

**3. What is an AI accelerator, and how is it different from a GPU?**

An AI accelerator specialises in a set of model operations or numerical formats. It may trade flexibility for efficiency, but performance depends on supported work and is not automatically higher than every GPU.

**4. Why can a GPU train an AI model much faster than a CPU?**

For a sufficiently large parallel workload, a GPU can execute many arithmetic operations concurrently. Benefits depend on utilisation, memory, precision and transfers; no fixed months-versus-days gain follows without a specified measurement.

**5. Is a GPU always better than a CPU? Why or why not?**

No. A small task, branch-heavy logic or expensive host/device transfer can favour a CPU. Compare a representative end-to-end workload rather than choosing from a universal device ranking.

## H08-02

Lesson: [Network cards, latency, and bandwidth](08%20Hardware%20and%20AI%20Networks/02-nic-latency-bandwidth.md).

**1. What does a network card do?**

A NIC sends and receives data on a network link and connects that link to the host system. It is an I/O device and may be integrated rather than a separate plug-in card.

**2. What is latency? What is bandwidth?**

Latency is a specified delay, such as one-way delay or round-trip time. Bandwidth here means capacity in bits/second; throughput is the rate actually achieved. State the measurement endpoints and distinguish bits from bytes.

**3. Which matters more for a video call? For downloading a large file?**

A video conversation needs low delay for responsive turn-taking, and still needs sufficient throughput for its media rate. A large download benefits from higher available throughput; loss, latency and protocol behaviour can also affect it.

**4. What is the highway analogy for latency and bandwidth?**

Travel time along the road models latency, and lane capacity models how much traffic can pass. The analogy is limited: network link rate affects packet serialisation time, and queueing changes delay.

**5. Why can a high-bandwidth connection still feel slow?**

A long propagation path, queues, remote processing or other bottlenecks can create delay even on a high-capacity link. More capacity alone does not remove every source of latency.

## H08-03

Lesson: [Where hardware meets AI and networks](08%20Hardware%20and%20AI%20Networks/03-where-hardware-meets-ai-and-networks.md).

**1. Why do AI workloads use GPUs and accelerators?**

Some neural-network operations expose large parallel matrix work that suits GPUs/accelerators. Small tabular RL or control-heavy work may suit CPUs. Device choice follows the workload, not simply the label AI.

**2. How does the memory hierarchy matter for AI?**

Models and batches must fit and move through the relevant memory system. Limited capacity or transfer bandwidth can leave arithmetic resources waiting, so data movement as well as arithmetic throughput affects performance.

**3. What hardware connects a computer to a network?**

The NIC is the I/O hardware linking a machine to its network. Interconnects such as PCIe can link it to the host; the network path also includes switches, links and other machines.

**4. How do latency and bandwidth affect AI training across machines?**

Communication delays and limited transfer rates can stall synchronisation or model/data exchanges. The effect depends on how computation is distributed and whether communication overlaps useful work.

**5. In your own words: why are hardware, AI, and networks not separate topics?**

Illustrative response: a robot processes observations on physical compute/memory hardware and may exchange data through network interfaces. Algorithms choose operations, while software, hardware and communication jointly determine behaviour and timing. Explain a concrete connection rather than just naming three areas.

## H09-01

Lesson: [Worked examples: putting it all together](09%20Practice%20and%20Summary/01-worked-examples.md).

**1. Trace `ADD R2, R3` with R2 = 4, R3 = 9, instruction at `0x400`. Final values and PC?**

Fetch from 0x400 advances PC to 0x404. Decode the shorthand ADD R2, R3 as R2 ← R2 + R3. Execute 4 + 9 = 13. Final: R2 = 13, R3 = 9, PC = 0x404.

**2. Program: 2,000,000 instructions, CPI = 2, clock = 4 GHz. Execution time?**

2,000,000 × 2 = 4,000,000 cycles. At 4 × 10^9 cycles/s, CPU time = 0.001 s = 1 ms.

**3. CPU A: 4 GHz, CPI = 2. CPU B: 2 GHz, CPI = 0.5. Same program. Which is faster? Show the calculation.**

For equal instruction count N: A uses N × 2/(4 × 10^9) = N × 0.5 ns. B uses N × 0.5/(2 × 10^9) = N × 0.25 ns. B is twice as fast. CPI = 0.5 is an average completion-rate measure enabled by overlapping work, not half a physical clock tick for each instruction's latency.

**4. Why does our ideal pipeline improve throughput while leaving latency unchanged, and why might real latency differ?**

Our model overlaps independent stages while keeping three cycles per instruction and the same cycle duration. More instructions finish per unit time; real pipeline overhead, dependencies or a changed clock can alter latency and the total gain.

**5. What does Example 1 omit about effective-address calculation in a real load?**

It omits effective-address calculation because the complete absolute address is provided. A real load can add a base register and offset using an ALU or an address-generation unit before accessing memory.

## H09-02

Lesson: [Common misconceptions](09%20Practice%20and%20Summary/02-common-misconceptions.md).

**1. Why does the CPU not understand variables?**

A native instruction uses encoded operands such as register identifiers and addresses. The language implementation connects source variable names to runtime representations and can optimise their storage; the CPU does not interpret the source name itself.

**2. Why is higher GHz not always faster?**

A program can need a different dynamic instruction count and average CPI on each system. Clock period is only one factor in CPU time, so a higher frequency alone cannot establish lower runtime.

**3. Does more RAM make the CPU faster? Why or why not?**

Extra RAM can avoid paging or support a larger resident working set, improving some workloads. It does not automatically raise clock speed or make a CPU-bound instruction stream execute faster.

**4. What does pipelining primarily improve? What happens to latency in our ideal model and potentially in real hardware?**

Pipelining primarily improves throughput. Our equal-clock ideal model leaves instruction latency unchanged; real pipeline overhead and clock changes can alter it.

**5. What is the difference between latency and bandwidth?**

Latency is a specified time delay. Bandwidth means capacity per second in this lesson; achieved throughput can be lower. A long-delay path can still have high capacity.

**6. Which misconception have you held yourself? How would you correct it now?**

Illustrative reflection: I used to assume a 4 GHz system was always faster. I would now compare a representative task's execution time and inspect instruction count/CPI instead of using clock rate alone. Any honest reflection with a corrected explanation is acceptable.

## H09-03

Lesson: [Summary map: how it all fits together](09%20Practice%20and%20Summary/03-summary-map.md).

**1. Name the nine topics in order.**

The sections are: hardware groups; inside the CPU; fetch/decode/execute; memory hierarchy; how programs run; performance; pipelining; hardware/AI/networks; practice and summary. The sequence moves from components to execution and evaluation.

**2. Which topic explains why GHz is not the whole story?**

Section 06 Performance. It relates clock period to frequency and combines dynamic instruction count, average CPI and period into CPU execution time.

**3. Which topic explains the difference between registers and RAM?**

Section 04 Memory Hierarchy, especially Registers and cache and RAM. Section 02 also introduces register operands and the ALU.

**4. Which topic connects hardware to AI and networks?**

Section 08 Hardware and AI Networks. It connects parallel computation and memory costs to AI workloads and NIC/network costs to distributed work.

**5. In your own words: what is the one thread that ties all nine topics together?**

Illustrative response: instructions, data storage, execution units and communication paths cooperate to carry out a computation. Timing depends on the software workload, data movement and hardware, rather than one magic component. Other well-supported summaries are valid.

## H09-04

Lesson: [Check yourself: final questions](09%20Practice%20and%20Summary/04-check-yourself.md).

**1. Which questions did you answer without hesitation?**

Illustrative reflection: I could explain PC versus IR and solve the clock-period question without notes. Name the actual questions you answered confidently; the sample is not a claim about your performance.

**2. Which ones needed the files? Those are your review topics.**

Illustrative reflection: I needed the memory lesson to distinguish a cache miss from a RAM access, so I will reread it and attempt the question again. Choose review topics from your own errors.

**3. Can you explain each answer to a friend in one minute?**

Illustrative expected outcome: give a short explanation, a concrete example and its key assumption for each answer. If you cannot do so, the answer key can guide practice; simply repeating a memorised sentence is not the goal.

**4. If not, which file will you reread first?**

Illustrative reflection: I will reread Instruction count and CPI because I confused completion rate with an instruction's latency, then redo the CPI = 0.5 comparison. A useful response names a lesson and a specific misunderstanding.

## Final self-test

All 18 main questions from [Check yourself: final questions](09%20Practice%20and%20Summary/04-check-yourself.md), in the original order.

**1. Name the hardware groups used in this project and one job for each.**

CPU executes instructions; RAM supplies working capacity; persistent storage retains saved files; I/O exchanges information with users/devices. Networking is an I/O use through a NIC, highlighted separately for this project.

**2. Why is software "the recipe" and hardware "the kitchen"?**

The recipe specifies operations, while the kitchen is the physical equipment performing them. The analogy distinguishes software from hardware but does not explain electrical timing or parallel execution.

**3. What is the difference between PC and IR?**

PC identifies an instruction address. In our teaching cycle it advances during fetch; IR keeps the fetched instruction during decode/execute. These are different from the address or value of data used by that instruction.

**4. What does the control unit do, and what does the ALU do?**

Control logic determines operations, operands, destinations and timing signals. The ALU performs selected arithmetic/logical operations on program values. Other execution units can perform specialised work.

**5. List the five steps of fetch.**

PC supplies the fetch address; CPU sends it to memory; instruction bits return; IR retains them; PC advances by four in this teaching model. Those steps do not execute the instruction's data operation yet.

**6. Trace `ADD R1, R2` with R1 = 6, R2 = 4, instruction at `0x100`. Final values and PC?**

Fetch at 0x100 makes PC = 0x104. ADD R1, R2 computes 6 + 4 and writes R1. Final: R1 = 10, R2 = 4, PC = 0x104. This assumes a four-byte straight-line teaching instruction.

**7. Order registers, cache, RAM, and disk from fastest to slowest.**

Typical access-latency order: registers, cache, RAM, then SSD/disk. Technologies and access paths explain the trade-off; physical distance alone is not a universal speed law.

**8. What is the difference between a cache hit and a cache miss?**

At a given cache level, a hit finds the requested memory block; a miss does not. A miss may be served by a later cache, so not every L1 miss causes a RAM access.

**9. What does the compiler do?**

A compiler translates code into another representation. Native toolchains can produce CPU machine code; CPython commonly uses bytecode and an interpreter, and Java commonly uses JVM bytecode with interpretation or runtime compilation.

**10. Why does the CPU not understand variables?**

Source names are language-level abstractions. Machine instructions use encoded registers, addresses, constants and operations; runtimes/compilers connect these mechanisms to source program values.

**11. Write the execution time formula.**

CPU time = dynamic instruction count × average CPI × clock period = instruction count × CPI / frequency. The examples assume a constant clock; I/O and scheduling waits can add elapsed time outside CPU execution.

**12. Program: 2,000,000 instructions, CPI = 2, clock = 2 GHz. Execution time?**

2,000,000 instructions × 2 cycles/instruction = 4,000,000 cycles. Divide by 2 × 10^9 cycles/s: 0.002 s = 2 ms.

**13. What happens to latency in our ideal pipeline, what may happen in real hardware, and what does pipelining primarily increase?**

Our ideal three-stage equal-clock model keeps each instruction at three cycles latency. Real pipeline overhead and clock changes can alter latency. The primary benefit is higher throughput: more completions per time interval.

**14. Why does a pipeline make the program faster overall?**

It overlaps stages from different instructions so hardware can do useful work concurrently. For independent instructions with no stalls, the line finishes one per cycle after filling; hazards and overhead limit the real gain.

**15. Why do AI workloads use GPUs?**

Large parallel matrix workloads in some neural networks can use GPU throughput effectively. Not all AI requires a GPU: small tabular Q-learning can run on a CPU, and transfers or control-heavy work can make CPU execution preferable.

**16. What is the difference between latency and bandwidth?**

Latency is an identified one-way or round-trip delay. Bandwidth here is capacity per second; throughput is the achieved rate. Capacity and delay describe different properties of the path.

**17. Name the one thread that ties all nine topics together.**

Illustrative summary: physical storage, execution and communication cooperate to run instructions, with performance determined by both the workload/software and the hardware/data paths. A different explanation is acceptable if it connects the topics accurately.

**18. Which topic do you need to review most? Why?**

Illustrative reflection: I need to review pipelining because I added individual instruction latencies instead of counting overlapping cycles. Name your own weakest topic, why it is difficult, and one next practice step.

## H00

Lesson: [Hardware — How Computers Actually Work (Introduction)](INTRODUCTION.md).

**1. In your own words: what is hardware, and why does software need it?**

Hardware is the physical equipment that stores, moves and processes encoded instructions and data. Software describes operations, but it needs an executing physical system to produce a result.

**2. Name the hardware groups used in this project and one job for each.**

Our groups are CPU (execute instructions), RAM (working storage), persistent storage (retain saved files) and I/O (exchange data with the outside world). Networking is a highlighted I/O use, not an extra compulsory component of every computer.

**3. Describe in 2–3 sentences what happens when a program runs.**

A language implementation translates or interprets the source. Machine instructions and active data are made available through working memory; the CPU fetches, decodes and executes instructions, moving values through registers, caches and memory as needed.

**4. Which file would you read to learn why 4 GHz is not always faster than 3 GHz?**

Read section 06 Performance, starting with Why more GHz is not the same as faster. It introduces dynamic instruction count, average CPI and clock period, then calculates CPU time from their product.
