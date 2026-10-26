# Networks — Explained Answer Key

**Status:** Revised with AI-assisted technical checks; awaiting team peer review.

[Module outline](OUTLINE.md)

These explanations cover all **30 questions** in the nine learner chapters. Question numbers match each chapter's Check Yourself section. Equivalent accurate explanations are acceptable. Sources for the concepts are linked in the corresponding chapters; these answers are not a claim of completed human peer review or an official marking rubric.

## Introduction

[Questions and worked trace](INTRODUCTION.md#8-check-yourself)

1. **Five-layer order.** Application → Transport → Network → Link → Physical. Suitable examples are HTTP, TCP, IP, Ethernet link framing, and optical signals in fiber. A physical medium is not itself an application protocol. This model separates Physical from the network-access layer used in the four-layer TCP/IP description.
2. **Why many packets?** Links limit the size of individual transmissions, and packet-sized pieces let multiple conversations share capacity. A large file therefore normally uses many packets. Recovery belongs to the relevant protocol: TCP can retransmit missing data; IP alone does not promise this service.
3. **IP versus TCP.** IP addresses and forwards packets on a best-effort basis. TCP, carried over IP, supplies an ordered byte stream using sequence tracking, acknowledgments, and recovery. TCP can report a failed connection if the network or peer does not recover, so reliable service does not guarantee every transfer will finish.
4. **HTTPS trace.** DNS supplies an address for the hostname. The host chooses a route; in the example, a remote destination uses its default gateway. IP packets travel through successive links and routers. TCP establishes the connection, then TLS validates the server identity and establishes protection. The browser exchanges HTTP requests/responses inside TLS and renders the returned content. Omitting TLS would omit the protection that makes this example HTTPS.
5. **Speed claim.** Reliability does not establish that TCP is faster. It also does not prove that UDP is always faster. Completion time and delay depend on conditions and requirements, including any recovery or other mechanisms supplied by an application above UDP.

## OSI Model

[Questions](OSI-MODEL.md#6-check-yourself)

1. **Top-to-bottom order.** Application, Presentation, Session, Transport, Network, Data Link, Physical. “Please Do Not Throw Sausage Pizza Away” gives the reverse direction, Physical to Application. The direction must be stated when using the mnemonic.
2. **Model comparison.** The common TCP/IP Application layer broadly groups OSI Layers 5–7; Transport corresponds broadly to 4; Internet to 3; Network Access includes 1–2. The introduction splits that last group into Link and Physical, producing five teaching layers. These groupings organize functions rather than requiring a fixed number of software components.
3. **Encapsulation.** In the example, TCP adds its header to application data, IPv4 carries the segment in an IP packet, and Ethernet carries the packet in a frame with link control information. Physical transmission encodes that frame as signals. The receiver processes the corresponding framing/headers upward. A router replaces link framing as it forwards the IP packet to another link.

## Network Types

[Questions](LAN-WAN-PAN.md#5-check-yourself)

1. **PAN versus LAN.** A PAN connects devices around one person, such as a phone and headphones. A LAN serves a local setting such as an office or campus. These labels describe typical scope; they are not fixed meter limits or interchangeable names for Bluetooth and Wi-Fi.
2. **LAN-to-WAN device.** A router forwards packets between IP networks, including from a LAN toward a provider's wider network. An access point supplies local wireless access. A home Wi-Fi router can contain both functions, which explains why the devices are often confused.
3. **Coverage versus WAN service.** Covering every room describes local Wi-Fi coverage. It does not establish the speed, reliability, or availability of the Internet/WAN connection. A device could communicate with a local printer while the external service is down.

## IP and Routing

[Questions](ROUTING-AND-IP.md#6-check-yourself)

1. **IPv4 and IPv6.** IPv4 uses 32-bit addresses, normally written as four decimal numbers. IPv6 uses 128-bit addresses and hexadecimal notation. IPv4's limited supply motivated the much larger space. Exhaustion of original unallocated pools does not mean previously assigned IPv4 addresses stopped working.
2. **Mask and local destination.** `/24` means the first 24 bits are the prefix; for this example, that is `192.168.1.0/24`. `192.168.1.80` shares it; `192.168.2.20` does not. The first is on the example's local subnet, while reaching the second needs an appropriate route. This answer assumes the normally configured LAN specified in the chapter.
3. **Default gateway.** If no more specific route matches, the host sends the packet to the next-hop router specified by its default route. The local frame targets that gateway while IP identifies the remote destination. The router then makes its own forwarding decision. Distance or country alone does not determine whether the default route is used.

## TCP and UDP

[Questions](TCP-AND-UDP.md#7-check-yourself)

1. **Handshake.** In the usual TCP setup, the client sends SYN, the server replies SYN-ACK, and the client acknowledges with ACK. This establishes connection state, including initial sequence information. It is not a TLS handshake and does not itself encrypt the application data.
2. **Game updates.** A position update that arrives after newer updates may no longer help. UDP lets the application choose whether to wait, recover, or continue. Reliable handling may still be needed for account changes or purchases. That reliability can use TCP or another suitable protocol; choosing UDP for one message type does not remove every application's need for recovery.
3. **Ports.** Ports identify transport endpoints within an addressed host. A client source port and server destination port help distinguish one communication from others. The complete connection context also includes addresses and the transport protocol. Routers normally forward by IP routes without deciding which browser tab or application owns the data.
4. **Loss and failure.** TCP can detect missing data and retransmit it, then provide bytes in order. A single lost packet therefore does not inherently crash an application. If recovery ultimately fails, the connection can abort or time out; the application must handle that outcome. TCP cannot restore a permanently unavailable peer.

## DNS

[Questions](DNS.md#6-check-yourself)

1. **Uncached lookup.** The recursive resolver works on the client's behalf. A root server directs it toward the TLD; a TLD server supplies the next delegation; an authoritative server answers from the relevant zone's records. The resolver returns the result. Cached answers or delegations can skip stages, so the full chain is not repeated for every lookup.
2. **A versus CNAME.** An A record supplies an IPv4 address. A CNAME identifies another DNS name as the canonical target of an alias. Resolving that target may require another lookup. A CNAME is therefore not simply a differently formatted IP address.
3. **TTL and changing answers.** TTL limits how long cached data can normally be reused. One resolver may still hold an unexpired old address, while another obtains the new authoritative value. Those clients can briefly receive different results. A change is not pushed instantly to all independent caches.

## DHCP

[Questions](DHCP.md#6-check-yourself)

1. **DORA.** In a typical new DHCPv4 allocation, Discover finds servers, Offer proposes configuration, Request selects an offer, and ACK confirms the lease and configuration. Discover and the selecting Request are broadcast in this example; it does not follow that every later DHCP message must also be broadcast.
2. **Other settings.** A subnet mask identifies the IPv4 prefix; a default gateway supplies a router for the default route; DNS server addresses tell the client where to ask name questions. Lease duration is another valid answer: it limits how long the assignment remains valid without renewal. DHCP provides configuration; the client then uses the corresponding services.
3. **Lease and reservation.** If renewal does not succeed before expiry, the client must stop using the expired address. A DHCP reservation associates a client with an address that the server consistently assigns through DHCP. A manually configured static address is entered on the device instead. A renewed lease can retain the same address, so “dynamic” does not mean “different on every connection”.

## HTTP and Security

[Questions](HTTP-AND-SECURITY.md#6-check-yourself)

1. **GET versus POST.** A GET requests a representation, such as an HTML page. A POST submits data for a resource to process, such as a form. POST does not itself encrypt data; HTTPS protection is separate from the HTTP method.
2. **404.** It means that the responding HTTP server did not find a current representation of the target resource or will not disclose one. It does not prove permanent nonexistence. The response comes from an HTTP-serving component, which can be an origin server or an intermediary acting as a server; it is not a DNS error code.
3. **HTTPS.** With successful validation, TLS protects the contents of HTTP communication, authenticates the server for the requested name, and detects tampering with protected data. Plain HTTP lacks this transport protection. HTTPS does not establish that the site's content is honest, hide all connection metadata, or prevent an attacker from disrupting connectivity.

## SSH

[Questions](SSH.md#6-check-yourself)

1. **Connection sequence.** The client contacts the server, normally on TCP port 22. The endpoints negotiate protection and perform key exchange; the client verifies the server's host identity. The server then authenticates the user for the requested account. If permitted, it starts the requested shell or command over the protected connection.
2. **Public and private keys.** The public key is registered for the account on the server; the private key remains protected under the user's control. The client proves possession through a signature. The server verifies that signature with the public key; it does not need to receive the private key.
3. **Host-key verification.** An encrypted connection is useful only if it reaches the intended server. Comparing the fingerprint with a trusted value helps detect an unexpected identity. An unfamiliar or changed key should be investigated: legitimate replacement is possible, but automatically accepting it would skip the identity check.
