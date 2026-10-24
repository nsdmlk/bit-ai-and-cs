# SSH (Secure Shell) — A Micro-Textbook for Beginners

This is the first draft of our SSH content, intended for `/content/Networks/SSH.md`. It explains how users securely connect to remote computers and run commands over a network.

---

## Learning Objectives

After this section, a beginner should be able to:

1. Explain what SSH is and why remote connections need protection.
2. Describe the roles of an SSH client and an SSH server.
3. Compare password authentication with public-key authentication.
4. Explain why checking a server's host key matters.

---

## 1. What Is SSH and Why Do We Need It?

Imagine managing a computer in another building—or another country. You need to run commands on it, but you do not want people on the network to read your password or change your commands.

**Secure Shell (SSH)** is a protocol for secure remote access. It provides **encryption** to keep session data private, **integrity protection** to detect tampering, and **authentication** to verify identities. Think of it as a protected connection between your computer and a remote machine. [SSH architecture: RFC 4251](https://www.rfc-editor.org/rfc/rfc4251)

A **shell** is a program that interprets commands. With SSH, you can use a remote computer's shell from your own terminal.

---

## 2. Clients and Servers: How a Connection Starts

SSH uses a **client-server model**:

- **SSH client:** The program on your computer that initiates the connection.
- **SSH server:** The program on the remote computer that accepts connections, commonly called `sshd`.

A typical connection follows these steps:

1. **Connect:** The client contacts the server, normally using **TCP port 22**.
2. **Establish protection:** Both sides negotiate security settings and perform a key exchange. The client also checks the server's identity using its host key.
3. **Authenticate the user:** The server checks whether the user can access the requested account.
4. **Start a session:** If access is allowed, the server can open a shell or execute a command. Session data travels through the encrypted connection. [OpenSSH server documentation](https://man.openbsd.org/sshd)

For example, `ssh student@server.example.com` requests access to the account `student` on the specified server. Commands entered after a successful shell login run on that remote computer. [OpenSSH client documentation](https://man.openbsd.org/ssh)

---

## 3. Authentication: Passwords and Key Pairs

Two common ways to authenticate are:

- **Password authentication:** You provide the remote account's password. SSH sends it through the encrypted connection.
- **Public-key authentication:** You use a mathematically related pair of keys: a **public key** and a **private key**.

The public key is registered with the account on the server. The private key stays under your control. During authentication, the client creates a digital signature that the server verifies using the public key. **The private key itself is not sent to the server.** [SSH authentication: RFC 4252](https://www.rfc-editor.org/rfc/rfc4252)

A private key can also be protected by a **passphrase**, which helps protect the stored key if someone obtains the key file. This passphrase is separate from the remote account's password. [OpenSSH client documentation](https://man.openbsd.org/ssh)

---

## 4. Host Keys: Checking the Server's Identity

Authentication works in both directions: the server checks the user, and the client checks the server.

A **host key** identifies the server. On a first connection, an SSH client may display its **fingerprint**, a short representation of the public host key. Compare it with a value obtained through a trusted channel, such as the server administrator.

OpenSSH remembers accepted host keys in its `known_hosts` file. If a key changes later, it warns you. A change might follow a legitimate server replacement, but it can also indicate impersonation, so investigate before accepting it. [OpenSSH host-key verification](https://man.openbsd.org/ssh#VERIFYING_HOST_KEYS)

---

## 5. Common Misconceptions

- **"My public key must remain secret."** False. Public keys are designed to be shared. The private key must remain protected.
- **"Opening an SSH session encrypts all my internet traffic."** False. SSH protects data carried through its connection. Other application traffic does not automatically pass through it. [SSH architecture: RFC 4251](https://www.rfc-editor.org/rfc/rfc4251)

---

## 6. Check Yourself

1. **Trace an SSH connection:** What happens between contacting the server and opening a remote shell?
2. **Compare public and private keys:** Which key is registered on the server, and which must remain protected?
3. **Explain host-key verification:** Why should you check a server's fingerprint before trusting it?

---

## 7. Scope Boundaries

- **Detailed:** Client-server roles, TCP port 22, encrypted sessions, password and public-key authentication, host-key verification.
- **Brief:** File transfers with SFTP, port forwarding, private-key passphrases.
- **Out of scope:** Cryptographic mathematics, advanced SSH configuration, certificate authorities, complex tunneling setups.
