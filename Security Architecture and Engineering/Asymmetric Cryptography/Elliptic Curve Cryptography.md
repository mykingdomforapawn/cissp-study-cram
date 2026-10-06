## The Hard Problem

ECC's security rests on the **elliptic curve discrete logarithm problem**: points on a specially defined elliptic curve can be combined (added) easily, but working backward to find how many times a point was combined with itself to reach a given result is computationally infeasible at sufficient size. It's a harder problem per bit than RSA's factoring or classic discrete logs, which is the whole reason ECC exists.

## Key Length Advantage

ECC achieves equivalent cryptographic strength to RSA at **much shorter key lengths** — roughly a 256-bit ECC key matches the strength of a 3072-bit RSA key (see Key Length and Keyspace in Cryptographic Keys). Shorter keys mean faster computation and less bandwidth/storage overhead, which is why ECC has become the preferred choice for constrained environments — mobile devices, smart cards, IoT.

## What It's Used For

ECC isn't a single algorithm but a mathematical foundation that other algorithms are built on top of: ECDH (elliptic curve Diffie-Hellman, for key exchange) and ECDSA (elliptic curve digital signature algorithm, for signatures) are the common named implementations, paralleling Diffie-Hellman and signature schemes built on classic discrete logs or RSA.

## Status

Not broken by classical computers at current key lengths, but the underlying discrete-log-style problem is one quantum computers would solve efficiently (see Quantum Computing and Cryptography), making ECC — like RSA — a primary candidate for post-quantum replacement.
