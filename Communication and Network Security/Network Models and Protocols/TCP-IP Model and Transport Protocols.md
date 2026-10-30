## TCP/IP Model

The **TCP/IP model** (also called the DARPA or DoD model) is the four-layer model that the internet actually runs on. It predates OSI and is a description of a working protocol suite rather than a design framework.

| TCP/IP layer | OSI equivalent | Protocols |
|---|---|---|
| **Application** | Application, Presentation, Session | HTTP, FTP, SMTP, DNS, SSH, SNMP ... |
| **Transport** (host-to-host) | Transport | TCP, UDP |
| **Internet** | Network | IP, ICMP, IGMP, IPsec, ARP (placed here or at link by different sources) |
| **Link** (network access) | Data Link, Physical | Ethernet, Wi-Fi, PPP |

The TCP/IP suite was designed for **interoperability, not security**. Most core protocols carry data in cleartext and have no authentication, which is why so much of network security consists of adding protections around them (TLS, IPsec, SSH, DNSSEC).

## TCP

The **Transmission Control Protocol** is **connection-oriented** and **reliable**: it numbers every byte, acknowledges receipt, retransmits lost segments, delivers data in order, and applies flow control through a sliding window. The cost is overhead and latency.

**Three-way handshake** establishes a session:

1. Client sends **SYN** (with its initial sequence number).
2. Server replies **SYN/ACK**.
3. Client replies **ACK**; the session is established.

A session is closed gracefully with **FIN / ACK** exchanges, or abruptly with **RST**.

**TCP header flags** (one bit each): **URG, ACK, PSH, RST, SYN, FIN** (plus ECE and CWR for congestion). Flags are what packet filters and scanners look at: a SYN without ACK is a new connection attempt, so a firewall can block inbound SYNs while allowing established traffic. Flag combinations that never occur legitimately (SYN+FIN, all flags set, no flags) are used in scanning and evasion.

Attacks that exploit TCP mechanics:

- **SYN flood**: many half-open connections exhaust the server's connection table. Defenses are SYN cookies and rate limiting.
- **Session hijacking / sequence prediction**: if the attacker can guess sequence numbers they can inject into or take over a session. Random initial sequence numbers and encryption are the defenses.

## UDP

The **User Datagram Protocol** is **connectionless** and **best-effort**: no handshake, no acknowledgment, no ordering, no retransmission. The header is only 8 bytes. It suits traffic where speed matters more than every packet arriving: DNS queries, VoIP, streaming, SNMP, DHCP, TFTP. Because there is no handshake, source addresses are trivially spoofed, which makes UDP services the usual amplifiers in reflection DDoS attacks (DNS, NTP, memcached).

## Ports

A **port** is a 16-bit number (0 to 65535) identifying the sending and receiving process; the IP address plus port is a **socket**.

| Range | Name | Use |
|---|---|---|
| 0 to 1023 | **Well-known** (system) ports | Standard services (HTTP 80, HTTPS 443, SSH 22 ...); binding usually needs privilege |
| 1024 to 49151 | **Registered** ports | Vendor-registered applications |
| 49152 to 65535 | **Dynamic / ephemeral** (private) ports | Chosen by the client for the source side of a connection |

A client picks an ephemeral source port and connects to the service's well-known destination port. Firewalls filter on these numbers, which is why services are sometimes moved to non-standard ports (obscurity, not a real control) and why malware tunnels over 80/443.

## Analyzing Network Traffic

A **protocol analyzer** or **sniffer** (Wireshark, tcpdump) captures frames and decodes them layer by layer, which is exactly de-encapsulation performed by a tool. Capturing all traffic requires a NIC in **promiscuous mode** and a vantage point that sees the traffic: a hub, a **SPAN / mirror port** on a switch, or a **network tap**. On a switched network an attacker who cannot get a mirror port resorts to ARP poisoning or MAC flooding to see other hosts' traffic (see [[IP, ICMP, and ARP]]).

Uses: troubleshooting, intrusion detection, forensic capture of an incident, and verifying that a protocol really is encrypted. Risk: anything not encrypted (Telnet, FTP, HTTP, SNMPv1/2 community strings) is readable in a capture, so the same tool serves the attacker. Captured traffic is sensitive data and should be handled accordingly.

## Key Points

- **TCP/IP has four layers: application, transport, internet, link.** The suite was built for interoperability, and security is bolted on.
- **TCP: connection-oriented, reliable, three-way handshake (SYN, SYN/ACK, ACK), flags.** UDP: connectionless, best-effort, easily spoofed.
- **Well-known ports are 0 to 1023; ephemeral ports are chosen by the client.**
- **SYN floods abuse the handshake; reflection attacks abuse UDP's lack of one.**
- **Sniffing needs promiscuous mode plus a vantage point (hub, mirror port, tap)**; on a switched network it needs ARP poisoning first.
