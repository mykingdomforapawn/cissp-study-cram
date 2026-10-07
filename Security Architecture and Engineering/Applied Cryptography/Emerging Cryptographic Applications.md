## Blockchain

A distributed, append-only ledger where each block contains a cryptographic hash of the previous block (see Hashing Algorithms), chaining every block to the entire history before it — altering any past block would change its hash, breaking every subsequent link and immediately revealing the tampering. Combined with distribution across many independent nodes (no single party controls the ledger), this is what gives blockchain its tamper-evidence property, without needing hashing alone to "prevent" anything by itself — it just makes tampering detectable.

## Lightweight Cryptography

Algorithms specifically designed for devices with severe constraints on power, memory, and processing — IoT sensors, RFID tags, embedded controllers — where standard algorithms like AES are too computationally expensive to run efficiently. Lightweight crypto trades some performance/security margin for a much smaller footprint, accepting a narrower threat model (e.g., a shorter operational lifespan, lower-value data) in exchange for being usable at all on constrained hardware.

## Homomorphic Encryption

Allows computation to be performed **directly on encrypted data**, producing an encrypted result that, when decrypted, matches the result of performing the same computation on the original plaintext — without ever decrypting the data during processing. This solves the data-in-use confidentiality problem: a third party (e.g., a cloud provider) can run computations on sensitive data without ever having access to the plaintext itself. Still computationally expensive compared to operating on plaintext directly, which limits it to use cases where that data-in-use confidentiality is worth the performance cost.
