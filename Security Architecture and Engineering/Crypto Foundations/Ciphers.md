Classic ciphers predate computers but illustrate the substitution and transposition building blocks every modern cipher still relies on (see Core Crypto Concepts).

## Codes vs. Ciphers

- **Code** — operates on *meaning*: whole words or phrases map to other words or phrases (e.g., "Attack at dawn" → "Blue Jay"). Requires a shared codebook, doesn't scale, and can't represent arbitrary messages that aren't already in the book.
- **Cipher** — operates on *individual characters or bits*, regardless of meaning. Any message can be enciphered, which is why every modern cryptosystem is built on ciphers, not codes.

## Substitution Ciphers

Replace each plaintext element with something else, without reordering it (see Substitution vs. Transposition in Core Crypto Concepts for the abstract operation).

### Caesar Cipher

A simple **substitution** cipher: shift every letter in the plaintext by a fixed number of positions in the alphabet (e.g., shift of 3: A→D, B→E). The "key" is just the shift amount — only 25 possible values, so it's trivially broken by brute force. Historically significant as the earliest named cipher, not as a serious security control.

### Vigenère Cipher

A **polyalphabetic substitution** cipher — instead of one fixed shift, it uses a repeating keyword to pick a different shift for each letter, cycling through the keyword letter by letter. This defeats simple frequency analysis (which breaks the Caesar cipher easily), since the same plaintext letter can map to different ciphertext letters depending on its position. Still breakable once the keyword length is discovered, but a meaningful step up in strength.

### Running Key Cipher

A variant that uses a very long key — traditionally a passage from a book — agreed on in advance by sender and receiver, instead of a short repeating keyword. Because the key is as long as (or longer than) the message and doesn't repeat in a short cycle, it resists the frequency-analysis attacks that break the Vigenère cipher.

## Transposition Ciphers

Rearrange the order of plaintext elements without changing the elements themselves (see Substitution vs. Transposition in Core Crypto Concepts). Example: a **rail fence cipher** writes the plaintext in a zigzag across multiple rows, then reads off each row in sequence to produce the ciphertext — the letters are unchanged, only their order is scrambled.

## One-Time Pad

A cipher that is **mathematically proven unbreakable** when used correctly — the only such cipher. It XORs the plaintext with a key that meets four strict requirements:

- The key is **truly random** (not algorithmically generated).
- The key is **at least as long as the message**.
- The key is **used exactly once**, then destroyed.
- The key is **kept completely secret**, known only to sender and receiver.

Break any one of these requirements and the "unbreakable" guarantee disappears. In practice, generating and securely distributing a truly random, message-length key for every communication is impractical at scale — which is why one-time pads see niche use (e.g., historically for diplomatic/intelligence channels) rather than everyday crypto.

## Block vs. Stream Ciphers

- **Block cipher** — encrypts fixed-size chunks of plaintext (e.g., 128 bits) at a time, padding the last block if needed.
- **Stream cipher** — encrypts data one bit or byte at a time, typically by XORing it with a generated keystream (conceptually similar to a one-time pad, but the keystream is algorithmically generated rather than truly random).

This is a foundational distinction for symmetric algorithms — see Block Ciphers and Modes of Operation for the detailed mechanics.

## Concealment, Steganography, and Watermarking

A different approach entirely: instead of scrambling the message (encryption), **hide the fact that a message exists at all** — or, with watermarking, hide a mark whose presence is secondary to proving ownership.

- **Concealment cipher** — the real message is hidden within an innocuous-looking cover message, readable only if you know the rule (e.g., "read every 5th word").
- **Steganography** — hiding data inside another file, most commonly an image, audio, or video file, by embedding it in redundant or low-order bits that don't visibly change the cover file.
- **Digital watermarking** — a related but distinct goal: embedding identifying information (e.g., an owner's mark) into a file, not to hide a secret message, but to prove ownership or detect unauthorized copies/tampering later. Unlike steganography, a watermark doesn't need to stay perfectly invisible — some watermarks are deliberately visible as a deterrent — and it's expected to survive the file being copied, compressed, or edited, which steganographic payloads generally aren't designed to withstand.
- Key distinction from encryption: encryption makes a message unreadable but obviously present; steganography/concealment tries to make the message invisible in the first place. The two are complementary — a hidden message can also be encrypted for defense in depth.
