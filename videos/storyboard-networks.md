# Storyboard 02 — How an HTTPS Request Travels

## Objective

Learners will distinguish DNS, TCP, TLS, HTTP, and IP while tracing a new HTTPS
connection.

| Time | Screen / visual | Narration | Learner action |
|---|---|---|---|
| 0:00–0:20 | Browser and server | “How does a name become a protected web response?” | State one thing the browser needs first. |
| 0:20–0:50 | Learning objective | Name the five responsibilities in the trace. | Listen for the order. |
| 0:50–1:30 | DNS diagram | DNS resolves a hostname to an IP address; caching may shorten later lookups. | Label name versus address. |
| 1:30–2:10 | IP route | IP packets move toward the destination using logical addresses and routes. | Identify the network-layer job. |
| 2:10–2:50 | TCP handshake | TCP establishes a connection and provides ports, ordering, and reliability. | Explain why the server needs a port. |
| 2:50–3:30 | TLS boundary | TLS authenticates the server and protects the HTTP exchange in HTTPS. | Name what TLS adds to HTTP. |
| 3:30–4:10 | HTTP request/response | Show method, path, status code, headers, and content. | Predict what a 404 means. |
| 4:10–4:40 | Pause activity | Which component handles naming, routing, reliability, and application meaning? | Answer four labels. |
| 4:40–5:00 | Answer and recap | Reveal DNS, IP, TCP, and HTTP/TLS assignments. | Explain why layers are separated. |

## Required source links

`content/Networks/INTRODUCTION.md`, `DNS.md`, `ROUTING-AND-IP.md`,
`TCP-AND-UDP.md`, and `HTTP-AND-SECURITY.md`.

## Review checks

Keep TLS in the trace. Do not claim that IP guarantees delivery or that OSI is a
literal implementation sequence for every Internet connection.
