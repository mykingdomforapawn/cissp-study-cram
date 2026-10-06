## What a Digital Signature Is

A digital signature combines **hashing** (integrity) with **asymmetric crypto** (authentication and non-repudiation) in one mechanism:

1. The sender hashes the message, producing a digest (see Hashing Algorithms).
2. The sender encrypts *that digest* with their own **private key** — this encrypted digest is the signature, attached to the message.
3. The recipient decrypts the signature with the sender's **public key**, recovering the original digest, and independently hashes the received message themselves.
4. If the two digests match, the message is both unaltered (integrity, from the hash) and provably from the claimed sender (authentication and non-repudiation, since only the sender's private key could have produced a signature that decrypts correctly with their public key).

This is the concrete mechanism behind Sign with your own private key in Asymmetric Key Algorithms' Two Use Modes, and the reason Why Non-repudiation Requires Asymmetric Crypto (Goals of Cryptography) — only a private key, held by exactly one party, can produce the signature.

## HMAC (Hash-based Message Authentication Code)

A lighter-weight alternative when both parties already share a secret key (a symmetric scenario, not asymmetric): HMAC combines a hash function with that **shared secret key**, producing a MAC that proves the message is intact and came from someone who holds the shared key.

- Faster than a full digital signature, since there's no asymmetric math involved.
- **No non-repudiation** — because the key is shared, either party could have produced the MAC, the same structural limitation as symmetric crypto generally (see Lack of Non-Repudiation in Symmetric Key Algorithms). HMAC proves authenticity *between the two key holders*, not to a third party.

## Digital Signature Standard (DSS)

The NIST standard that specifies which algorithms are approved for generating digital signatures — currently DSA, RSA, and ECDSA (see Asymmetric Algorithm Comparison for the algorithms themselves). DSS doesn't introduce new cryptographic math of its own; it standardizes which existing asymmetric algorithms, combined with an approved hash function, are acceptable for producing a valid signature under the standard.
