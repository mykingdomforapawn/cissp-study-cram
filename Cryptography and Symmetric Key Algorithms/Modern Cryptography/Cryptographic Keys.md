## Key Length and Keyspace

A key's strength comes from its length — see Key Space and Brute Force in Core Crypto Concepts for why doubling key length squares the keyspace rather than doubling it. In practice, "how long is long enough" differs by algorithm family: a 128-bit symmetric key and a 2048-bit RSA key offer roughly comparable real-world strength, because asymmetric algorithms rely on mathematical structure (factoring, discrete logs) that can be attacked more efficiently than brute force — see the Asymmetric Key Algorithms note for why that gap exists.

## Symmetric vs. Asymmetric Key Use

- **Symmetric** — one shared secret key, used for both encryption and decryption. Both parties must already possess the same key.
- **Asymmetric** — a mathematically linked key *pair*: a **public key** (shareable with anyone) and a **private key** (kept secret, never shared). What one key encrypts, only the other can decrypt.

Depth on each is in the dedicated Symmetric Key Algorithms and Asymmetric Key Algorithms notes — this note covers only what's common to keys in general.

## Public vs. Private Key — Baseline Vocabulary

- **Public key** — distributed freely; anyone can use it to encrypt a message for the key owner, or verify a signature made by the key owner.
- **Private key** — never leaves the owner's control; used to decrypt messages encrypted with the matching public key, or to create a digital signature.

## Key Security Principles

Regardless of symmetric or asymmetric, a key is only as good as how it's handled:

- **Randomly generated** — predictable keys (e.g., derived from a weak password or a flawed random number generator) undermine the whole keyspace, no matter how long the key is.
- **As long as practical** — balanced against performance; longer isn't free.
- **Protected at rest and in transit** — a leaked key makes the strongest algorithm irrelevant.
- **Rotated periodically** — limits the damage window if a key is ever compromised, and limits the amount of ciphertext an attacker can collect under a single key.

## Key Clustering

A weakness where two *different* keys, applied to the same plaintext, produce the *same* ciphertext. It's never a design goal — its presence means an attacker who recovers one valid key hasn't actually confirmed it's the *only* key that works, which can undermine confidence in an algorithm's key schedule.
