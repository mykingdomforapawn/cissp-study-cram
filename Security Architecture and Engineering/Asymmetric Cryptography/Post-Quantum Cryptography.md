## What It Is

A new generation of asymmetric algorithms designed to resist attack by both classical *and* quantum computers — specifically, algorithms that don't rely on factoring or discrete logarithms, the two problems Shor's algorithm solves (see Quantum Computing and Cryptography). This is the practical response to RSA, Diffie-Hellman, ElGamal, and ECC all being vulnerable to a sufficiently capable quantum computer.

## Why It Matters Now, Not Later

Even though large-scale quantum computers don't exist yet, post-quantum migration is already underway because of **"harvest now, decrypt later"**: an adversary can capture and store encrypted traffic today, then decrypt it retroactively once quantum computing matures. Data that needs to stay confidential for years (not just until tomorrow) is already at risk under today's asymmetric algorithms, which is why standardization and migration started well ahead of the actual quantum threat materializing.

## Crypto-Agility Connection

This is a direct, concrete instance of the crypto-agility principle described in Symmetric Key Management: systems designed to swap algorithms without a full redesign will migrate to post-quantum algorithms far more easily than systems with RSA or ECC hardcoded throughout.

## Status

Standardization is underway (e.g., NIST has been selecting and publishing post-quantum algorithm standards); naming specific algorithms is beyond what the exam tests. The exam-relevant point is recognizing the term, understanding why it exists (the problems named in Quantum Computing and Cryptography), and the harvest-now-decrypt-later urgency — not implementation details.
