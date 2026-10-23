# Network Types: PAN, LAN, MAN, and WAN — A Micro-Textbook for Beginners

This is the first draft of our Network Scale content. It lives in the repo as `/content/Networks/LAN-WAN-PAN.md` and covers how networks are categorized by their geographic physical footprint.

---

## Learning Objectives

After this section, a beginner should be able to:
1. Categorize networks by their physical scale (PAN, LAN, MAN, WAN).
2. Give real-world examples of each network category.
3. Understand the hardware boundaries that separate local networks from global wide-area networks.

---

## 1. Size Matters: Categorizing Networks

Networks come in vastly different sizes, ranging from a Bluetooth connection on your wrist to the global internet spanning continents. Network engineers categorize them by **geographic scope**.

---

## 2. The Four Main Scale Categories

| Network Type | Full Name | Geographic Scope | Typical Example |
|---|---|---|---|
| **PAN** | Personal Area Network | Centered around a single person (~10 meters) | Bluetooth headphones connected to your phone |
| **LAN** | Local Area Network | A single room, home, office, or building | Home Wi-Fi network, office ethernet switch |
| **MAN** | Metropolitan Area Network | Spans an entire city or town | A city's municipal Wi-Fi or cable provider grid |
| **WAN** | Wide Area Network | Spans countries, continents, or the globe | **The Internet**, enterprise multi-office links |

---

## 3. From Local to Global: How LANs Connect to WANs

* **LANs** use technologies like Ethernet cables and Wi-Fi access points. They are owned and controlled by individuals or organizations.
* **WANs** connect separate LANs across vast distances. Because you can't run a personal ethernet cable across an ocean, LANs connect to a **router** or **gateway** which hands data off to Internet Service Providers (ISPs) operating high-capacity fiber-optic trunk lines across the WAN.

---

## 4. Common Misconceptions

- **"Wi-Fi and the Internet are the same thing."** Wi-Fi is a local wireless technology (LAN) that connects your device to a router; the Internet is a global network of networks (WAN) that the router accesses.
- **"MANs are very common in daily conversation."** MANs exist conceptually between LANs and WANs, but in modern networking architecture, the line has blurred as high-speed fiber bridges city and regional links directly into global WANs.

---

## 5. Check Yourself

1. **Differentiate** between a PAN and a LAN with real-world examples.
2. **What connects a LAN to a WAN?** Name the primary hardware device responsible.
3. **Spot the error:** "My house has a great WAN connection because my Wi-Fi router covers every room." Correct the terminology.

---

## 6. Scope Boundaries

- **Detailed:** PAN, LAN, WAN definitions, hardware handoffs between local and global spaces.
- **Brief:** MAN characteristics.
- **Out of scope:** Submarine fiber-optic cable engineering, cellular tower base station design (5G cell topology).