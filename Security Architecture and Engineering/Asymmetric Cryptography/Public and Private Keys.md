## The Key Pair

Asymmetric crypto generates a mathematically linked pair at once — a **public key** and a **private key** — rather than a single shared secret (see Symmetric vs. Asymmetric Key Use in Cryptographic Keys for the contrast). The link is one-directional in practice: the public key can be derived from the private key, but not the reverse, because doing so would require solving a computationally hard problem (see Why It's Slow in Asymmetric Key Algorithms).

- **Public key** — distributed freely, published, handed to anyone. Used to encrypt a message *for* the key owner, or to verify a signature *made by* the key owner.
- **Private key** — never leaves the owner's possession or control. Used to decrypt messages encrypted with the matching public key, or to create a digital signature.

## Why the Pairing Works Both Ways

The same key pair supports two distinct operations, depending on which key is used for which step (see Two Use Modes in Asymmetric Key Algorithms for the full breakdown):

- Encrypt with the **public** key → only the **private** key decrypts it → confidentiality.
- Sign with the **private** key → the **public** key verifies it → authentication and non-repudiation.

Mixing these up is a common point of confusion: encrypting with your *own* private key doesn't provide confidentiality (anyone with your public key, which is everyone, could decrypt it) — it provides proof of origin, since only you could have produced it.

## Key Pair Generation

Each algorithm (RSA, ElGamal, ECC — covered in their own notes) has its own mathematical method for generating a linked pair, but the generation always has to produce a public key from which the private key is computationally infeasible to recover, at the key length chosen. Generation itself relies on the same randomness requirements as any other key (see Key Creation in Symmetric Key Management) — a flawed random number generator that produces predictable private keys defeats the whole pair, regardless of key length.
