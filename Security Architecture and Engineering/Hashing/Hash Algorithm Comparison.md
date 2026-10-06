## Comparison Table

| Algorithm | Digest size | Status |
|---|---|---|
| MD5 | 128 bits | Broken — practical collision attacks exist |
| SHA-1 | 160 bits | Deprecated — practical collision attacks exist |
| SHA-2 family (SHA-256, SHA-384, SHA-512) | 256–512 bits | Current standard |
| SHA-3 | 224–512 bits (selectable) | Current standard, structurally independent backup to SHA-2 |
| RIPEMD-160 | 160 bits | Legacy, not broken, rarely the default choice |

## SHA Family

The **Secure Hash Algorithm** family, developed by NIST, is the current standard:

- **SHA-1** — 160-bit digest. Deprecated: practical collision attacks have been demonstrated, so it should not be used for new security purposes, even though it's still found in legacy systems.
- **SHA-2** — the current standard family (SHA-256, SHA-384, SHA-512, named for digest size). No practical collision attacks known; this is the default choice for integrity, signatures, and certificates today.
- **SHA-3** — standardized later, built on a structurally different internal design (a sponge construction, not the Merkle–Damgård structure SHA-1/SHA-2 share). It exists as a backup standard — if a structural weakness were ever found in SHA-2's design, SHA-3 wouldn't share it, since it's built differently from the ground up.

## MD5

Produces a 128-bit digest. Once ubiquitous, now **broken** — practical collision attacks mean an attacker can craft two different inputs with the same MD5 digest, defeating any integrity check that relies on it (see Collisions in Hashing Algorithms). It should never be used for security purposes (signatures, certificates, password hashing); it's still occasionally seen for non-security checksums (e.g., verifying a download wasn't corrupted by accident, not tampered with by an attacker), where collision resistance against a deliberate adversary doesn't matter.

## RIPEMD

Developed in Europe as an independent alternative to the NSA-developed SHA family. **RIPEMD-160** (160-bit digest) is the common variant — not broken, but never saw the widespread adoption SHA did, so it shows up far less in practice. Worth recognizing by name as a non-US-designed alternative, more than as an active default choice.

## Takeaway: What's Safe to Use Today

- **Use:** SHA-2 (or SHA-3 where a structurally independent option is wanted).
- **Broken, do not use for security purposes:** MD5.
- **Deprecated, do not use for new systems:** SHA-1.
- **Legacy, technically unbroken but rarely the default:** RIPEMD-160.
