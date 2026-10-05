## Base Vocabulary

- **Plaintext** — the original, readable message.
- **Ciphertext** — the scrambled output after encryption.
- **Algorithm (cipher)** — the mathematical procedure that transforms plaintext to ciphertext and back. It's public, published, and peer-reviewed.
- **Key** — the secret input to the algorithm that determines the specific transformation. It's the only thing that stays hidden.

## Kerckhoffs's Principle

A cryptosystem must remain secure even if everything about it — the algorithm itself — is publicly known, as long as the key stays secret. Security must rest entirely in the key, never in hiding the algorithm.

- **Security through obscurity** (hiding the algorithm instead of protecting the key) is not a valid design. A proprietary, unreviewed algorithm is weaker in practice than a public one, because it hasn't been stress-tested by the cryptographic community.

## Substitution vs. Transposition

The two fundamental operations every cipher builds on:

- **Substitution** — replace each plaintext element with something else (e.g., letter → different letter). See Classic Ciphers (Caesar) for the simplest example.
- **Transposition** — rearrange the order of plaintext elements without changing them.

Modern ciphers combine both repeatedly across multiple rounds — see Block Ciphers and Modes of Operation.

## Confusion and Diffusion

Shannon's two properties a strong cipher must have:

- **Confusion** — the relationship between the key and the ciphertext is as complex and obscure as possible. Changing one bit of the key should change the ciphertext unpredictably.
- **Diffusion** — the influence of a single plaintext bit is spread across many ciphertext bits. Changing one bit of plaintext should affect many parts of the output.

Substitution primarily drives confusion; transposition primarily drives diffusion.

## Key Space and Brute Force

- **Key space** — the total number of possible keys for a given key length (2^n for an n-bit key).
- A **brute-force attack** tries every key in the key space until one works. Doubling the key length doesn't double the work — it squares the key space, making brute force exponentially harder.
- This is why key length is the primary lever for cipher strength, independent of the algorithm's design.

## Avalanche Effect

A desirable property where a tiny change in input — flipping a single plaintext or key bit — cascades into a drastically different ciphertext (ideally ~50% of output bits flip). It's the practical, observable result of good confusion and diffusion: without it, similar inputs would produce similar outputs, leaking structure to an attacker.
