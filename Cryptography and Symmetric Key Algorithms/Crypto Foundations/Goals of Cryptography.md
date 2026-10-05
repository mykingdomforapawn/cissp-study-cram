Cryptography exists to serve four distinct security goals. Two of them map directly onto the [[CIA Triad]]; the other two are additions the triad doesn't cover on its own.

- **Confidentiality**
	* Goal: Only authorized parties can read the data.
	* Mechanism: Encryption (symmetric or asymmetric) — see the Modern Cryptography notes.
	* Maps to: Confidentiality in the CIA Triad.
- **Integrity**
	* Goal: Data hasn't been altered, accidentally or maliciously, in transit or at rest.
	* Mechanism: Hashing — see Hashing Algorithms.
	* Maps to: Integrity in the CIA Triad.
- **Authentication**
	* Goal: Prove that a party (or a message) really is who/what it claims to be.
	* Mechanism: Digital certificates, message authentication codes (MACs), challenge-response protocols.
	* Not in CIA Triad: authentication is about verifying identity, not about protecting the data itself.
- **Non-repudiation**
	* Goal: A party cannot later deny having sent or signed something.
	* Mechanism: Digital signatures.
	* Not in CIA Triad: closest conceptual link is Integrity (it also prevents a sender from disowning an action), but the triad has no dedicated pillar for it.

## Why Non-repudiation Requires Asymmetric Crypto

This is a frequent exam trap: **symmetric encryption cannot provide non-repudiation.** Both parties hold the *same* shared key, so either one could have produced the ciphertext — there's no way to prove which one did. Only asymmetric crypto can provide non-repudiation, because a private key belongs to exactly one party: if a message verifies against their public key, only they could have signed it.

| Goal | Symmetric crypto | Asymmetric crypto |
|---|---|---|
| Confidentiality | Yes | Yes |
| Integrity (via hashing) | Yes | Yes |
| Authentication | Limited | Yes |
| Non-repudiation | No | Yes |

## Crypto Is One Layer, Not a Silver Bullet

Cryptography delivers these four goals only for the data it actually protects — it says nothing about endpoint security, physical access, or social engineering. It's one control among many in a [[Defense in Depth]] strategy, not a replacement for the rest of the stack.
