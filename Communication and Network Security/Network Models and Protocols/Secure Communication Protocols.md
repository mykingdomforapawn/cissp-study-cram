## Overview

Secure communication protocols add **confidentiality, integrity, and authentication** to traffic that the base TCP/IP suite sends in cleartext. They differ mainly in **which layer they operate at**, which decides what they protect and what they leave exposed, and in whether they protect **a link, a session, or a message**.

## The Protocols

| Protocol | Layer | What it protects | Notes |
|---|---|---|---|
| **IPsec** | Network (3) | Any IP traffic, transparently to applications | **AH** for integrity and authentication, **ESP** for encryption (plus integrity); **transport mode** (payload only) vs **tunnel mode** (whole packet, for VPNs); keys via **IKE**. Detail in [[Network Encryption]] |
| **TLS** (successor of SSL) | Between transport and application (session/presentation) | A single application session, usually HTTPS, but also mail, LDAP, VPNs | Server authenticated by certificate, client optionally; **TLS 1.2 and 1.3** are current, SSL and TLS 1.0/1.1 are deprecated. Detail in [[Web Applications]] |
| **SSH** | Application (7) | Remote terminal, file transfer (SFTP, SCP), and **port forwarding / tunneling** of other protocols | Replaces Telnet, rlogin, rsh and FTP; authenticates with passwords or keys; port 22 |
| **Kerberos** | Application | **Authentication** in a domain, with single sign-on | Ticket-based, uses a trusted **KDC**; symmetric cryptography; relies on time synchronization. Covered in Domain 5 |
| **Secure RPC (S-RPC)** | Session/application | Authentication for remote procedure calls | Adds authentication to RPC, which otherwise trusts the caller |
| **Signal Protocol** | Application | End-to-end encrypted messaging and calls | Double Ratchet gives **forward secrecy** per message; used by Signal, WhatsApp, and others |
| **SET** (Secure Electronic Transaction) | Application | Card payment transactions | Historical; replaced in practice by TLS plus PCI DSS controls |

## Choosing by Layer

- **Lower layer means broader and more transparent.** IPsec protects every application without any application change, and hides transport headers (ports) in tunnel mode. It is the choice for site-to-site and remote access VPNs.
- **Higher layer means more targeted and more application-aware.** TLS protects one session and lets the application decide what to authenticate; SSH protects one administrative connection. Neither hides IP addresses.
- **Link encryption vs end-to-end**: encryption on a link (including a VPN tunnel) is removed at the tunnel endpoint, so traffic beyond it is exposed again. End-to-end encryption (TLS to the real server, Signal between two devices) stays encrypted through every intermediary. See [[Network Encryption]] for the trade-off.

## Common Concerns

- **Deprecated versions**: SSLv2/v3, TLS 1.0/1.1, SSH-1, WEP-era ciphers. A secure protocol in an old version is not secure.
- **Certificate validation**: TLS only authenticates the server if the client actually checks the certificate chain, name, and revocation. Disabled validation makes interception trivial.
- **Key management**: IPsec pre-shared keys that never rotate, SSH host keys accepted without verification, and long-lived API keys are all common failures.
- **Encrypted does not mean inspected**: encrypted traffic blinds IDS and DLP; organizations use TLS inspection (a controlled interception proxy) on egress, which has its own privacy and legal considerations.

## Key Points

- **IPsec = layer 3, protects all IP traffic, AH/ESP, transport vs tunnel mode, the VPN workhorse.**
- **TLS = per-session, certificate-based server authentication, the basis of HTTPS; SSL and TLS 1.0/1.1 are dead.**
- **SSH = secure remote administration and file transfer, and a tunnel for anything else.**
- **Kerberos = ticket-based authentication with a KDC and single sign-on; S-RPC authenticates remote calls.**
- **Signal gives end-to-end encryption with per-message forward secrecy.**
