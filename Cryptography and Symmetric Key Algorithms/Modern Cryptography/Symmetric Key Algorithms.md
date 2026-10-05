## What Symmetric Crypto Is

A single shared secret key encrypts *and* decrypts — both parties use the exact same key. The main advantage is **speed**: symmetric algorithms are computationally cheap compared to asymmetric ones, which is why they're used for bulk data encryption (see Asymmetric Key Algorithms for the comparison). The trade-off is a set of structural weaknesses that come from both parties needing the same secret.

## Key Distribution Problem

Before two parties can communicate securely, they both need the same key — but they have no secure channel to exchange it over yet. Sending the key in the clear defeats the purpose; this is the chicken-and-egg problem symmetric crypto can't solve on its own. Asymmetric crypto exists in large part to solve exactly this (see Asymmetric Key Algorithms).

## Scalability Problem

Every pair of parties that needs to communicate securely needs its own unique shared key — reusing one key across multiple pairs means anyone who holds it can read everyone else's traffic. For **n** parties who all need to talk to each other pairwise, the number of keys required is:

n(n - 1) / 2

This grows quadratically: 10 parties need 45 keys, 100 parties need 4,950. Symmetric crypto alone doesn't scale to large groups.

## Lack of Non-Repudiation

Because both parties hold the identical key, there's no way to prove which one actually produced a given ciphertext — see Why Non-repudiation Requires Asymmetric Crypto in Goals of Cryptography.

## Key Regeneration

If a shared key is ever compromised, it must be replaced — but the replacement has to reach every party who held the old key, over a secure channel, which reopens the key distribution problem above. The larger the group sharing a key, the more parties need to be reached, compounding the scalability problem too.
