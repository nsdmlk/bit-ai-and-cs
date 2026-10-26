# The OSI Model and Network Stacks — A Micro-Textbook for Beginners

This chapter uses models to organize networking responsibilities and explain encapsulation.

**Status:** Revised with AI-assisted technical checks; awaiting team peer review.

[Module outline and reading order](OUTLINE.md) · [Explained answers](ANSWER-KEY.md)

---

## Learning Objectives

After this section, a beginner should be able to:

1. Explain why layered models are useful.
2. Name the seven OSI layers in order.
3. Relate OSI to four-layer TCP/IP and five-layer teaching models.
4. Describe encapsulation and decapsulation in a simple Internet example.

## 1. Why Do We Need a Model?

The **OSI (Open Systems Interconnection) model** separates communication into seven layers. It is a reference framework for describing responsibilities, not a rule that every real implementation must contain seven separate software components. [ITU-T X.200, Basic Reference Model](https://www.itu.int/rec/T-REC-X.200-199407-I/en)

Layering helps isolate problems. A damaged cable and an incorrect HTTP request belong to different parts of the communication process.

## 2. The Seven Layers

**“Please Do Not Throw Sausage Pizza Away” runs from bottom to top: Layer 1 to Layer 7.** Read the table downward for the opposite order, Application to Physical.

| Layer | Name | Main responsibility | Illustrative examples |
|---|---|---|---|
| **7** | **Application** | Network services used by application processes | HTTP, DNS, SMTP |
| **6** | **Presentation** | Representation, encoding, and transformation of data | Text encodings, image formats |
| **5** | **Session** | Organizing and coordinating a dialogue | Session establishment and control |
| **4** | **Transport** | End-to-end transport; reliability and ordering depend on the protocol | TCP, UDP |
| **3** | **Network** | Addressing and forwarding between networks | IP, router forwarding |
| **2** | **Data Link** | Framing and delivery over a local link | Ethernet/Wi-Fi link functions |
| **1** | **Physical** | Encoding and transmitting bits as signals | Copper, fiber, radio |

These Internet examples are **approximate functional mappings** onto the OSI reference model. For example, Internet applications often implement functions associated with OSI's upper three layers together. TLS provides security between application protocols and their transport; assigning it one universal OSI layer would be misleading.

## 3. OSI, TCP/IP, and the Five-Layer Teaching Model

A common **four-layer TCP/IP model** groups functions as follows:

1. **Application:** broadly covers OSI's Application, Presentation, and Session functions.
2. **Transport:** corresponds broadly to OSI Layer 4.
3. **Internet:** corresponds broadly to OSI Layer 3.
4. **Link / Network Access:** includes link and physical transmission functions.

The [Introduction](INTRODUCTION.md) uses **five layers** by separating Physical from Link. The layer count is a modelling choice, not a claim about different Internets. Strict layering is itself an imperfect description of implementations. [RFC 1122 §§1.1.3 and 1.3.1](https://www.rfc-editor.org/rfc/rfc1122.html#section-1.1.3)

## 4. Encapsulation: Adding Control Information

Consider application data sent with TCP over IPv4 and Ethernet:

1. **Application:** produces data for its protocol.
2. **TCP:** adds a TCP header, forming a **segment**.
3. **IPv4:** adds an IP header, forming an **IP packet**.
4. **Ethernet:** carries the packet in a **frame** with link control information, including a header and trailer.
5. **Physical transmission:** encodes the frame as signals on the medium.

This wrapping is **encapsulation**. The physical step transmits signals; it is not simply another protocol header. At the receiving endpoint, **decapsulation** processes the corresponding framing and headers to deliver the data upward. [TCP segmentation: RFC 9293 §2.2](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2), [Ethernet/IP encapsulation: RFC 1122 §2.3.3](https://www.rfc-editor.org/rfc/rfc1122.html#section-2.3.3)

A router removes incoming link framing, examines the IP packet, and uses suitable new framing on the next link. It does not normally reconstruct the application's entire message merely to forward a packet.

## 5. Common Misconceptions

- **“Every network strictly implements all seven OSI layers.”** OSI is a reference model; real protocol suites group responsibilities differently.
- **“Four-layer and five-layer descriptions contradict each other.”** The five-layer teaching model separates physical transmission from the four-layer model's network-access layer.
- **“Routers forward packets by interpreting webpage content.”** Ordinary IP forwarding primarily uses network-layer information, especially the destination address and routing table.

## 6. Check Yourself

1. **List** the seven OSI layers from top to bottom.
2. **Compare** OSI with the four-layer TCP/IP model, and explain the introduction's fifth layer.
3. **Explain encapsulation:** what happens in the TCP/IPv4/Ethernet example from application data to physical signals?

[Explained answers: OSI Q1–Q3](ANSWER-KEY.md#osi-model)

## 7. Scope Boundaries

- **Detailed:** Layer order, model mappings, encapsulation and decapsulation.
- **Brief:** Presentation/session responsibilities and router link-framing changes.
- **Out of scope:** OSI protocol-suite history, detailed Ethernet frame fields, strict classification of every Internet protocol into an OSI layer.
