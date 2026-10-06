## Why Quantum Computing Threatens Crypto

Classical computers attack cryptography through brute force or by exploiting weaknesses in an algorithm's math — both bounded by conventional compute limits (see Work Function in Crypto Mathematics). Quantum computers use fundamentally different computation (qubits, superposition) that makes certain specific hard-math problems — the ones most of today's asymmetric crypto relies on — solvable in practical time, not just faster.

## The Two Relevant Algorithms

- **Shor's algorithm** — efficiently factors large numbers and solves discrete logarithm problems on a sufficiently large quantum computer. This directly breaks RSA (factoring), Diffie-Hellman and ElGamal (discrete logs), and ECC (elliptic curve discrete logs) — see Asymmetric Algorithm Comparison.
- **Grover's algorithm** — provides a quadratic speedup for brute-forcing symmetric keys and hash functions, not an outright break. A 128-bit AES key's effective strength drops to roughly 64 bits against a quantum attacker — serious, but fixed simply by doubling key length, unlike the asymmetric case.

## The Practical Takeaway

Quantum computing is an **asymmetric-crypto-breaking** threat more than a symmetric-crypto-breaking one: RSA, Diffie-Hellman, ElGamal, and ECC are all built on the two problems Shor's algorithm solves, while AES just needs longer keys to stay ahead of Grover's algorithm. This asymmetry is exactly why post-quantum efforts (below) focus on replacing asymmetric algorithms specifically.

## Current State

Large-scale, fault-tolerant quantum computers capable of running Shor's algorithm against real-world key sizes don't exist yet — this is a forward-looking risk, not a present break. The exam-relevant point is the *why* (which problems quantum computing solves and which algorithms that endangers), not a specific timeline.

## Post-Quantum Cryptography

A new generation of asymmetric algorithms designed to resist attack by both classical *and* quantum computers — specifically, algorithms that don't rely on factoring or discrete logarithms. This is the practical response to RSA, Diffie-Hellman, ElGamal, and ECC all being vulnerable to a sufficiently capable quantum computer.

Even though large-scale quantum computers don't exist yet, migration is already underway because of **"harvest now, decrypt later"**: an adversary can capture and store encrypted traffic today, then decrypt it retroactively once quantum computing matures. Data that needs to stay confidential for years is already at risk under today's asymmetric algorithms, which is why standardization and migration started well ahead of the quantum threat actually materializing.

This is a direct, concrete instance of the crypto-agility principle described in Symmetric Key Management: systems designed to swap algorithms without a full redesign will migrate to post-quantum algorithms far more easily than systems with RSA or ECC hardcoded throughout.

Standardization is underway (e.g., NIST has been selecting and publishing post-quantum algorithm standards); naming specific algorithms is beyond what the exam tests. The exam-relevant point is recognizing the term, understanding why it exists, and the harvest-now-decrypt-later urgency — not implementation details.
