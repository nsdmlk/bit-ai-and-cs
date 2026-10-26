# Hardware — outline, reading order and development status

**Status:** Revised on 26 October 2026 with AI-assisted technical checks; awaiting team peer review. This is a revision, not the original 24 October submission.

Start with the [introduction](INTRODUCTION.md). The nine section folders contain 33 lessons. The [answer key](ANSWER-KEY.md) covers all lesson questions and the final self-test. The authoring template is not part of the learner reading order.

## Learners and learning goals

Assume basic computer literacy and the ability to read a simple assignment or loop. No prior processor-architecture knowledge is required. The units and pseudocode conventions needed below are defined here.

After this part, a learner should be able to:

- Identify the CPU, RAM, persistent storage and I/O, explaining why a NIC is an I/O device.
- Trace arithmetic and memory-transfer pseudocode, distinguishing instruction addresses, data addresses and stored values.
- Explain register operands, cache hits/misses and the purpose of working versus persistent memory.
- Explain the difference between native machine code, bytecode and runtime execution at an introductory level.
- Calculate constant-clock CPU time from dynamic instruction count and average CPI, and distinguish it from elapsed waiting time.
- Compare latency and throughput with an explicitly ideal three-stage pipeline.
- Explain when parallel hardware and network communication can help or limit an AI workload.

## Teaching-machine conventions

These conventions define the examples; they do not claim that every real CPU is implemented this way.

- **Byte/address:** a byte contains eight bits. Each byte has an address in our model; a four-byte word occupies four successive byte addresses.
- **Hexadecimal:** `0x` introduces base-16 notation, with digits 0–9 and A–F. Adding four to `0x100` gives `0x104`; `0x10C + 4 = 0x110`.
- **Instructions and data:** example instructions occupy four bytes; the integer data examples also use four-byte words. The address containing an instruction is separate from any data address it reads/writes.
- **PC/IR timing:** PC initially identifies the instruction to fetch. Fetch copies it into IR and advances PC by four. Decode/execute use IR. Branches can redirect PC, but the worked traces contain only sequential flow.
- **Arithmetic notation:** the full form is `ADD Rd, Rs1, Rs2`, meaning `Rd ← Rs1 + Rs2`. The two-operand form `ADD Rd, Rs` is shorthand for `ADD Rd, Rd, Rs`. `SUB Rd, Rs` similarly overwrites Rd with `Rd - Rs`. Both forms are explicitly defined pseudocode, not a claim about a particular real assembler.
- **Memory notation:** `LOAD R1, [0x200]` transfers the word at data address 0x200 into R1; `STORE [0x200], R1` transfers the other way. Absolute addresses omit effective-address arithmetic. Real processors can use an ALU/AGU for base-plus-offset address calculation.
- **Timing units:** Hz means cycles/second, GHz means 10^9 cycles/second, ns means 10^-9 seconds, and ms means 10^-3 seconds. CPU time calculations assume a constant clock. Dynamic instruction count includes repetitions; average CPI is cycles/completed instructions, not individual latency.
- **Ideal pipeline:** three one-cycle stages, unchanged clock period, independent instructions and no stalls or resource conflicts. Under these assumptions, n instructions take `3n` cycles sequentially or `n + 2` cycles when pipelined. Real pipeline timing may differ.

## Section map

| Section | Prerequisites | Main example/activity | Scope | Current status |
| --- | --- | --- | --- | --- |
| 01 Hardware groups | Read the conventions above | Trace a video/recipe analogy to physical components | CPU, working/persistent memory and I/O; networking as I/O | Revised; awaiting team peer review |
| 02 Inside the CPU | Section 01 | Identify PC/IR and trace register/ALU data movement | Simple functional datapath/control/address/data model | Revised; awaiting team peer review |
| 03 Fetch/decode/execute | Section 02 | Trace ADD, LOAD and SUB with explicit initial values | Four-byte straight-line teaching instructions; real address-generation caveat | Revised; awaiting team peer review |
| 04 Memory hierarchy | Sections 01–03 | Explain array reuse and cache misses | Registers, locality, cache levels, RAM and persistent storage | Revised; awaiting team peer review |
| 05 How programs run | Sections 02–04 | Translate and trace a = b + c | Stored-program model, compiler/runtime distinction and pseudocode | Revised; awaiting team peer review |
| 06 Performance | Basic multiplication/division and timing units above | Calculate cycles, periods and CPU times | Dynamic count, average CPI and constant clock; no advanced benchmarking | Revised; awaiting team peer review |
| 07 Pipelining | Sections 03 and 06 | Count an ideal overlap timeline | Throughput/latency, fill/drain; detailed hazards excluded | Revised; awaiting team peer review |
| 08 Hardware, AI and networks | Sections 04 and 06; basic AI/network introductions useful | Choose hardware by workload and explain a distributed-training bottleneck | Conceptual GPU/accelerator/NIC use; no deep optimisation | Revised; awaiting team peer review |
| 09 Practice and summary | Sections 01–08 | Mixed worked examples and an 18-item final self-test | Review/application of the preceding lessons | Revised; awaiting team peer review |

## Every lesson in reading order

Each listed lesson has an objective, worked illustration, independent questions, linked explained answers and identifiable sources. Status applies to the revised text; no human peer approval is claimed.

| Lesson | Main learning objective | Answers | Status |
| --- | --- | --- | --- |
| [Why hardware matters](01%20What%20is%20Hardware/01-why-hardware-matters.md) | explain why a program needs hardware to run, and why knowing hardware helps you understand performance. | [4 explained answers](ANSWER-KEY.md#h01-01) | Revised; awaiting team peer review |
| [The hardware groups used in this project](01%20What%20is%20Hardware/02-five-parts-of-a-computer.md) | name the main hardware groups used in this project and explain what each one does. | [5 explained answers](ANSWER-KEY.md#h01-02) | Revised; awaiting team peer review |
| [The kitchen analogy](01%20What%20is%20Hardware/03-kitchen-analogy.md) | match each part of a computer to a part of a kitchen, and use the analogy to explain how the parts work together. | [5 explained answers](ANSWER-KEY.md#h01-03) | Revised; awaiting team peer review |
| [PC and IR: where the CPU keeps its place](02%20Inside%20the%20CPU/01-pc-and-ir.md) | explain what the Program Counter and the Instruction Register are, and why the CPU needs both. | [4 explained answers](ANSWER-KEY.md#h02-01) | Revised; awaiting team peer review |
| [Registers and the ALU: where values live and where math happens](02%20Inside%20the%20CPU/02-registers-and-alu.md) | explain what registers are, what the ALU does, and why the CPU needs both. | [4 explained answers](ANSWER-KEY.md#h02-02) | Revised; awaiting team peer review |
| [The control unit: the manager of the CPU](02%20Inside%20the%20CPU/03-control-unit.md) | explain what the control unit does and why the CPU needs a "manager". | [4 explained answers](ANSWER-KEY.md#h02-03) | Revised; awaiting team peer review |
| [Buses: the roads between parts](02%20Inside%20the%20CPU/04-buses.md) | explain what a bus is, and the difference between the address bus and the data bus. | [5 explained answers](ANSWER-KEY.md#h02-04) | Revised; awaiting team peer review |
| [Fetch: get the next instruction](03%20Fetch%20Decode%20Execute/01-fetch.md) | describe the steps of the fetch phase and explain what the PC and the two buses do during it. | [5 explained answers](ANSWER-KEY.md#h03-01) | Revised; awaiting team peer review |
| [Decode: figure out what the instruction means](03%20Fetch%20Decode%20Execute/02-decode.md) | explain what the decode phase does and what the control unit works out during it. | [5 explained answers](ANSWER-KEY.md#h03-02) | Revised; awaiting team peer review |
| [Execute: actually do it](03%20Fetch%20Decode%20Execute/03-execute.md) | explain what happens during the execute phase, for both arithmetic and memory instructions. | [5 explained answers](ANSWER-KEY.md#h03-03) | Revised; awaiting team peer review |
| [Repeat and the clock: why the cycle never stops](03%20Fetch%20Decode%20Execute/04-repeat-and-clock.md) | explain why the fetch–decode–execute cycle repeats and what the clock does. | [4 explained answers](ANSWER-KEY.md#h03-04) | Revised; awaiting team peer review |
| [Worked examples: tracing instructions](03%20Fetch%20Decode%20Execute/05-worked-examples.md) | trace a simple instruction through fetch, decode, and execute, and state the final register values and the new PC. | [4 explained answers](ANSWER-KEY.md#h03-05) | Revised; awaiting team peer review |
| [Why memory has layers](04%20Memory%20Hierarchy/01-why-layers.md) | explain why memory is organized in layers and why the CPU cannot use just one kind of memory. | [4 explained answers](ANSWER-KEY.md#h04-01) | Revised; awaiting team peer review |
| [Registers and cache: the fast layers](04%20Memory%20Hierarchy/02-registers-and-cache.md) | explain what registers and cache are, and why they are the fastest memory in the machine. | [5 explained answers](ANSWER-KEY.md#h04-02) | Revised; awaiting team peer review |
| [RAM: the working memory](04%20Memory%20Hierarchy/03-ram.md) | explain what RAM is, what it holds, and how it differs from registers and disk. | [5 explained answers](ANSWER-KEY.md#h04-03) | Revised; awaiting team peer review |
| [Storage: the persistent layer](04%20Memory%20Hierarchy/04-storage.md) | explain what storage is, why it is slower than RAM, and why it is still essential. | [5 explained answers](ANSWER-KEY.md#h04-04) | Revised; awaiting team peer review |
| [The stored-program idea](05%20How%20Program%20Runs/01-stored-program-idea.md) | explain what the stored-program idea is and why code and data can live in the same memory. | [4 explained answers](ANSWER-KEY.md#h05-01) | Revised; awaiting team peer review |
| [The compiler: from code to instructions](05%20How%20Program%20Runs/02-compiler-and-instructions.md) | explain what a compiler does and why the CPU does not understand variables. | [5 explained answers](ANSWER-KEY.md#h05-02) | Revised; awaiting team peer review |
| [Worked example: `a = b + c`](05%20How%20Program%20Runs/03-example-a-equals-b-plus-c.md) | translate a simple line of code into instructions and trace how the values change. | [5 explained answers](ANSWER-KEY.md#h05-03) | Revised; awaiting team peer review |
| [Why "more GHz" is not the same as "faster"](06%20Performance/01-why-ghz-is-not-speed.md) | explain why a higher clock speed does not automatically mean a faster CPU. | [5 explained answers](ANSWER-KEY.md#h06-01) | Revised; awaiting team peer review |
| [Instruction count and CPI](06%20Performance/02-instruction-count-and-cpi.md) | explain what instruction count and CPI are, and why both matter for performance. | [5 explained answers](ANSWER-KEY.md#h06-02) | Revised; awaiting team peer review |
| [Clock period: the length of one cycle](06%20Performance/03-clock-period.md) | explain what clock period is, how it relates to clock frequency, and why it is only one of three performance factors. | [5 explained answers](ANSWER-KEY.md#h06-03) | Revised; awaiting team peer review |
| [Worked calculation: putting it all together](06%20Performance/04-worked-calculation.md) | calculate execution time from instruction count, CPI, and clock frequency, and compare two CPUs. | [5 explained answers](ANSWER-KEY.md#h06-04) | Revised; awaiting team peer review |
| [The problem with doing one thing at a time](07%20Pipelining/01-problem-with-sequence.md) | explain why a CPU that does fetch, then decode, then execute, one instruction at a time, wastes time. | [5 explained answers](ANSWER-KEY.md#h07-01) | Revised; awaiting team peer review |
| [The assembly-line idea](07%20Pipelining/02-assembly-line-idea.md) | explain what pipelining is, using the assembly-line analogy, and why it makes the CPU faster. | [5 explained answers](ANSWER-KEY.md#h07-02) | Revised; awaiting team peer review |
| [Throughput: why the pipeline is faster overall](07%20Pipelining/03-throughput.md) | explain what throughput is, how pipelining increases it, and why latency and throughput are different. | [5 explained answers](ANSWER-KEY.md#h07-03) | Revised; awaiting team peer review |
| [GPU and AI accelerators](08%20Hardware%20and%20AI%20Networks/01-gpu-and-ai-accelerators.md) | explain what a GPU is, why AI workloads use it, and what an AI accelerator is. | [5 explained answers](ANSWER-KEY.md#h08-01) | Revised; awaiting team peer review |
| [Network cards, latency, and bandwidth](08%20Hardware%20and%20AI%20Networks/02-nic-latency-bandwidth.md) | explain what a network card does, and the difference between latency and bandwidth. | [5 explained answers](ANSWER-KEY.md#h08-02) | Revised; awaiting team peer review |
| [Where hardware meets AI and networks](08%20Hardware%20and%20AI%20Networks/03-where-hardware-meets-ai-and-networks.md) | explain how the hardware topics connect to the AI and networks parts of the project. | [5 explained answers](ANSWER-KEY.md#h08-03) | Revised; awaiting team peer review |
| [Worked examples: putting it all together](09%20Practice%20and%20Summary/01-worked-examples.md) | solve mixed problems that combine tracing, memory, performance, and pipelining. | [5 explained answers](ANSWER-KEY.md#h09-01) | Revised; awaiting team peer review |
| [Common misconceptions](09%20Practice%20and%20Summary/02-common-misconceptions.md) | recognize and correct the most common beginner mistakes about hardware. | [6 explained answers](ANSWER-KEY.md#h09-02) | Revised; awaiting team peer review |
| [Summary map: how it all fits together](09%20Practice%20and%20Summary/03-summary-map.md) | describe the whole Hardware part in one page and see how the nine topics connect. | [5 explained answers](ANSWER-KEY.md#h09-03) | Revised; awaiting team peer review |
| [Check yourself: final questions](09%20Practice%20and%20Summary/04-check-yourself.md) | test their understanding of the whole Hardware part and identify what to review. | [4 explained answers](ANSWER-KEY.md#h09-04) | Revised; awaiting team peer review |

## Open checks and boundaries

- A teammate still needs to attempt the activities and review the revised claims, figures and sources. Record actual findings and corrections after that review occurs.
- Verify coverage against the team's actual course materials, especially the required depth of CUDA, assembler and performance. No course lecture numbers or teacher approvals are invented here.
- Visuals and prose must use the same conventions. The final source package must contain the figures it uses and render without dependence on GitHub.
- Detailed pipeline hazards, out-of-order execution, cache replacement policy, machine-instruction encoding and production GPU programming remain outside this beginner part.
- The sources in each lesson support technical concepts; model assumptions and original teaching examples are stated explicitly. General descriptions do not substitute for measured device-performance claims.

## Reusing one connected topic

Use Section 03 as the first connected teaching sequence. In the **Study Guide**, place the model box before the fetch/decode/execute explanation, then use a trace table and the independent ADD/LOAD questions with their explained answers. In **PPT**, show instruction memory, PC, IR, registers and data memory, revealing one transfer at a time. In a **video tutorial**, narrate a fresh ADD trace and pause before the result; then contrast the separate instruction/data addresses of LOAD. These are production plans, not claims that finished media or human-reviewed lessons already exist.

## Source entry points

- [MIT 6.004, Building the Beta](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/): explicitly defined processor model and datapath.
- [MIT 6.004, Caches and the Memory Hierarchy](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c14/c14s1/): memory trade-offs and locality.
- [Cornell CS 3410, Pipelining & Performance](https://www.cs.cornell.edu/courses/cs3410/2026sp/notes/pipelining.html): timing assumptions and pipeline completion rate.
- [NVIDIA CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/): workload assessment and parallel/transfer costs.

Use the narrower lesson source lists for bytecode, I/O, CPI definitions and memory permissions.
