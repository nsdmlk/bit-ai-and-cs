# IP Addressing and Routing — A Micro-Textbook for Beginners

This is the first draft of our Network Layer content. It lives in the repo as `/content/Networks/ROUTING-AND-IP.md` and covers how IP addresses locate devices and how routers guide data across the global internet.

---

## Learning Objectives

After this section, a beginner should be able to:
1. Explain what an IP address is and contrast IPv4 with IPv6.
2. Describe how subnets split large networks into smaller, manageable neighborhoods.
3. Explain how routers use routing tables to make hop-by-hop forwarding decisions.
4. Define the role of a default gateway in connecting local networks to the wider internet.

---

## 1. IP Addresses: The Digital Postal Address

At Layer 3 (the Network layer), every device connected to a network needs a unique identifier: an **IP (Internet Protocol) address**. 

Unlike physical MAC addresses (which are hardcoded into your network card at the factory), IP addresses are **logical**. They change depending on where you connect—your laptop has one IP address on your home Wi-Fi, another at a coffee shop, and another on a cellular hotspot.

* **IPv4:** Written as four numbers separated by dots (e.g., `192.168.1.50`). Each number ranges from 0 to 255 (32-bit addresses), giving us about 4.3 billion unique addresses—which ran out years ago!
* **IPv6:** Written as groups of hexadecimal characters separated by colons (e.g., `2001:db8::ff00:42:8329`). Using 128-bit addresses, IPv6 provides enough IP addresses for every grain of sand on Earth.

---

## 2. Subnets: Network vs. Host Portions

An IP address doesn't just identify a machine; it identifies **what network** that machine lives on. An IP address is split into two parts:
1. **The Network ID:** Identifies the specific local network.
2. **The Host ID:** Identifies the exact machine on that network.

A **Subnet Mask** (or CIDR notation like `/24`) acts like a lens that tells computers which part of the IP address is the network and which part is the host. If two computers share the same network portion, they can talk directly. If they are on different networks, they must send data through a router.

---

## 3. Routers and Routing Tables: Step-by-Step Navigation

A **router** is a specialized computer that connects different networks together. When a router receives an IP packet, it looks at the destination IP address, checks its internal **routing table**, and decides which path (or "next hop") gets the packet closer to its final destination.

Routers don't need to know the entire map of the internet. They only need to know: *"If a packet is heading to network X, hand it to Router Y."* It's like asking for street directions one intersection at a time.

---

## 4. The Default Gateway: Your Exit Door

When your home computer wants to send data to a website across the world (which is on a totally different network), it realizes the destination IP doesn't match the local subnet. 

Instead, your computer hands the packet to its **Default Gateway** (usually your home Wi-Fi router). The default gateway acts as your local network's exit door, taking internal traffic and routing it out toward the wider internet.

---

## 5. Common Misconceptions

- **"An IP address permanently belongs to a physical device."** False. IP addresses are dynamic and assigned by routers or DHCP servers when you join a network.
- **"Routers look at every detail of your application data."** Routers operate at Layer 3; they look at IP headers to see source and destination addresses, but they rarely inspect the underlying TCP payload or web content.

---

## 6. Check Yourself

1. **Compare** IPv4 and IPv6: why was IPv6 created?
2. **What is a subnet mask**, and why do we need to split an IP address into a network portion and a host portion?
3. **Explain the role of a default gateway** when your computer communicates with a server in another country.

---

## 7. Scope Boundaries

- **Detailed:** IPv4 vs IPv6 structure, network/host ID concept, routing tables, default gateways.
- **Brief:** CIDR notation arithmetic, DHCP address leasing.
- **Out of scope:** BGP (Border Gateway Protocol) path vector internals, interior gateway routing protocols (OSPF, EIGRP mathematics).