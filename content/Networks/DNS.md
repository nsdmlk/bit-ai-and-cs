# DNS (Domain Name System) — A Micro-Textbook for Beginners

This chapter explains how names lead to network addresses and why caching reduces lookup work.

**Status:** Revised with AI-assisted technical checks; awaiting team peer review.

[Module outline and reading order](OUTLINE.md) · [Explained answers](ANSWER-KEY.md)

---

## Learning Objectives

After this section, a beginner should be able to:

1. Explain DNS's role in retrieving information associated with names.
2. Describe recursive resolvers, root servers, TLD servers, and authoritative servers.
3. Explain caching and TTL.
4. Distinguish A, AAAA, CNAME, and MX records.

## 1. What Is DNS?

People can remember names such as `example.com` more easily than numeric addresses. The **Domain Name System (DNS)** is a distributed, hierarchical system for retrieving records associated with names. Address lookup is one important use; DNS also stores other information, such as mail-routing records.

The “phonebook of the Internet” analogy captures name lookup, although real DNS is distributed across many independently operated servers. Without DNS, applications would need another way to obtain destination addresses. [RFC 1034 §§2–3](https://www.rfc-editor.org/rfc/rfc1034.html#section-2)

## 2. A Lookup Without Useful Cached Information

If neither the device nor its resolver has a usable answer, a simple lookup for `example.com` can involve:

1. **Recursive resolver:** Receives the device's question and obtains an answer on its behalf. It may be provided by an ISP, an organization, or a public DNS service.
2. **Root name server:** Directs the resolver toward servers for the relevant top-level domain, such as `.com`.
3. **TLD name server:** Supplies delegation information pointing toward the authoritative servers for `example.com`.
4. **Authoritative name server:** Answers from the records for the relevant zone. An answer may contain an address, an alias, or other information depending on the question.

The resolver returns the result to the client. Cached answers or delegations can let it skip parts of this path. [RFC 1034 §5.3.3](https://www.rfc-editor.org/rfc/rfc1034.html#section-5.3.3)

The root system has **13 named authorities**, served by many physical instances worldwide. This does not mean that only 13 physical root servers exist. [IANA root servers](https://www.iana.org/domains/root/servers)

## 3. Common Record Types

| Type | What it supplies | Illustrative use |
|---|---|---|
| **A** | IPv4 address | `example.com` → `192.0.2.10` |
| **AAAA** | IPv6 address | `example.com` → `2001:db8::10` |
| **CNAME** | Another DNS name, making the owner name an alias | `www.example.com` → `example.com` |
| **MX** | Mail server names and their preferences | Identifies where mail for a domain should be delivered |

These are documentation examples, not results of live DNS queries. A and CNAME differ because one supplies an address while the other points to another name. [RFC 1034 §3.6](https://www.rfc-editor.org/rfc/rfc1034.html#section-3.6), [AAAA: RFC 3596 §2](https://www.rfc-editor.org/rfc/rfc3596.html#section-2)

## 4. Caching: Making Lookups Faster

The operating system, browser, and recursive resolver may retain lookup results. A **TTL (Time To Live)** on DNS data specifies how long it can ordinarily be reused from a cache before a fresh lookup is needed.

**Worked example:** A resolver caches an address with a TTL of 300 seconds. One minute later, a second client asks for the same record. The resolver can normally reuse the cached answer, with less time remaining on its TTL. If the authoritative address changes meanwhile, clients using the old cached record may temporarily receive the old value. [RFC 1034 §3.6](https://www.rfc-editor.org/rfc/rfc1034.html#section-3.6)

The TTL is not a promise that all caches update together at one global instant.

## 5. Common Misconceptions

- **“DNS is stored on one master computer.”** It is distributed and hierarchically delegated.
- **“Every lookup contacts root, TLD, and authoritative servers.”** Caches can answer directly or shorten the path.
- **“Changing a record updates every user's answer immediately.”** Existing cached records can remain in use until their cache lifetime ends.

## 6. Check Yourself

1. **Trace a lookup without useful caches:** what do the recursive resolver, root, TLD, and authoritative servers do?
2. **Compare an A record with a CNAME record.** Which returns an address and which returns another name?
3. **Explain TTL:** why can two clients briefly receive different addresses after a record changes?

[Explained answers: DNS Q1–Q3](ANSWER-KEY.md#dns)

## 7. Scope Boundaries

- **Detailed:** Resolver hierarchy, A/AAAA/CNAME/MX records, caching and TTL.
- **Brief:** Local caches and the distinction between named root authorities and physical instances.
- **Out of scope:** Anycast routing, DNSSEC, zone-file configuration, advanced delegation cases, reverse DNS, and encrypted DNS transports.
