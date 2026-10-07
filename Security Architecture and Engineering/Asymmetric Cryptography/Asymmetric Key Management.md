## HSM (Hardware Security Module)

Dedicated, tamper-resistant hardware that generates, stores, and uses private keys without the key ever leaving the device in plaintext — cryptographic operations (signing, decrypting) happen inside the HSM itself, and only the result comes out. This is the concrete implementation of "protect keys in hardware" referenced in Symmetric Key Management's Key Storage section, and it matters more for asymmetric private keys specifically, since a single compromised private key can undermine an entire chain of trust (see Certificate Authorities in Public Key Infrastructure).

## Separate Key Pairs for Signing vs. Encryption

A private key used for signing shouldn't also be used for encryption, and vice versa. Mixing the two roles weakens both guarantees — among other reasons, it complicates revocation and rollover (below): revoking a compromised key used for both purposes simultaneously breaks decryption of old data *and* invalidates every past signature, where separate key pairs let each be managed independently.

## Private Key Backup — The Asymmetric Exception to Escrow

Whether a private key should be backed up depends entirely on what it's used for:

- An **encryption** private key should be backed up/escrowed — lose it, and every message or file encrypted to the matching public key becomes permanently unreadable. Same motivation as Key Escrow in Symmetric Key Management.
- A **signing** private key should **not** be escrowed or backed up anywhere else. If a copy exists outside the owner's sole control, non-repudiation is gone — you can no longer prove that only the owner could have produced a given signature (see Why Non-repudiation Requires Asymmetric Crypto in Goals of Cryptography).

This split is exactly why separating signing and encryption key pairs (above) matters in practice, not just in theory.

## Key Rollover

When a certificate is renewed, or a key is suspected compromised, the old key pair is retired and a new one generated — see Enrollment and Revocation in Public Key Infrastructure for the certificate-side mechanics this ties into.
