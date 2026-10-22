# Networks — A Micro-Textbook for Beginners

This is the first draft of our Networks content. It lives in the repo as `/content/Networks/INTRODUCTION.md` and will become the foundation for the Study Guide, slides, videos, and test bank.

---

## Learning Objectives

After this section, a beginner should be able to:
1. Explain what happens between typing a URL and seeing a page load.
2. Name the main layers of the network stack and what each one is responsible for.
3. Describe how data is split into packets and reassembled at the destination.
4. Explain the roles of IP and TCP, and why we need both.
5. Describe at a high level how DNS and routing deliver a request to the right machine.

---

## 1. What a Network Actually Does

A network is a system that moves **data** from one machine to another. That sounds simple, but the hard part is doing it reliably: machines are far apart, links fail, packets get lost or arrive out of order, and many programs use the network at the same time.

The core idea is **layering**. Instead of one giant problem, the network is split into layers, each solving one piece and handing the result to the next. This is why you can change Wi-Fi without rewriting your browser.

---

## 2. The Layers (in Plain Terms)

| Layer | What it does | Example |
|---|---|---|
| **Application** | The program's own protocol | HTTP, DNS, SSH |
| **Transport** | Delivers data to the right program, in order | TCP, UDP |
| **Network** | Moves packets between machines across networks | IP |
| **Link** | Moves frames between directly connected devices | Ethernet, Wi-Fi |
| **Physical** | Sends bits over a wire or radio | cables, radio signals |

Think of it like mail: the application writes the letter, transport puts it in an envelope with a port number, network writes the address, link hands it to the local post office, physical is the truck.

---

## 3. Packets: Splitting and Reassembling

Large data is not sent as one piece. It is split into **packets**, each with a header containing source, destination, and sequence information. Packets may travel different routes and arrive out of order. The receiver uses the headers to **reassemble** the original data.

Why packets? Because links have size limits, and splitting allows many messages to share the same link and lets the network recover from loss by resending only small pieces.

---

## 4. IP and TCP: Two Different Jobs

These two are often confused, but they do different things.

**IP (Internet Protocol)** is the addressing and routing layer. It gets a packet from one machine to another, possibly across many networks. IP is **best-effort**: it does not guarantee delivery, order, or that packets arrive at all.

**TCP (Transmission Control Protocol)** sits on top of IP and adds reliability: it numbers the data, acknowledges what arrived, retransmits what was lost, and reorders packets so the application sees a clean stream. TCP also handles **ports**, so the operating system knows which program should receive the data.

**UDP** is the alternative to TCP: no guarantees, no retransmission, less overhead. It is used when speed matters more than perfect delivery, like live video.

**Why both IP and TCP?** IP solves "get it to the right machine." TCP solves "make it arrive correctly and in order." Keeping them separate means IP can route anything, and TCP only worries about reliability.

---

## 5. DNS and Routing: Finding the Right Machine

**DNS (Domain Name System)** turns a human-readable name like `example.com` into an IP address. It is itself a distributed system: your machine asks a resolver, the resolver asks root and authoritative servers, and the answer is cached so the next lookup is fast.

**Routing** is how packets find their way across the internet. Routers hold tables mapping destination networks to the next hop. Each router only needs to know the next step, not the whole path — like asking for directions one intersection at a time.

**Worked example — loading a page:**
1. Browser asks DNS for the IP of `example.com`.
2. DNS returns an IP address.
3. Browser opens a TCP connection to that IP on port 443 (HTTPS).
4. TCP performs a handshake to agree on the connection.
5. Browser sends an HTTP request over the connection.
6. The server responds; TCP ensures the response arrives complete and in order.
7. Browser renders the page.

---

## 6. Worked Example: Tracing a Request

Suppose you open `http://example.com`.

- **Application:** HTTP GET request for `/`.
- **Transport:** TCP segments the request, assigns a source port, tracks sequence numbers.
- **Network:** each segment becomes an IP packet with source and destination IP addresses.
- **Link:** each packet becomes a frame for the local network (e.g., Ethernet or Wi-Fi).
- **Physical:** bits travel over the medium.
- At the destination, the process reverses: frames → packets → segments → HTTP request.

If a packet is lost, TCP notices the missing acknowledgment, retransmits, and the receiver reorders — the application never sees the gap.

---

## 7. Common Misconceptions

- **"IP and TCP are the same thing."** IP routes packets between machines; TCP makes delivery reliable and ordered.
- **"Data travels as one big stream."** It is split into packets that may take different routes.
- **"DNS is just a lookup table."** It is a distributed, cached system with multiple levels of servers.
- **"The internet is a single network."** It is a network of networks, connected by routers that forward packets hop by hop.
- **"UDP is broken TCP."** UDP is a deliberate trade-off: no guarantees, but less overhead, useful for real-time data.

---

## 8. Check Yourself

1. **Order the layers** from application to physical and give one example protocol for each.
2. **Explain** why a large file is split into packets instead of sent as one piece.
3. **Compare** IP and TCP: what does each guarantee, and what does each leave to the other?
4. **Trace** what happens when you type `example.com` into a browser: name the DNS step, the TCP step, and the HTTP step.
5. **Spot the error:** "TCP is faster than UDP because it is more reliable." What is wrong with this claim?

*Answers are in the test bank (separate file); the study guide(soon) will include short explanations.*

---

## 9. Scope Boundaries

- **Detailed:** layering, packets, IP vs. TCP, DNS and routing basics, the end-to-end request trace.
- **Brief:** UDP, HTTP vs. HTTPS, caching in DNS.
- **Out of scope:** congestion-control algorithms, TLS handshake details, BGP internals, IPv6 addressing details, socket programming.

---

## 10. References (to complete and verify)

- Course materials for the Networks module (insert lecture/slide numbers).
- Kurose & Ross, *Computer Networking: A Top-Down Approach* — chapters on the application, transport, and network layers (insert edition/pages).
