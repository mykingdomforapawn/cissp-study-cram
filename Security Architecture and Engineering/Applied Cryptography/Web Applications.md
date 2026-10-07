## SSL and TLS

**SSL (Secure Sockets Layer)** and its successor **TLS (Transport Layer Security)** protect web traffic in transit, using the hybrid cryptosystem pattern end to end:

1. A handshake establishes a shared symmetric session key, typically via (elliptic-curve) Diffie-Hellman (see Diffie-Hellman in Asymmetric Algorithm Comparison), with the server authenticated by a certificate (see Public Key Infrastructure).
2. The actual traffic is then encrypted with that symmetric session key, usually under an authenticated mode like AES-GCM (see Block Ciphers and Modes of Operation).

SSL itself is obsolete and insecure — "SSL" in casual conversation almost always actually means TLS today, which has gone through several versions as weaknesses in earlier ones were found. Ephemeral key exchange (see Ephemeral Keys in Asymmetric Key Algorithms) is what gives modern TLS forward secrecy: compromising the server's long-term private key doesn't expose past session traffic, since each session's symmetric key was unique and discarded.

HTTPS (HTTP over TLS) runs over **TCP port 443**, distinct from unencrypted HTTP's port 80.

## Tor and the Dark Web

**Tor (The Onion Router)** provides anonymity rather than just confidentiality: traffic is wrapped in multiple layers of encryption and routed through a chain of volunteer-run relays, with each relay only able to decrypt (peel off) one layer — learning the previous and next hop, but never the full path from source to destination. This is **onion routing**, and it's a distinct goal from TLS: TLS protects *what* is being said from an eavesdropper, while Tor protects *who is talking to whom* from any single observer along the path.

The **dark web** refers to content only reachable through a network like Tor (not indexed by standard search engines, not reachable with a regular browser and a normal URL). Its anonymity properties enable legitimate uses (whistleblowing, privacy under oppressive regimes, censorship circumvention) alongside illicit ones — the technology itself is neutral; the exam-relevant point is understanding the anonymity mechanism, not judging its uses.
