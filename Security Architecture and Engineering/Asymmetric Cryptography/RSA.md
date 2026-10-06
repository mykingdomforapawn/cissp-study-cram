## The Hard Problem

RSA's security rests on **integer factorization**: multiplying two large prime numbers together is fast, but factoring the resulting product back into those two primes is computationally infeasible at sufficient size. The public key is derived from the product; the private key depends on knowing the original primes — recovering the private key from the public key means solving that factoring problem.

## How the Keys Relate

- The public key is built from the product of two large primes (and a public exponent).
- The private key is built from those same two primes (and a derived private exponent).
- Anyone can verify or encrypt using the public product; only someone who knows the original primes (the private key holder) can efficiently reverse the operation.

Depth beyond this conceptual level (the actual modular exponentiation math) isn't exam-relevant — see Modulo in Crypto Mathematics for the general mechanism RSA relies on.

## Key Length

RSA requires much longer keys than symmetric or ECC algorithms for equivalent strength, because factoring is attacked more efficiently than brute force (see Key Length and Keyspace in Cryptographic Keys for the comparison). 2048-bit RSA keys are the current practical minimum; 1024-bit RSA is considered too weak for modern use.

## Status and Use

The most widely deployed asymmetric algorithm historically — used for key exchange, digital signatures, and certificates throughout PKI. Not broken by classical computers at current key lengths, but factoring is one of the two problems a sufficiently capable quantum computer would solve efficiently (see Quantum Computing and Cryptography), making RSA a primary candidate for post-quantum replacement.
