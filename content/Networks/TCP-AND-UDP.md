# Transport Layer: TCP and UDP — A Micro-Textbook for Beginners

This chapter compares two transport services and explains ports without assuming one protocol is always faster.

**Status:** Revised with AI-assisted technical checks; awaiting team peer review.

[Module outline and reading order](OUTLINE.md) · [Explained answers](ANSWER-KEY.md)

---

## Learning Objectives

After this section, a beginner should be able to:

1. Distinguish connection-oriented and connectionless transport.
2. Explain TCP's ordering and loss recovery, including their limits.
3. Describe UDP's minimal service and why an application may choose it.
4. Explain ports and application endpoints.
5. Relate transport choices to an application's delivery requirements.

## 1. The Transport Layer's Role

IP forwards packets to destination addresses. **Transport protocols** provide communication between application endpoints. TCP and UDP use **ports** as part of that addressing: for example, a service may listen on port 443 while clients use temporary source ports.

TCP and UDP also provide different delivery behavior. This choice affects what an application must do when data is missing, duplicated, or out of order.

## 2. TCP: An Ordered Byte Stream

**TCP (Transmission Control Protocol)** provides a reliable, ordered byte stream. It does not preserve the boundaries of an application's individual messages; the application protocol must identify those boundaries when needed. [RFC 9293 §2.2](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2)

Its main mechanisms include:

- **Connection setup:** The usual three-way handshake is SYN → SYN-ACK → ACK.
- **Sequence numbers:** TCP tracks positions in the byte stream so received data can be ordered.
- **Acknowledgments and retransmission:** Acknowledgments report received data. TCP retransmits when it detects loss, for example after a retransmission timeout.
- **Flow control:** A receiver advertises how much data it can accept, helping prevent a sender from overwhelming it.
- **Congestion control:** The sender adapts to network conditions; detailed algorithms are outside this chapter.

Reliability is not a promise that every transfer finishes. If a peer or path remains unavailable, the connection can fail and the application must handle an error or timeout. [RFC 5482 §1](https://www.rfc-editor.org/rfc/rfc5482.html#section-1)

## 3. UDP: Individual Datagrams

**UDP (User Datagram Protocol)** carries separate messages called **datagrams**. Its header is **8 bytes**, containing source and destination ports, length, and checksum. It has no built-in connection handshake, retransmission, or ordering mechanism. [RFC 768, header format](https://www.rfc-editor.org/rfc/rfc768.html)

The small set of mechanisms lets an application choose its own behavior. A time-sensitive position update in a game may become useless after newer updates arrive. Other messages, such as a purchase confirmation, still need reliable handling.

Retransmission is not always useless in real-time media: it can help when the application's delay budget allows it. The important question is whether recovered data can still arrive in time. [RFC 4588 §3](https://www.rfc-editor.org/rfc/rfc4588.html#section-3)

UDP itself lacks congestion control and recovery, but applications or protocols built above it may supply them. “UDP” therefore does not mean an entire application has no reliability. [RFC 8085](https://datatracker.ietf.org/doc/html/rfc8085)

## 4. Ports: Addressing Application Endpoints

Ports resemble apartment numbers within a building, while an IP address helps identify the building. The analogy is approximate: connection identification also uses addresses, transport protocol, and the ports at both ends.

- **Standard service ports:** Common defaults include HTTP on 80, HTTPS on 443, and DNS on 53. Ports 0–1023 form the system/well-known range; services can be configured differently.
- **Temporary client ports:** The operating system commonly chooses an available source port when an application opens communication.

For the [HTTPS example](INTRODUCTION.md#6-worked-example-a-new-https-connection), a client might connect from temporary port `49152` to server port `443`. Replies use the corresponding endpoint information to reach the correct connection.

## 5. Comparison

| Feature | TCP | UDP |
|---|---|---|
| **Service** | Byte stream | Individual datagrams |
| **Ordering/recovery** | Built in; connection failure remains possible | Not built in |
| **Connection setup** | Normally a three-way handshake | No UDP handshake |
| **Overhead and timing** | Includes mechanisms for setup, ordering, recovery, and flow/congestion control | Small header; higher layers add mechanisms as needed |
| **Examples** | HTTP/1.1 and HTTP/2, SMTP, many file transfers | Many game/media protocols and traditional DNS queries |

These are examples, not exclusive pairings. **DNS also uses TCP**, and **HTTP/3 uses QUIC over UDP**. QUIC provides reliable streams above UDP. [RFC 7766 §5](https://www.rfc-editor.org/rfc/rfc7766.html#section-5), [RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html), [RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)

## 6. Common Misconceptions

- **“TCP is always slower; UDP is always faster.”** Neither is a universal performance rule. Results depend on requirements, network conditions, and the mechanisms used above the transport.
- **“UDP provides zero overhead.”** It has an 8-byte header; applications may add more.
- **“UDP data is always corrupted.”** Its checksum can detect accidental corruption. IPv4 permits an omitted UDP checksum; a checksum is normally required with IPv6. A checksum does not repair loss. [RFC 768](https://www.rfc-editor.org/rfc/rfc768.html), [RFC 8200 §8.1](https://www.rfc-editor.org/rfc/rfc8200.html#section-8.1)
- **“An IP address alone tells the operating system which application endpoint should receive TCP/UDP data.”** Transport ports also matter. Ordinary router forwarding, however, does not require identifying the application.

## 7. Check Yourself

1. **Describe** the usual TCP three-way handshake.
2. **Explain** why a real-time game might use UDP for frequent position updates. Why might other game messages need reliable handling?
3. **What is a port**, and why is an IP address alone insufficient to identify a TCP/UDP application endpoint?
4. **Spot the error:** “If one packet is lost using TCP, the application crashes because TCP cannot recover.” What can TCP do, and what if recovery ultimately fails?

[Explained answers: TCP and UDP Q1–Q4](ANSWER-KEY.md#tcp-and-udp)

## 8. Scope Boundaries

- **Detailed:** Stream versus datagram service, TCP setup/ordering/recovery, ports, application trade-offs.
- **Brief:** UDP header/checksum, temporary ports, flow/congestion control purpose, DNS/HTTP transport variants.
- **Out of scope:** Congestion-control algorithms, detailed packet-field diagrams, sliding-window mathematics, socket programming.
