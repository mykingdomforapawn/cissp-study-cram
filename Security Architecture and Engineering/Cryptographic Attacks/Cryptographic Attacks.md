## General Attack Categories

- **Brute force** — trying every key in the keyspace until one works. See Key Space and Brute Force in Core Crypto Concepts for why key length is the main defense.
- **Analytic** — exploiting a weakness in the algorithm's own mathematical structure, rather than just trying keys blindly (e.g., the collision attacks that broke MD5 and SHA-1 — see Hash Algorithm Comparison).
- **Implementation** — exploiting a bug or flaw in *how* crypto was coded or deployed (e.g., a flawed random number generator, a reused IV, improper padding checks), not a weakness in the algorithm itself. A mathematically sound algorithm can still be broken in practice through a bad implementation.
- **Statistical** — exploiting detectable patterns or bias in an algorithm's output that a truly random process wouldn't produce, to narrow down the key or recover plaintext.
- **Fault injection** — deliberately inducing a hardware fault (voltage glitches, temperature extremes, laser pulses) during a cryptographic operation to cause it to leak key material or produce exploitable incorrect output. Primarily relevant against hardware implementations (smart cards, HSMs — see Asymmetric Key Management).
- **Side-channel** — exploiting physical information leaked during a cryptographic operation (power consumption, electromagnetic emissions, even sound) rather than attacking the math or the ciphertext directly.
- **Timing** — a specific side-channel attack: measuring how long an operation takes to execute, since execution time can vary based on the key or data being processed, leaking information bit by bit.
- **Rainbow tables** — precomputed tables mapping common inputs to their hash outputs, letting an attacker reverse a stolen hash by lookup instead of brute force. See Salting in Hashing Algorithms for why a per-password salt defeats this.
- **Frequency analysis** — exploiting the predictable frequency of letters/patterns in natural language to break simple substitution ciphers. See the Vigenère Cipher in Ciphers for how a polyalphabetic cipher resists this.

## Attack Models by Attacker Access

These describe what the attacker has access to, in increasing order of how much that gives them to work with:

- **Ciphertext-only** — the attacker only has intercepted ciphertext, nothing else. The weakest position to attack from.
- **Known-plaintext** — the attacker has one or more matched plaintext/ciphertext pairs (e.g., a known file format header), and tries to use that to deduce the key.
- **Chosen-plaintext** — the attacker can get the target system to encrypt plaintext of their own choosing and observe the resulting ciphertext, then use that to probe the algorithm's behavior.
- **Chosen-ciphertext** — the attacker can get the target system to decrypt ciphertext of their own choosing and observe the resulting plaintext — the strongest position, since the attacker controls input on both sides of the operation.

## Protocol-Level Attacks

- **Meet-in-the-middle** — attacks a cipher applied multiple times in sequence (e.g., double encryption) by working forward from the plaintext and backward from the ciphertext simultaneously, meeting in the middle — this is why naive double-DES offered far less than double the expected security, and why 3DES's effective strength is weaker than its nominal key length suggests (see 3DES in Symmetric Algorithm Comparison).
- **Man-in-the-middle** — an attacker secretly relays and potentially alters communication between two parties who believe they're communicating directly with each other. This is exactly the gap Diffie-Hellman alone doesn't close (see Diffie-Hellman in Asymmetric Algorithm Comparison) — unauthenticated key exchange is vulnerable unless paired with a separate authentication mechanism.
- **Replay** — capturing a legitimate message (or an entire exchange) and resending it later to trick a system into repeating an action (e.g., resending a captured authentication exchange). See Nonce in Crypto Mathematics for the standard defense: a non-repeating value per message that lets the receiver reject anything already seen.

## Salting, Revisited

Rainbow tables above are the attack; **salting** (see Salting in Hashing Algorithms) is the standard mitigation — forcing an attacker to redo the precomputation work per password instead of reusing one universal table.
