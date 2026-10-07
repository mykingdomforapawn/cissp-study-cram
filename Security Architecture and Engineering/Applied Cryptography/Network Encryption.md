## Circuit Encryption (Link Encryption)

Encrypts an entire communication link (e.g., a dedicated line between two network nodes) rather than individual messages — everything crossing that physical or logical link is protected, including headers and routing information that application-layer encryption (like TLS) typically leaves exposed. The trade-off: each hop along a multi-hop path has to decrypt and re-encrypt the traffic to route it onward, so every intermediate node must be trusted, unlike end-to-end encryption where only the two endpoints hold the key.

## IPsec

A suite of protocols that encrypts and authenticates traffic at the **network layer** (IP itself), rather than at the application layer like TLS — meaning it protects any traffic riding over IP, transparently to the applications using it. Two modes:

- **Transport mode** — encrypts only the payload of each IP packet, leaving the original header intact; used for end-to-end protection between two hosts.
- **Tunnel mode** — encrypts the entire original packet (header included) and wraps it in a new IP header; used for site-to-site VPNs, since it hides the original source/destination from anyone observing the tunnel.

IPsec relies on the same building blocks covered elsewhere: a key exchange (typically Diffie-Hellman, see Asymmetric Algorithm Comparison) to establish a shared secret, then symmetric encryption for the actual traffic — the hybrid cryptosystem pattern again (see Hybrid Cryptosystems in Asymmetric Key Algorithms).
