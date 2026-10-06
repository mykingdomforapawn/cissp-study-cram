## What It Solves

Diffie-Hellman isn't an encryption algorithm — it's a **key exchange protocol**. It lets two parties who have never met and share no prior secret derive the *same* shared secret value over a channel an eavesdropper can watch in full, without ever transmitting the secret itself. This is one of the three practical answers to the key distribution problem named in Symmetric Key Management's Key Distribution section, alongside offline distribution and public key encryption.

## How It Works, Conceptually

Both parties publicly agree on some shared starting values, then each combines those public values with their own **private** value to compute a public value they exchange openly. Each side then combines the other party's public value with their own private value — and due to the math involved, both sides land on the identical shared secret, even though an eavesdropper who saw every public value exchanged can't feasibly reconstruct it. The security rests on the same **discrete logarithm problem** ElGamal uses (see ElGamal) — easy to compute forward, infeasible to reverse.

## What It Doesn't Provide

Diffie-Hellman alone gives both parties a shared secret, but it doesn't **authenticate** either party — it's vulnerable to a man-in-the-middle attack where an attacker establishes separate shared secrets with each party and relays/alters traffic between them, with neither side realizing anyone else is involved. In practice, Diffie-Hellman is paired with a separate authentication mechanism (e.g., digital signatures backed by certificates) to close this gap — mechanics of that pairing belong to PKI/TLS handshake coverage.

## Where It's Used

The shared secret produced is typically used as (or to derive) a symmetric session key, feeding directly into the hybrid cryptosystem pattern described in Asymmetric Key Algorithms. ECDH (see Elliptic Curve Cryptography) is the elliptic-curve variant of the same protocol, used throughout modern TLS.
