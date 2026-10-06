## What Hashing Is

A **one-way function** (see One-Way Functions in Crypto Mathematics) that takes an input of any length and produces a fixed-length output, called a **digest** or **hash value**. Unlike encryption, hashing has no key and no reverse operation — there's no way to reconstruct the input from the digest.

## Properties of a Good Hash

- **One-way** — computationally infeasible to reverse the digest back into the original input.
- **Deterministic** — the same input always produces the same digest, every time.
- **Collision-resistant** — infeasible to find two *different* inputs that produce the same digest.
- **Avalanche effect** — changing even one bit of input should produce a drastically different digest (see Avalanche Effect in Core Crypto Concepts).

## What Hashing Provides (and Doesn't)

Hashing provides **integrity**, not confidentiality — see the Goals of Cryptography comparison table. A digest proves data hasn't changed; it doesn't hide the data's content, and it can't be "decrypted" back to the original, because there's no key and no reverse function to run.

## Collisions

A **collision** is when two different inputs produce the same hash digest — a direct violation of collision resistance. Collisions matter because they let an attacker substitute a malicious file or message for a legitimate one while keeping the same digest, defeating any integrity check that relies on comparing hashes. An algorithm with known, practical collision attacks is no longer trustworthy for integrity verification.

## Common Algorithms (Named Only)

- **MD5** — produces a 128-bit digest; broken, practical collision attacks exist. Should not be used for security purposes.
- **SHA-1** — produces a 160-bit digest; deprecated, practical collision attacks exist.
- **SHA-2 family** (SHA-256, SHA-512, etc.) — current standard, no practical collision attacks known.

Full mechanics of each are deferred to the PKI chapter.

## Salting

For password hashing specifically, a random value (the **salt**) is appended to the password before hashing, and stored alongside the resulting digest. This defeats precomputation attacks (e.g., rainbow tables): without a salt, an attacker can hash every entry in a dictionary once and match it against any stolen hash database; with a unique salt per password, the attacker has to redo that work for every single password, making bulk cracking impractical. This is distinct from plain data-integrity hashing (e.g., verifying a downloaded file), where there's no secret to protect and no need for a salt.
