## Key Creation

A key is only as strong as how it's generated: it must be **randomly generated** (see Boolean Math/One-Way Functions and Key Space and Brute Force) so it draws unpredictably from the full keyspace. A key derived from a weak source — a password, a predictable seed — undermines the keyspace regardless of its stated length.

## Key Distribution

The structural problem described in Symmetric Key Algorithms: both parties need the same key before they have a secure channel to send it over. In practice this is solved one of two ways:

- **Out-of-band delivery** — physically or separately transmitting the key outside the channel it will protect (e.g., in person, via a separate courier).
- **Key wrapping with asymmetric crypto** — encrypting the symmetric key with the recipient's public key before sending it, the same hybrid cryptosystem pattern described in Asymmetric Key Algorithms.

## Key Storage

A key must never be stored alongside the data it protects — if both are compromised together, the encryption provides no protection at all. Keys should be:

- Access-controlled separately from the protected data, following least privilege.
- Where possible, protected by dedicated hardware (a hardware security module, or HSM) rather than sitting in general-purpose storage — mechanics of HSMs are covered in later domains.
- Never stored in plaintext in application code, config files, or alongside ciphertext.

## Key Destruction

When a key reaches end of life (planned rotation, or a system being decommissioned), it must be **securely destroyed**, not merely deleted — a deleted key can sometimes be recovered from storage media. This is the basis of **crypto-shredding**: destroying only the key (not the much larger volume of ciphertext it protects) renders all data encrypted under that key permanently unrecoverable, which is a fast, practical way to "delete" encrypted data at scale.

## Key Escrow

A trusted third party holds a copy of a key for authorized recovery later — for business continuity (an employee leaves, a lost key would otherwise make data permanently inaccessible) or for legally compelled access (e.g., law enforcement with a warrant). Escrow is useful but controversial: see Skipjack in Symmetric Algorithm Comparison for the classic cautionary example (the Clipper Chip), where mandated government escrow became the central objection, independent of the cipher's technical soundness.

## Key Recovery

The authorized process of retrieving an escrowed or otherwise lost key — distinct from an attacker "recovering" a key through cracking. To prevent any single person (including an insider) from triggering recovery alone, recovery is typically gated by **split knowledge** / **M of N control** (see Crypto Mathematics): the key is divided among multiple custodians, and a minimum number of them must act together to reconstruct it.
