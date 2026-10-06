## What Asymmetric Crypto Is

A mathematically linked **key pair**: a public key and a private key. What one key encrypts, only the other can decrypt — and critically, the private key can't feasibly be derived from the public one, even though they're mathematically related (see Modulo and One-Way Functions in Crypto Mathematics for why). The public key is shared freely; the private key never leaves its owner. Full depth on the key pair itself, and on specific algorithms, is in Public and Private Keys and the other Asymmetric Cryptography notes.

## Solves the Key Distribution Problem

Unlike symmetric crypto, the public key doesn't need a secure channel to be shared — it's designed to be given out openly. This is the structural fix for the key distribution problem described in Symmetric Key Algorithms: no secret ever has to cross the wire.

## Two Use Modes

- **Encrypt with the recipient's public key** — only the recipient's private key can decrypt it. Provides confidentiality.
- **Sign with your own private key** — anyone can verify the signature using your public key, proving the message came from you and wasn't altered. Provides authentication and non-repudiation (see Goals of Cryptography).

The certificate and trust mechanics behind actually distributing and validating public keys (PKI, certificate authorities) are covered in the PKI notes.

## Why It's Slow

Asymmetric algorithms rely on computationally hard math problems — factoring large prime products, discrete logarithms — rather than the simple bit-level operations (XOR, substitution, transposition) symmetric ciphers use. That math is what makes the private key infeasible to derive from the public key, but it also makes asymmetric crypto orders of magnitude slower than symmetric crypto. It's used for small amounts of data (keys, signatures, handshakes), never for bulk encryption.

## Hybrid Cryptosystems

In practice, almost no real system uses asymmetric crypto alone. Instead:

1. Asymmetric crypto encrypts a small, randomly generated **symmetric session key**.
2. The fast symmetric algorithm encrypts the actual bulk data using that session key.

This combines asymmetric crypto's solution to key distribution with symmetric crypto's speed — this pattern underlies TLS and most other modern secure-communication protocols.

## Common Algorithms

- **RSA** — based on the difficulty of factoring large prime products. See RSA.
- **Diffie-Hellman** — a key *exchange* protocol (not encryption itself), based on discrete logarithms. See Diffie-Hellman Key Exchange.
- **ElGamal** — encryption built on the same discrete logarithm problem as Diffie-Hellman. See ElGamal.
- **ECC (Elliptic Curve Cryptography)** — based on the elliptic curve discrete logarithm problem; achieves equivalent strength to RSA at much shorter key lengths. See Elliptic Curve Cryptography.

Full mechanics of each are in the dedicated Asymmetric Cryptography notes above.

## Post-Quantum Note

RSA, Diffie-Hellman, ElGamal, and ECC all rely on math problems that a sufficiently capable quantum computer could solve efficiently, breaking them outright — see Quantum Computing and Cryptography and Post-Quantum Cryptography for the full treatment.
