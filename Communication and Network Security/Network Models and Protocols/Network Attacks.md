## Framing

Most network attacks are one of three things against traffic in transit — **reading it, changing it, or replaying it** — or one of two things against a session — **impersonating an endpoint or taking the session over**. Grouping them this way makes the defenses obvious, because each maps to a cryptographic service: confidentiality, integrity, freshness, authentication.

| Attack | What it violates | Core defense |
|---|---|---|
| Eavesdropping | Confidentiality | Encryption |
| Modification | Integrity | Integrity protection (MAC, signature) |
| Replay | Freshness | Sequence numbers, timestamps, nonces |
| Spoofing | Authentication | Mutual authentication |
| Hijacking | Session integrity | Authenticated, encrypted sessions |

## Eavesdropping

**Eavesdropping (sniffing, passive interception)** is capturing traffic without altering it. It is the hardest attack to detect, because it leaves no trace in the traffic itself — a passive tap or a promiscuous NIC changes nothing.

Where it happens:

- **On the wire**: a physical tap on copper, an unused port, or a compromised switch using port mirroring. Fiber is harder to tap without detection and emits no usable emanations (see [[Transmission Media]]).
- **On a switched LAN**: via ARP poisoning or MAC flooding (see [[Switch and VLAN Security]]).
- **On wireless**: simply by being in range (see [[Wireless Attacks]]).
- **At an intermediary**: a compromised router, a rogue proxy, a malicious ISP or carrier, or a rogue access point.
- **Out of band**: **emanations** from cables and screens (TEMPEST), and shoulder surfing — the reminder that not all interception is on the network.

Even when content is encrypted, **traffic analysis** of the metadata — who talks to whom, when, how much, how often — reveals relationships, schedules, and events. Padding, constant-rate traffic, and onion routing are the countermeasures, and they are expensive.

Defenses: **encrypt everything** (TLS, IPsec, SSH, MACsec), eliminate cleartext protocols (Telnet, FTP, HTTP, SNMPv1/2, POP3/IMAP without TLS), physically protect cabling and wiring closets, disable unused ports, and use switches rather than hubs. Detection is limited and indirect: finding a NIC in promiscuous mode, noticing an unknown device, or spotting the ARP anomalies that enable it.

## Modification Attacks

A **modification attack** alters data in transit — changing an amount, a destination account, a command, or a downloaded file — and requires the attacker to be **on the path**, usually established first through ARP or DNS poisoning, a rogue AP, or a compromised router.

Related forms:

- **On-path (man-in-the-middle) attack**: the attacker relays and can read and modify both directions, impersonating each party to the other. The umbrella position that makes modification possible.
- **Injection**: inserting new packets or content into an existing flow (forged TCP packets, injected scripts or ads in unencrypted HTTP).
- **Downgrade attack**: forcing a weaker version or cipher (SSL stripping, STARTTLS stripping) so that the content becomes modifiable at all.
- **Data diddling**: small, hard-to-notice alterations repeated over time; the fraud pattern rather than the burst attack.

Defenses: **integrity protection** rather than encryption alone — an AEAD cipher suite, a MAC, a digital signature, signed software updates. **Authenticate the endpoint**, so the attacker cannot be the other party: certificate validation, certificate pinning, HSTS, mutual TLS, SSH host key verification. The failure mode in practice is almost always **a user or client ignoring a certificate warning**.

## Replay Attacks

A **replay attack** captures valid traffic and **resends it later** — an authentication exchange, a transaction, a command — without needing to decrypt or understand it. Encryption alone does not stop it, which is why it is worth separating from the other two: the replayed message is genuine.

Defenses: **sequence numbers**, **timestamps** with a validity window (the reason Kerberos requires synchronized clocks), **nonces** and challenge-response (the reason CHAP challenges rather than accepting a hash), and **session tokens that expire**. Note that **packet sequencing** and session-layer controls exist in protocols partly for this reason.

## Spoofing and Masquerading

**Spoofing** is claiming an identity that is not yours, at whichever layer is convenient:

- **MAC spoofing** to defeat address-based filtering.
- **IP spoofing** to bypass address-based trust, hide an attack's origin, or make a reflection/amplification DDoS land on a victim. Mitigated by **ingress and egress filtering** at the network edge.
- **ARP spoofing** for on-path position on the LAN.
- **DNS spoofing/poisoning** to send a victim to the wrong server (see [[DNS and DNS Attacks]]).
- **Email and caller-ID spoofing** for social engineering (see [[Email Security]], [[Voice Communications]]).
- **Rogue access points and evil twins** at the wireless layer.

The common root: **the protocol carries an identifier but no proof of identity**. The answer is always to add cryptographic authentication rather than to trust the identifier.

## Session Hijacking

**Hijacking** takes over an **already-authenticated** session, so the attacker never needs the credential. Mechanisms: stealing a session cookie or token (via XSS, sniffing an unencrypted session, or a shared machine), predicting TCP sequence numbers, or inserting into a session from an on-path position. **TCP session hijacking** classically desynchronizes the legitimate client and continues the session in its place.

Defenses: encrypt the whole session (not just the login), random and long session identifiers, **re-authenticate before sensitive actions**, bind the session to attributes that are hard to move, idle and absolute timeouts, cookie flags (Secure, HttpOnly, SameSite), and periodic re-authentication of the link, which is what CHAP does.

## Key Points

- **Eavesdropping is passive and nearly undetectable; encryption makes it useless, but metadata still supports traffic analysis.**
- **Modification requires an on-path position and is defeated by integrity protection plus endpoint authentication — not by encryption alone.**
- **Replay resends genuine captured traffic; encryption does not stop it, sequence numbers, timestamps, and nonces do.**
- **Spoofing works wherever a protocol carries an identifier without proof: MAC, IP, ARP, DNS, email, caller ID.**
- **Hijacking takes over an authenticated session and bypasses the credential entirely; protect the whole session, not only the login.**
