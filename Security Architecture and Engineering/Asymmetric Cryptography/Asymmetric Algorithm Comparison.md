## Comparison Table

| Algorithm | Hard problem | Provides | Key length vs. equivalent strength | Status |
|---|---|---|---|---|
| RSA | Integer factorization | Encryption, signatures | 2048-bit minimum | Current standard; quantum-vulnerable |
| Diffie-Hellman | Discrete logarithm | Key exchange only (not encryption) | Comparable to RSA at similar bit lengths | Current standard; quantum-vulnerable |
| ElGamal | Discrete logarithm | Encryption (signature variant exists, rarely used) | Comparable to RSA at similar bit lengths | Sound but less deployed; quantum-vulnerable |
| ECC | Elliptic curve discrete logarithm | Encryption (via ECDH), signatures (via ECDSA) | ~256-bit ECC ≈ 3072-bit RSA | Current standard, preferred for constrained devices; quantum-vulnerable |

All four rely on a hard math problem a sufficiently capable quantum computer would solve efficiently — see Quantum Computing and Cryptography.

## RSA

Security rests on **integer factorization**: multiplying two large primes together is fast, but factoring the product back into those primes is computationally infeasible at sufficient size. The public key is built from the product; the private key depends on knowing the original primes. The most widely deployed asymmetric algorithm historically, used for key exchange, digital signatures, and certificates throughout PKI. Requires much longer keys than ECC for equivalent strength, because factoring is attacked more efficiently than brute force (see Key Length and Keyspace in Cryptographic Keys).

## Diffie-Hellman Key Exchange

Not an encryption algorithm — a **key exchange protocol**. It lets two parties who share no prior secret derive the *same* shared secret over a channel an eavesdropper can watch in full, without ever transmitting the secret itself (one of the three practical answers to the key distribution problem named in Symmetric Key Management's Key Distribution section, alongside offline distribution and public key encryption).

Both parties publicly agree on shared starting values, then each combines those with their own **private** value to compute a public value they exchange openly; combining the other party's public value with one's own private value lands both sides on the identical shared secret, even though an eavesdropper who saw every exchanged value can't feasibly reconstruct it. Security rests on the **discrete logarithm problem** — easy to compute forward, infeasible to reverse.

Diffie-Hellman alone doesn't **authenticate** either party — it's vulnerable to a man-in-the-middle attack where an attacker establishes separate shared secrets with each side and relays/alters traffic between them. In practice it's paired with a separate authentication mechanism (e.g., signatures backed by certificates); that pairing belongs to PKI/TLS handshake coverage. The shared secret produced typically becomes (or derives) a symmetric session key, feeding into the hybrid cryptosystem pattern in Asymmetric Key Algorithms. ECDH is the elliptic-curve variant of the same protocol, used throughout modern TLS.

## ElGamal

Also built on the **discrete logarithm problem**. Primarily used for **encryption**, built directly on a Diffie-Hellman-style key agreement — a shared value is derived, then used to mask the plaintext. A signature variant exists but is far less commonly deployed than its encryption use, and ElGamal overall is less common than RSA or ECC. Ciphertext is roughly double the size of the plaintext — a structural consequence of the algorithm, not a flaw, but one reason it's seen less in bandwidth-sensitive deployments.

## Elliptic Curve Cryptography (ECC)

Security rests on the **elliptic curve discrete logarithm problem**: points on a specially defined elliptic curve combine (add) easily, but working backward to find how many times a point was combined with itself to reach a given result is computationally infeasible at sufficient size — a harder problem per bit than RSA's factoring or classic discrete logs, which is why ECC achieves equivalent strength at much shorter key lengths (faster computation, less bandwidth/storage — the reason it's preferred for constrained environments like mobile devices, smart cards, and IoT).

ECC isn't a single algorithm but a mathematical foundation other algorithms build on: **ECDH** (elliptic curve Diffie-Hellman, key exchange) and **ECDSA** (elliptic curve digital signature algorithm, signatures) are the common named implementations.

## Merkle-Hellman Knapsack (Broken, Historical)

An early asymmetric cryptosystem based on the **subset-sum (knapsack) problem** rather than factoring or discrete logs. It's a classic exam distractor precisely because it's **broken** — cryptanalysts found a way to exploit the specific mathematical structure used to hide the "easy" knapsack inside a "hard" one, recovering the private key. Worth recognizing by name as a historical, now-insecure asymmetric algorithm, distinct from RSA/Diffie-Hellman/ElGamal/ECC above, all of which remain secure today.
