## Boolean Math and Logical Operations

Ciphers operate on bits, so the underlying math is boolean logic: AND, OR, NOT, and especially **XOR (exclusive OR)**.

| A | B | XOR |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

XOR is the one that matters most for crypto because it's **reversible with the same key**: `plaintext XOR key = ciphertext`, and `ciphertext XOR key = plaintext` again. This single property is the basis of stream ciphers and the one-time pad.

## Modulo

Modulo (`mod`) returns the remainder of a division — like clock arithmetic, values wrap back around after reaching a fixed range (e.g., `mod 12` never produces a result outside 0–11). Cryptography relies on it to keep computed values inside a fixed-size range, and **modular exponentiation** (raising a number to a power, then taking the result mod a large number) is the mathematical core of asymmetric algorithms like RSA and Diffie-Hellman.

## One-Way Functions

A function that's computationally easy to run forward but computationally infeasible to reverse, even knowing the output. This asymmetry is what hashing and asymmetric crypto are built on:

- Hashing — easy to hash a message, infeasible to reconstruct the message from the hash.
- Asymmetric crypto — easy to compute a public key from a private key (via modular exponentiation), infeasible to go the other way.

## Nonce

A **n**umber used **once** — a value included to make each execution of a protocol or encryption operation unique, even with the same key. It defeats replay attacks, since a captured and resent message carries the old nonce and gets rejected.

- Distinct from an **IV (initialization vector)**: both are "used once," but a nonce doesn't have to be random or secret, just non-repeating for a given key; an IV is usually random and feeds directly into the cipher's chaining (see Block Ciphers and Modes of Operation).

## Zero-Knowledge Proof

A method for proving you know a secret **without revealing the secret itself** or any information that would help derive it. Classic analogy: proving you know the password to a locked door by walking through it and back out through a different, otherwise-inaccessible path — the observer is convinced you have the key, but never sees it.

## Split Knowledge

No single person holds the complete key or secret — it's divided into pieces, and a minimum number of pieces must be combined to reconstruct it. Often implemented as **M of N control**: N people each hold a piece, and any M of them (M ≤ N) must come together to reconstitute the secret. This prevents any one person from being a single point of compromise or failure.

## Work Function (Work Factor)

The estimated time and resources required to break a cryptosystem — typically via brute force. It's the practical yardstick for "how secure is secure enough":

- If the work factor exceeds the useful lifetime of the data being protected (data doesn't need to stay secret longer than it takes to crack it), the cipher is considered adequate.
- Work factor is why key length matters more than almost anything else — see Key Space and Brute Force in Core Crypto Concepts.
- As computing power increases over time, a fixed key length's work factor shrinks — this is why algorithms and key lengths get deprecated (see Cryptographic Lifecycle).
