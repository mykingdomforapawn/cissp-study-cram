## Why Quantum Computing Threatens Crypto

Classical computers attack cryptography through brute force or by exploiting weaknesses in an algorithm's math — both bounded by conventional compute limits (see Work Function in Crypto Mathematics). Quantum computers use fundamentally different computation (qubits, superposition) that makes certain specific hard-math problems — the ones most of today's asymmetric crypto relies on — solvable in practical time, not just faster.

## The Two Relevant Algorithms

- **Shor's algorithm** — efficiently factors large numbers and solves discrete logarithm problems on a sufficiently large quantum computer. This directly breaks RSA (factoring), Diffie-Hellman and ElGamal (discrete logs), and ECC (elliptic curve discrete logs) — see RSA, Diffie-Hellman Key Exchange, ElGamal, and Elliptic Curve Cryptography.
- **Grover's algorithm** — provides a quadratic speedup for brute-forcing symmetric keys and hash functions, not an outright break. A 128-bit AES key's effective strength drops to roughly 64 bits against a quantum attacker — serious, but fixed simply by doubling key length, unlike the asymmetric case.

## The Practical Takeaway

Quantum computing is an **asymmetric-crypto-breaking** threat more than a symmetric-crypto-breaking one: RSA, Diffie-Hellman, ElGamal, and ECC are all built on the two problems Shor's algorithm solves, while AES just needs longer keys to stay ahead of Grover's algorithm. This asymmetry is exactly why post-quantum cryptography efforts focus on replacing asymmetric algorithms specifically — see Post-Quantum Cryptography.

## Current State

Large-scale, fault-tolerant quantum computers capable of running Shor's algorithm against real-world key sizes don't exist yet — this is a forward-looking risk, not a present break. The exam-relevant point is the *why* (which problems quantum computing solves and which algorithms that endangers), not a specific timeline.
