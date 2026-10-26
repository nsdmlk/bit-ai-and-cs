# Networks — Outline and Reading Order

**Status:** Revised with AI-assisted technical checks; awaiting team peer review.

**Audience:** Beginners who can use a browser but have not studied network protocols. The examples are explanatory models, not claims of experiments performed by the team.

**Module outcome:** Explain how a configured device finds a service, routes packets, establishes appropriate transport and protection, and exchanges application data.

## Reading Order and Prerequisites

The introduction is an overview. Later chapters develop its terms; it is normal to revisit its worked example after reading HTTP and Security.

| Order | Chapter | Main learning outcome | Prerequisite | Practice and answer range |
|---|---|---|---|---|
| 1 | [Introduction](INTRODUCTION.md) | Trace a fresh HTTPS-over-TCP exchange through the stack | Basic browser use | Worked HTTPS trace; Introduction Q1–Q5 |
| 2 | [OSI Model](OSI-MODEL.md) | Explain layer order, model grouping, and encapsulation | Introduction's overview | TCP/IP/Ethernet wrapping example; OSI Q1–Q3 |
| 3 | [Network Types](LAN-WAN-PAN.md) | Distinguish network scale and access point/router roles | Introduction | Local printing during an Internet outage; Network Types Q1–Q3 |
| 4 | [IP and Routing](ROUTING-AND-IP.md) | Use a simple prefix and default route to explain forwarding | Network Types; basic layer names | `/24` local/remote comparison; IP and Routing Q1–Q3 |
| 5 | [TCP and UDP](TCP-AND-UDP.md) | Compare transport services and application requirements | IP and Routing | Client/server port example; TCP and UDP Q1–Q4 |
| 6 | [DNS](DNS.md) | Trace a cold-cache lookup and interpret records/TTL | IP address concept | 300-second cache example; DNS Q1–Q3 |
| 7 | [DHCP](DHCP.md) | Explain DHCPv4 configuration and lease behavior | IP/subnet/gateway; UDP and DNS roles | Lease settings and expiry scenario; DHCP Q1–Q3 |
| 8 | [HTTP and Security](HTTP-AND-SECURITY.md) | Explain messages and HTTPS protection | DNS; TCP; IP/gateway | HTTP request and complete HTTPS trace; HTTP and Security Q1–Q3 |
| 9 | [SSH](SSH.md) | Distinguish server identity checks and user authentication | TCP; basic encryption/authentication concepts from HTTP | Host-fingerprint discrepancy; SSH Q1–Q3 |

All **30 chapter questions** have [explained answers](ANSWER-KEY.md). Try the question before reading its answer. The explanations give expected reasoning, not a marking rubric.

## Scope and Model Assumptions

- The module teaches core concepts and small examples, not production server administration.
- The introduction uses a five-layer model; the OSI chapter explains its relationship to the four-layer TCP/IP and seven-layer OSI models.
- The worked web trace assumes a fresh HTTP/1.1 HTTPS connection over TCP. HTTP/3 is named as a boundary; its QUIC mechanics are not taught.
- The subnet example is a normally configured IPv4 `/24` LAN. IPv6 address size and notation are introduced, but its on-link discovery is outside scope.
- DHCP means **DHCPv4** in its chapter. DHCPv6 and SLAAC operation are outside scope.
- Detailed exclusions are recorded at the end of each chapter. A scope label does not promise a finished slide deck or video.

## Evidence and Current Review State

The revised chapters cite standards or official documentation beside technical claims. The [HTTPS flow diagram](assets/https-request-flow.svg) is an original explanatory SVG in the repository and has a relative link from the introduction. It is not a packet capture.

AI assistance was used to identify technical issues and propose revised wording. The current pass checked question coverage, local links, and consistency of the teaching examples. **No team peer-review approval or live networking experiment is claimed.** The next step is for team members to review the chapters and answer explanations, record actual outcomes, and update this status only after that work occurs.

## Reuse in Study Resources

One developed topic can be reused without changing its technical assumptions:

- **Study guide:** the introduction's worked HTTPS trace, diagram, and explained answers to Q3–Q4.
- **Slides:** one diagram slide, followed by DNS, TCP/TLS, and HTTP stages with a short ordering activity.
- **Video:** narrate the same illustrative trace, then pause at the missing-TLS misconception and explain its correction.

These are proposed uses of current content, not claims that those resources have been produced.
