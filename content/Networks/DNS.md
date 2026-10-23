# DNS (Domain Name System) — A Micro-Textbook for Beginners

This is the first draft of our DNS content. It lives in the repo as `/content/Networks/DNS.md` and explains how the internet translates human-readable names into machine-routable IP addresses.

---

## Learning Objectives

After this section, a beginner should be able to:
1. Explain what DNS is and why it functions as the "phonebook of the internet."
2. Name the hierarchy of DNS servers involved in resolving a domain name.
3. Describe the concept of DNS caching and why it makes web browsing fast.
4. Identify common types of DNS records (A, AAAA, CNAME, MX).

---

## 1. What Is DNS and Why Do We Need It?

Humans remember names easily (`google.com`, `github.com`), but computers talk using numeric IP addresses (`142.250.190.46`). 

The **Domain Name System (DNS)** is a globally distributed database that maps human names to IP addresses. Without DNS, you would have to type a string of numbers into your browser for every website you want to visit.

---

## 2. The Hierarchy of DNS Resolution

When your device doesn't know an IP address, it launches a multi-step query through a chain of specialized servers:

1. **Recursive Resolver (ISP or Public DNS like 8.8.8.8):** Your computer's first stop. The resolver accepts your request and does the heavy lifting of querying the rest of the internet on your behalf.
2. **Root Name Servers:** The top of the hierarchy (13 logical root server authorities worldwide). When the resolver asks for `example.com`, the root server looks at `.com` and points the resolver to a **Top-Level Domain (TLD) server**.
3. **TLD Name Servers:** Servers responsible for specific extensions like `.com`, `.org`, or `.jp`. The TLD server looks at `example` and points the resolver to the **Authoritative Name Server**.
4. **Authoritative Name Server:** The final authority maintained by the domain owner (e.g., AWS Route 53 or Cloudflare). It holds the actual IP address record for `example.com` and hands it back.

---

## 3. DNS Records: Types of Entries

DNS databases contain different record types depending on what information is needed:

* **A Record:** Maps a domain name to an **IPv4 address** (e.g., `192.0.2.1`).
* **AAAA Record:** Maps a domain name to an **IPv6 address** (longer format).
* **CNAME (Canonical Name):** Creates an alias, pointing one domain name to another (e.g., `www.example.com` points to `example.com`).
* **MX Record (Mail Exchange):** Specifies the mail servers responsible for receiving email for a domain.

---

## 4. Caching: Making Lookups Instant

If every single click on the internet required querying Root, TLD, and Authoritative servers across the globe, the web would feel sluggish. 

To prevent this, **DNS caching** happens at multiple levels:
* Your local operating system and browser cache recent lookups.
* Your local router or ISP resolver caches results based on a **TTL (Time To Live)** expiration timer set by the domain owner.

---

## 5. Common Misconceptions

- **"DNS is stored on one giant master computer."** False. DNS is completely decentralized and distributed across thousands of servers worldwide.
- **"Changing a website's IP address updates globally instantly."** Propagation delays happen because intermediate resolvers cache old DNS records until their TTL expires.

---

## 6. Check Yourself

1. **Trace a DNS lookup:** What are the roles of the recursive resolver, root servers, TLD servers, and authoritative servers?
2. **What is an A record** compared to a CNAME record?
3. **Explain the purpose of TTL (Time To Live)** in a DNS record.

---

## 7. Scope Boundaries

- **Detailed:** Resolver hierarchy, root/TLD/authoritative split, basic record types (A, CNAME, MX), caching.
- **Brief:** Anycast routing for DNS servers, DNSSEC security extensions.
- **Out of scope:** BIND configuration files, advanced zone file scripting, reverse DNS pointer records (PTR internals).