## Block Ciphers, Recap

Block ciphers encrypt fixed-size chunks of plaintext at a time (see Block vs. Stream Ciphers in Ciphers). Everything below is about how those fixed-size blocks get chained together across a whole message — which is what a **mode of operation** defines.

## Block Size and Padding

A block cipher only operates on complete blocks of a fixed size (e.g., 128 bits for AES). Real messages are rarely an exact multiple of the block size, so the last block is **padded** — filled out with extra bytes following an agreed-upon scheme — before encryption, and the padding is stripped back off after decryption.

## Why Modes of Operation Exist

Encrypting every block independently with the same key has a critical weakness: **identical plaintext blocks produce identical ciphertext blocks.** An attacker who sees repeated ciphertext patterns can infer structure in the plaintext without ever breaking the key. Modes of operation define how blocks are linked together (typically by mixing in the previous block's output, or a counter) so that identical plaintext blocks no longer produce identical ciphertext.

## ECB (Electronic Codebook)

The naive mode: each block is encrypted independently, with no chaining at all. It's the one mode that still exhibits the pattern-leakage problem above — the classic illustration is encrypting an image in ECB and still being able to make out the original shapes in the ciphertext, because repeated pixel patterns map to repeated ciphertext blocks. **ECB should never be used** for anything beyond a single, short, random block.

## CBC (Cipher Block Chaining)

Each plaintext block is XORed with the *previous ciphertext block* before being encrypted. The first block has no predecessor, so it's XORed with a random **IV (initialization vector)** instead.

- Fixes the ECB pattern-leakage problem — identical plaintext blocks now produce different ciphertext, because each one is chained to whatever came before.
- Was the historical default mode for many years.
- Downsides: a single bit error in one ciphertext block corrupts that block and the next one on decryption (error propagation), and encryption can't be parallelized since each block depends on the previous one's output.

## CFB and OFB (Feedback Modes)

Both turn a block cipher into a **stream cipher** by generating a keystream and XORing it with the plaintext, rather than encrypting the plaintext directly.

- **CFB (Cipher Feedback)** — feeds the *previous ciphertext* back into the cipher to generate the next keystream block. Like CBC, an error in one block propagates into the next.
- **OFB (Output Feedback)** — feeds the *cipher's own output* (not the ciphertext) back in to generate the next keystream block, independent of the ciphertext. This avoids error propagation — a corrupted ciphertext bit only corrupts the corresponding plaintext bit, nothing beyond it.

## CTR (Counter)

Encrypts a **counter value** (a nonce combined with an incrementing number) instead of chaining to any previous block, then XORs the result with the plaintext — conceptually similar to OFB, but the keystream for any block can be computed independently just by knowing its counter value.

- Fully **parallelizable** for both encryption and decryption, since no block depends on another.
- No error propagation — a corrupted ciphertext bit only affects the corresponding plaintext bit.
- The modern default: underlies authenticated modes like AES-GCM used throughout current protocols (e.g., TLS).

## Why Authenticity Matters Beyond Confidentiality

ECB through CTR above only provide **confidentiality** — they say nothing about whether the ciphertext was tampered with in transit. An attacker who can't read the plaintext can often still flip bits in the ciphertext and have the recipient decrypt it into corrupted (or deliberately manipulated) plaintext without detection. **Authenticated encryption** modes close that gap by producing an authentication tag alongside the ciphertext, checked on decryption before the plaintext is trusted.

## GCM (Galois/Counter Mode)

Combines CTR mode's keystream generation with a Galois-field-based authentication tag, computed over the ciphertext in the same pass as encryption. Provides **confidentiality and data authenticity/integrity together**, with CTR's full parallelizability. This is the modern default for authenticated encryption — e.g., AES-GCM underlies TLS.

## CCM (Counter with CBC-MAC)

Combines CTR mode for confidentiality with **CBC-MAC** (a MAC built from CBC mode) for authenticity — two passes over the data instead of GCM's one, so it's slower, but it's used where GCM isn't available or standardized, such as some wireless and IoT protocols (e.g., WPA2's CCMP).

## Comparison

| Mode | Parallelizable | Error propagation | Authenticity | Typical use |
|---|---|---|---|---|
| ECB | Yes | No (errors stay in-block) | No | Never — insecure, leaks patterns |
| CBC | No (encryption); yes (decryption) | Yes, into the next block | No | Legacy default |
| CFB | No (encryption); yes (decryption) | Yes, into the next block | No | Legacy, stream-like use |
| OFB | No | No | No | Legacy, error-sensitive channels |
| CTR | Yes | No | No | Confidentiality-only baseline |
| GCM | Yes | No | Yes | Modern default (e.g., AES-GCM in TLS) |
| CCM | No | No | Yes | Where GCM isn't available (e.g., WPA2/CCMP) |
