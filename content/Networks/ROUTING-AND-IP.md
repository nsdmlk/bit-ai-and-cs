# IP Addressing and Routing — A Micro-Textbook for Beginners

This chapter explains interface addresses, subnet prefixes, and hop-by-hop forwarding.

**Status:** Revised with AI-assisted technical checks; awaiting team peer review.

[Module outline and reading order](OUTLINE.md) · [Explained answers](ANSWER-KEY.md)

---

## Learning Objectives

After this section, a beginner should be able to:

1. Explain IP addresses and compare IPv4 with IPv6.
2. Use a simple IPv4 prefix to distinguish local and remote destinations.
3. Describe how a router uses a routing table.
4. Explain the default gateway's role.

## 1. IP Addresses: Logical Network Addresses

To communicate using IP, a network interface uses an **IP address**. A device may have several interfaces or addresses. An address is not a permanent physical-device identity, and private addresses can be reused on separate networks. [IPv6 addressing model: RFC 4291 §2.1](https://www.rfc-editor.org/rfc/rfc4291.html#section-2.1), [Private IPv4: RFC 1918 §3](https://www.rfc-editor.org/rfc/rfc1918.html#section-3)

A **MAC address** is used for local-link communication on technologies such as Ethernet and Wi-Fi. Interfaces may have factory-assigned MAC addresses, but software can also configure or randomize the address used. [Apple, private Wi-Fi addresses](https://support.apple.com/en-nz/102509)

- **IPv4:** 32 bits, usually written as four decimal numbers from 0 to 255, such as `192.168.1.50`. There are about 4.3 billion possible values, including reserved ranges. The original IANA unallocated pool was exhausted in 2011; existing IPv4 networks continue to operate. [NRO, IPv4 free-pool exhaustion](https://www.nro.net/ipv4-free-pool-depleted/)
- **IPv6:** 128 bits, written using hexadecimal groups and colons, such as the documentation address `2001:db8::50`. Its much larger address space addresses the shortage inherent in IPv4. [RFC 4291 §§2–2.2](https://www.rfc-editor.org/rfc/rfc4291.html#section-2)

## 2. Subnets: Prefix and Interface Portion

For a simple IPv4 LAN, a **subnet mask** identifies the network prefix. The remaining bits distinguish interface addresses within that subnet. **CIDR notation** writes the prefix length after a slash: `/24` means the first 24 bits are the prefix. [RFC 4632 §3.1](https://www.rfc-editor.org/rfc/rfc4632.html#section-3.1)

**Worked example:** A laptop has `192.168.1.50/24`, with mask `255.255.255.0`. Its subnet is `192.168.1.0/24`.

- Destination `192.168.1.80` shares that prefix. In this normally configured LAN, the laptop can send to it on the local link.
- Destination `192.168.2.20` does not share the prefix. The laptop needs an appropriate route through a router.

This example assumes the devices are attached to the expected links and communication is permitted. Matching address digits alone cannot repair a disconnected cable or an incorrect network setup. IPv6 also uses prefixes, but its on-link discovery details are outside this chapter.

## 3. Routers and Routing Tables

A **router** forwards IP packets between networks. It checks a destination against its routing table and chooses an outgoing interface or next hop. The most specific matching prefix is preferred; a default route provides a fallback. [RFC 1812 §5.2.4](https://www.rfc-editor.org/rfc/rfc1812.html#section-5.2.4)

A router does not need to store the complete journey for each packet. One entry might mean: “For this destination prefix, send to the next router on this interface.” Each hop makes its own forwarding decision.

## 4. The Default Gateway

A host's **default gateway** is the next-hop router used by its default route when no more specific route applies. On a home network, this is commonly the home router.

For example, the laptop above might use gateway `192.168.1.1`. To contact `203.0.113.10` in our [HTTPS example](INTRODUCTION.md#6-worked-example-a-new-https-connection), it sends frames to the gateway while the IP packet identifies the remote destination. The gateway forwards it toward another network.

The decision concerns addresses and routes, not country borders. A nearby server can be on another network; a remote service's geographic location is not encoded directly in the host's subnet comparison.

## 5. Common Misconceptions

- **“An IP address permanently belongs to a physical device.”** Addresses may be configured manually or automatically, for example with DHCP. They can remain stable or change. A router only assigns DHCP addresses if it also runs that service. [Microsoft DHCP overview](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top)
- **“Routers must read webpage content to forward packets.”** Ordinary IP forwarding uses network-layer information. A device that also performs firewall or proxy functions may inspect more.

## 6. Check Yourself

1. **Compare** IPv4 and IPv6: why was a larger address space needed?
2. **Explain a subnet mask.** For `192.168.1.50/24`, which destination is local in the example: `192.168.1.80` or `192.168.2.20`, and why?
3. **Explain a default gateway** when a destination is outside the local subnet and no more specific route applies.

[Explained answers: IP and Routing Q1–Q3](ANSWER-KEY.md#ip-and-routing)

## 7. Scope Boundaries

- **Detailed:** Address versus device identity, IPv4/IPv6 size, a `/24` example, routing tables, default gateway.
- **Brief:** Private address reuse, configurable MAC addresses, static versus automatic configuration.
- **Out of scope:** General subnet arithmetic, IPv6 on-link discovery, NAT internals, BGP, OSPF, and EIGRP.
