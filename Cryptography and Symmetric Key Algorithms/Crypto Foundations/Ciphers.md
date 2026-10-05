Classic ciphers predate computers but illustrate the substitution and transposition building blocks every modern cipher still relies on (see Core Crypto Concepts).

## Caesar Cipher

A simple **substitution** cipher: shift every letter in the plaintext by a fixed number of positions in the alphabet (e.g., shift of 3: A→D, B→E). The "key" is just the shift amount — only 25 possible values, so it's trivially broken by brute force. Historically significant as the earliest named cipher, not as a serious security control.

## Vigenère Cipher

A **polyalphabetic substitution** cipher — instead of one fixed shift, it uses a repeating keyword to pick a different shift for each letter, cycling through the keyword letter by letter. This defeats simple frequency analysis (which breaks the Caesar cipher easily), since the same plaintext letter can map to different ciphertext letters depending on its position. Still breakable once the keyword length is discovered, but a meaningful step up in strength.

## Running Key Cipher

A variant that uses a very long key — traditionally a passage from a book — agreed on in advance by sender and receiver, instead of a short repeating keyword. Because the key is as long as (or longer than) the message and doesn't repeat in a short cycle, it resists the frequency-analysis attacks that break the Vigenère cipher.

## Concealment and Steganography

A different approach entirely: instead of scrambling the message (encryption), **hide the fact that a message exists at all**.

- **Concealment cipher** — the real message is hidden within an innocuous-looking cover message, readable only if you know the rule (e.g., "read every 5th word").
- **Steganography** — hiding data inside another file, most commonly an image, audio, or video file, by embedding it in redundant or low-order bits that don't visibly change the cover file.
- Key distinction from encryption: encryption makes a message unreadable but obviously present; steganography/concealment tries to make the message invisible in the first place. The two are complementary — a hidden message can also be encrypted for defense in depth.
