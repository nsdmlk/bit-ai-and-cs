# HTTP, HTTPS, and Security — A Micro-Textbook for Beginners

This chapter explains web requests and responses, then the protection supplied by TLS.

**Status:** Revised with AI-assisted technical checks; awaiting team peer review.

[Module outline and reading order](OUTLINE.md) · [Explained answers](ANSWER-KEY.md)

---

## Learning Objectives

After this section, a beginner should be able to:

1. Explain HTTP's client-server model.
2. Identify methods, targets, headers, bodies, and status codes.
3. Explain how HTTPS adds confidentiality, server authentication, and tamper detection.

## 1. HTTP: Communication on the Web

**HTTP (Hypertext Transfer Protocol)** is an application protocol. A **client**, often a browser, requests a resource or submits information. A **server** processes the request and returns a response. The resource could be HTML, an image, or data for an application. [RFC 9110 §§1–3](https://www.rfc-editor.org/rfc/rfc9110.html#section-1)

A page can require many requests. Conversely, cached content or an existing connection can avoid some network work, so every click does not necessarily begin a fresh connection.

## 2. Requests and Responses

A request identifies a **method**, a **target** such as `/about`, and **headers**. It can also contain a **body**, for example form data.

- **GET:** Request a representation of a resource.
- **POST:** Submit data for the target resource to process, such as a form.
- **PUT:** Request creation or replacement of the target resource's state with the submitted representation.
- **DELETE:** Request removal of the target resource's association with its current functionality.

A response includes a **status code**, headers, and sometimes a body. Common examples are:

| Status | Meaning |
|---|---|
| **200 OK** | The request succeeded |
| **301 Moved Permanently** | A permanent redirect |
| **302 Found** | A temporary redirect |
| **404 Not Found** | The server did not find a current representation, or will not disclose one |
| **500 Internal Server Error** | An unexpected server-side problem prevented completion |

A 500 does not necessarily mean the server crashed. Status classes provide a broader guide: **1xx** informational, **2xx** successful, **3xx** redirection, **4xx** client error, **5xx** server error. [RFC 9110 §§9 and 15](https://www.rfc-editor.org/rfc/rfc9110.html#section-15)

**Illustrative HTTP/1.1 request:**

```http
GET /about HTTP/1.1
Host: example.com
Accept: text/html

```

The server might respond with `200 OK`, a `Content-Type: text/html` header, and an HTML body. With HTTPS, these HTTP details travel inside protected communication rather than appearing as cleartext on the network.

**Cookies in brief:** A response can use `Set-Cookie` to ask the browser to store a cookie. Subject to its scope and browser rules, the browser later includes it in a `Cookie` request header. This can help associate requests with a session. [RFC 6265 §3](https://www.rfc-editor.org/rfc/rfc6265.html#section-3)

## 3. Plain HTTP

Plain `http://` provides no transport encryption of HTTP data. Someone able to observe the traffic on its path may read it, and an active intermediary may alter it. Local Wi-Fi encryption does not supply protection across the entire route to the web server.

## 4. HTTPS and TLS

**HTTPS** protects HTTP communication using **TLS (Transport Layer Security)**. In a new certificate-based HTTPS connection over TCP:

1. The client and server establish TCP, normally to server port **443**.
2. A TLS handshake establishes security parameters and keys. The client validates the server's certificate and its association with the requested hostname.
3. HTTP requests and responses travel in protected TLS records. **Encryption** protects their contents from network observers. **Integrity protection** detects tampering, so altered records are rejected.

TLS does not prevent an attacker from dropping traffic or interrupting a connection, and connection metadata can remain visible. It protects communication between its endpoints; it does not prove that the website's content or business is honest. [RFC 8446 §§1–2](https://www.rfc-editor.org/rfc/rfc8446.html#section-1), [HTTPS: RFC 9110 §4.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-4.2.2)

The [complete worked trace](INTRODUCTION.md#6-worked-example-a-new-https-connection) connects DNS, routing, TCP, TLS, and HTTP. HTTP/3 uses QUIC over UDP instead of this TCP setup; its details are outside the chapter. [RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html)

## 5. Common Misconceptions

- **“HTTP and HTML are the same thing.”** HTTP is a communication protocol; HTML describes the structure of a webpage.
- **“HTTPS means a site cannot be a scam.”** An encrypted, authenticated connection can still lead to a malicious site.
- **“TLS makes data impossible to modify.”** It detects tampering with protected data; it cannot prevent every network disruption.

## 6. Check Yourself

1. **Describe** the difference between GET and POST using a webpage or form example.
2. **Explain 404:** what does it mean, and which kind of component returns that HTTP response?
3. **Explain HTTPS protection** compared with plain HTTP on an untrusted network. What does it not establish about the website?

[Explained answers: HTTP and Security Q1–Q3](ANSWER-KEY.md#http-and-security)

## 7. Scope Boundaries

- **Detailed:** Client-server exchange, methods, message components, selected status codes and classes, TLS protection.
- **Brief:** Cookie exchange, certificate/name validation, the HTTP/3 boundary.
- **Out of scope:** Cryptographic mathematics, complete HTTP syntax, cookie security policy, HTTP/2 multiplexing, QUIC mechanics.
