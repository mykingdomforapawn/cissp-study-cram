## Comparison Table

| Algorithm | Key size | Block size | Rounds | Status |
|---|---|---|---|---|
| DES | 56 bits (effective) | 64 bits | 16 | Broken — brute-forceable |
| 3DES | 112 or 168 bits (effective ~112) | 64 bits | 48 (3×16) | Deprecated |
| IDEA | 128 bits | 64 bits | 8 | Largely superseded |
| Blowfish | 32–448 bits (variable) | 64 bits | 16 | Legacy, still unbroken |
| Skipjack | 80 bits | 64 bits | 32 | Deprecated, escrow controversy |
| RC5 / RC6 | Variable (up to 2048 bits) | Variable (32/64/128 bits) | Variable | Legacy; RC6 was an AES finalist |
| AES | 128, 192, or 256 bits | 128 bits | 10, 12, or 14 (by key size) | Current standard |

## DES (Data Encryption Standard)

The first US federal symmetric encryption standard. Uses a 64-bit key, but 8 bits are parity, leaving an **effective 56-bit key** — far too small by modern standards, and brute-forceable since the late 1990s with purpose-built hardware. Historically significant as the first widely standardized cipher; no longer secure for any real use.

## 3DES (Triple DES)

A patch, not a redesign: applies DES three times in an **Encrypt-Decrypt-Encrypt (EDE)** sequence, usually with two or three distinct keys, pushing the effective key strength up toward 112 bits. It extended DES's usable life for years, but is now deprecated — a meet-in-the-middle attack reduces its effective strength well below the nominal key length, and three full passes of an already-slow cipher make it much slower than modern alternatives like AES.

## IDEA (International Data Encryption Algorithm)

A 128-bit-key, 64-bit-block cipher best known for its use in early versions of PGP for email encryption. Never broken in practice, but largely superseded by AES and no longer in common use.

## Blowfish

Designed as a free, unpatented replacement for DES. Uses a variable key length (32–448 bits) and a 64-bit block, and remains unbroken in its full form — but its 64-bit block size is now considered a weakness for high-volume traffic (birthday-bound collision risk). Predecessor to Twofish, which addressed the block size issue but didn't see the same adoption.

## Skipjack

An NSA-designed cipher, notable mainly for its association with the 1990s **Clipper Chip** initiative, which built in a **key escrow** mechanism — a copy of each key held by the government, recoverable with a warrant. The controversy over mandated government access (rather than any cryptographic flaw) is why Skipjack is a recurring exam reference point, more than its technical design.

## Rivest (RC5 / RC6)

RC5 (and its successor RC6) use a variable key size, block size, and number of rounds, making them flexible but also harder to standardize comparisons against. **RC6 was a finalist in the NIST competition that ultimately selected Rijndael (AES)** — it lost on parts of the evaluation criteria, not on being broken.

## AES (Advanced Encryption Standard)

The current US federal and de facto global standard, based on the **Rijndael** cipher. Uses a 128-bit block and a 128, 192, or 256-bit key (with 10, 12, or 14 rounds respectively — more rounds for longer keys). Won the NIST competition for combining strong security margins with high performance in both software and hardware, replacing DES/3DES as the default choice for new systems.

## Takeaway: What's Safe to Use Today

- **Use:** AES (paired with an authenticated mode like GCM — see Block Ciphers and Modes of Operation).
- **Historical / legacy only, do not use for new systems:** DES, 3DES, IDEA, Skipjack.
- **Legacy, technically unbroken but not a modern default:** Blowfish, RC5/RC6.
