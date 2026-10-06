## The Hard Problem

ElGamal's security rests on the **discrete logarithm problem**: in modular arithmetic, computing a modular exponentiation is fast, but working backward to find the exponent from the result is computationally infeasible at sufficient size — the same underlying hard problem Diffie-Hellman key exchange relies on (see Diffie-Hellman Key Exchange).

## What It's Used For

Unlike RSA, which can do both encryption and signatures, ElGamal is primarily used for **encryption** built directly on a Diffie-Hellman-style key agreement — a shared value is derived, then used to mask the plaintext. A signature variant exists (ElGamal signatures), but it's far less commonly deployed than its encryption use, and less common overall than RSA or ECC.

## Trade-off

ElGamal ciphertext is roughly double the size of the plaintext (a structural consequence of the algorithm, not a flaw) — one reason it's seen less in bandwidth-sensitive deployments compared to RSA or ECC, despite being conceptually sound and unbroken.
