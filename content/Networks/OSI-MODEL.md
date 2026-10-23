# The OSI Model & Network Stacks — A Micro-Textbook for Beginners

This is the first draft of our OSI Model content. It lives in the repo as `/content/Networks/OSI-MODEL.md` and provides the structural roadmap for how computer systems conceptualize network communication.

---

## Learning Objectives

After this section, a beginner should be able to:
1. Explain the purpose of the 7-layer OSI model and why layered abstraction matters.
2. Name and sequence all 7 layers of the OSI model from top to bottom.
3. Contrast the theoretical 7-layer OSI model with the practical 4-layer TCP/IP stack.
4. Describe how encapsulation and decapsulation work as data moves down and up the stack.

---

## 1. Why Do We Need a Model?

When computer networking was in its infancy, different hardware vendors built proprietary networks that couldn't talk to each other. To fix this, standardization bodies created conceptual frameworks to break network communication down into modular layers. 

The most famous framework is the **OSI (Open Systems Interconnection) Model**, consisting of **7 distinct layers**. While modern internet traffic runs primarily on the simpler 4-layer TCP/IP suite, the OSI model remains the universal language engineers use to troubleshoot and describe where network operations occur.

---

## 2. The 7 Layers of the OSI Model

A popular mnemonic to remember the layers from top to bottom (Layer 7 down to Layer 1) is **"Please Do Not Throw Sausage Pizza Away"**.

| Layer | Name | What it does | Common Protocols / Examples |
|---|---|---|---|
| **7** | **Application** | Directly serves user programs and UI | HTTP, FTP, DNS, SMTP |
| **6** | **Presentation** | Translates, encrypts, and compresses data | TLS/SSL, JPEG, ASCII |
| **5** | **Session** | Manages sessions and dialogue control | NetBIOS, RPC |
| **4** | **Transport** | End-to-end delivery, reliability, and ports | TCP, UDP |
| **3** | **Network** | Routing packets across multiple networks | IP, ICMP, Routers |
| **2** | **Data Link** | Node-to-node framing and physical addressing | Ethernet, Wi-Fi (MAC addresses) |
| **1** | **Physical** | Raw bit transmission over hardware medium | Cables, fiber optics, radio waves |

---

## 3. OSI vs. Practical TCP/IP Stack

While the OSI model has 7 layers, the actual internet operates on a compressed **4-layer TCP/IP model**:

1. **Application Layer** (Combines OSI Layers 5, 6, and 7)
2. **Transport Layer** (Corresponds to OSI Layer 4)
3. **Internet / Network Layer** (Corresponds to OSI Layer 3)
4. **Link / Network Access Layer** (Combines OSI Layers 1 and 2)

---

## 4. Encapsulation: Adding Envelopes Inside Envelopes

As data travels **down** the stack from your browser to the physical wires, each layer wraps the data with its own control header. This process is called **encapsulation**.

1. **Application data** is generated.
2. **Transport layer** adds a header (creating a *segment* or *datagram*).
3. **Network layer** adds an IP header (creating a *packet*).
4. **Data Link layer** adds a MAC header and trailer (creating a *frame*).
5. **Physical layer** turns it into electrical/light/radio bits.

At the destination, the process reverses (**decapsulation**): each layer strips off its corresponding header until only the clean application data remains.

---

## 5. Common Misconceptions

- **"Every real-world network strictly uses all 7 OSI layers."** No, the 7-layer model is a conceptual reference tool; the real internet runs on the 4-layer TCP/IP model.
- **"Routers operate at the application layer."** Routers operate primarily at Layer 3 (Network) inspecting IP headers, whereas firewalls or proxies can operate higher up.

---

## 6. Check Yourself

1. **List** the 7 layers of the OSI model in order from top to bottom.
2. **Compare** the 7-layer OSI model with the 4-layer TCP/IP stack—what changed?
3. **Explain encapsulation:** What happens to data as it moves down from the Application layer to the Physical layer?

---

## 7. Scope Boundaries

- **Detailed:** The 7 layers, encapsulation/decapsulation, mapping to TCP/IP.
- **Brief:** Session and presentation layer specifics.
- **Out of scope:** Deep historical standards committee specifications, proprietary OSI protocol suite implementations (X.25).