# Network Types: PAN, LAN, MAN, and WAN — A Micro-Textbook for Beginners

This chapter compares networks by their typical geographic scope.

**Status:** Revised with AI-assisted technical checks; awaiting team peer review.

[Module outline and reading order](OUTLINE.md) · [Explained answers](ANSWER-KEY.md)

---

## Learning Objectives

After this section, a beginner should be able to:

1. Distinguish PAN, LAN, MAN, and WAN by typical scope.
2. Give an example of each category.
3. Explain the different roles of an access point and a router.

## 1. Categorizing Networks

A connection between a phone and headphones has a different scope from a network linking offices in different countries. The labels below describe useful categories, rather than fixed distance thresholds or mandatory hardware designs.

## 2. Four Common Scale Categories

| Type | Full name | Typical scope | Example |
|---|---|---|---|
| **PAN** | Personal Area Network | Devices around one person | Phone and Bluetooth headphones |
| **LAN** | Local Area Network | Home, office, building, or campus | Devices sharing an office Ethernet/Wi-Fi network |
| **MAN** | Metropolitan Area Network | A city or metropolitan area | A network connecting municipal sites across a city |
| **WAN** | Wide Area Network | Connections across larger geographic areas | Enterprise links between distant offices |

The Internet connects many networks worldwide and is a useful WAN-scale example. A PAN is often short-range, but “10 meters” is not a universal Bluetooth limit: achievable range depends on the radio design and environment. [Bluetooth SIG, understanding range](https://www.bluetooth.com/learn-about-bluetooth/key-attributes/range/)

## 3. Connecting Local and Wider Networks

An **access point** lets Wi-Fi devices join a local wireless network. A **switch** connects devices within a local wired network. A **router** forwards packets between IP networks; it can connect a LAN to a provider's wider network.

A home “Wi-Fi router” usually combines several roles, including an access point and router. The roles are still different. A local network can operate without an Internet connection. [Cisco, networking basics](https://www.cisco.com/site/us/en/learn/topics/small-business/networking-basics.html), [Cisco, access points](https://www.cisco.com/site/us/en/learn/topics/small-business/what-is-an-access-point.html)

WAN connections can use provider fiber, cellular, or other links. They are not defined by a particular cable or by crossing an ocean.

**Example:** A laptop can reach a home printer over Wi-Fi while the home's Internet service is down. Its local link works; the path to remote Internet services does not. This is an illustrative scenario, not a measured test.

## 4. Common Misconceptions

- **“Wi-Fi and the Internet are the same thing.”** Wi-Fi provides local wireless connectivity. Reaching the Internet requires a working path beyond that local network.
- **“Full Wi-Fi signal proves good Internet service.”** Signal strength says something about the local wireless link, not the entire path to a remote service.

## 5. Check Yourself

1. **Differentiate** a PAN and a LAN with examples.
2. **What connects a LAN to a WAN?** Name the primary device role and distinguish it from an access point.
3. **Spot the error:** “My house has a great WAN connection because my Wi-Fi router covers every room.” Correct the terminology.

[Explained answers: Network Types Q1–Q3](ANSWER-KEY.md#network-types)

## 6. Scope Boundaries

- **Detailed:** Network scale categories and access point/switch/router roles.
- **Brief:** MAN examples and different WAN link technologies.
- **Out of scope:** Fixed distance classifications, provider network design, submarine cables, and cellular radio engineering.
