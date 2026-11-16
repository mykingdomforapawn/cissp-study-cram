Access control attacks aim at the one thing every other control depends on: the link between a **subject** and the authority it holds. Either steal a legitimate identity, or acquire more authority than the identity should have.

## Risk Elements

An attack only exists where three things meet, and each is a place to intervene:

- **Asset** — what is worth taking. Reducing it is possible: data that is not retained cannot be stolen (see [[Identifying and Classifying Assets]]).
- **Threat** — who would act and how. Rarely removable; it can be deterred and detected.
- **Vulnerability** — the weakness that makes the action work. The element most under the organization's control, and where remediation normally goes.

**Risk = threat × vulnerability against an asset.** Access control reduces risk by removing vulnerabilities (weak credentials, excessive privilege) and limiting what any one compromised identity reaches. The full treatment is in [[Risk Management Concepts]].

## Privilege Escalation

Gaining authority beyond what the compromised account should hold. Usually the second step of an intrusion, after an initial foothold.

- **Vertical escalation** — a normal user acquires administrative rights. Through an unpatched local kernel or service flaw, a misconfigured service running as system, an exposed credential, or a token stolen from memory.
- **Horizontal escalation** — moving sideways into a **different account at the same level** to reach data the original account could not. Common in web applications where an object identifier in a request can simply be changed to another user's.

Defenses: least privilege and separation of administrative accounts from daily-use accounts, prompt patching, removing local administrator rights, and server-side authorization checks on every request rather than only at the interface (see [[Authorization Mechanisms]] on constrained interfaces).

## Password Attacks

| Attack | How it works | What actually stops it |
|---|---|---|
| **Dictionary** | Tries a word list, with common mutations | Breach-list screening, length requirements |
| **Brute force** | Tries the whole keyspace; feasible offline against fast hashes | Length, and a **slow** hash (bcrypt, scrypt, Argon2, PBKDF2) |
| **Hybrid** | A dictionary word plus appended digits or symbols — how people actually build passwords | Same as dictionary; passphrases |
| **Password spraying** | **One** common password tried across **many** accounts, staying under each account's lockout threshold | Detection across accounts, not per account; MFA; breach screening |
| **Credential stuffing** | Username and password pairs from **another site's breach** replayed here, exploiting reuse | MFA, breach-credential monitoring, password managers that make reuse unnecessary |
| **Birthday attack** | Exploits the collision probability in a hash function, so a **collision** is found far faster than a preimage | Long hash outputs and a collision-resistant algorithm |
| **Rainbow table** | Precomputed hash-to-plaintext lookup tables, reversing a stolen hash instantly | A **per-password salt**, which makes any precomputed table useless |

**Spraying is one password against many accounts; stuffing is breached pairs reused against a new site.** That contrast is the one most often tested.

The cryptographic side of these — brute force, birthday, rainbow tables, and salting — is in [[Cryptographic Attacks]] and [[Hashing Algorithms]]. Password policy and storage are in [[Knowledge-Based Authentication]].

### Credential Theft from Memory

Cracking is unnecessary when the credential can be lifted intact.

- **Mimikatz** and comparable tooling read credential material out of memory on a compromised host: plaintext passwords, NTLM hashes, and Kerberos tickets.
- **Pass-the-hash** then authenticates with the **hash itself**, since legacy NTLM authentication proves knowledge of the hash, not of the password. Changing the password invalidates it; nothing else does.
- **Pass-the-ticket** is the Kerberos equivalent, reusing a stolen ticket until it expires. See [[Kerberos]] for the full set of ticket attacks.

Defenses: credential guard and similar memory protections, disabling legacy NTLM, tiered administration so that a high-privilege credential is never typed on a lower-trust machine, and privileged access workstations.

### Running Privileged Commands

Administrators need elevated rights occasionally, and how that elevation is held decides what an attacker inherits:

| Approach | What an attacker who owns the user's session gets | Accountability |
|---|---|---|
| **Standing administrator rights** on the daily account | Everything, immediately | Poor — the account is always privileged |
| **`sudo` / "run as administrator"** from the user's own session | The same elevation, because it runs **in the context of that already-authenticated session** — no separate secret is required | Good — the log names the individual |
| **A separate privileged credential entered on demand** (root password, second admin account) | Nothing extra: the attacker lacks the secret and cannot elevate | Good if the credential is per-person, poor if root is shared |

The exchange is real: **`sudo` gives the better audit trail, a separately-held credential gives the better containment**, and the usual answer is a **separate named administrative account** that gets both — individually attributable and not reachable from a compromised standard session. A shared root password gives containment but destroys accountability, since the log cannot say who used it (see [[AAA Framework]]).

## Sniffing and Spoofing

- **Sniffing** — passive capture of traffic to extract credentials or session tokens. Effective against any protocol that transmits credentials in the clear (Telnet, FTP, plain LDAP, HTTP, PAP). The defense is encryption in transit, not network trust; a switched network is not protection. See [[Wireless Attacks]] and [[Network Attacks]].
- **Spoofing** — falsifying an identity: a source IP or MAC address, a caller ID, an email sender, a wireless access point (the **evil twin**), or a login page in a phishing campaign. Each spoof attacks an identifier that was never designed to be verified.
- **Session hijacking** — taking over an already-authenticated session with a stolen or predicted token, bypassing authentication entirely. See [[Credential and Session Management]].
- **Social engineering and phishing** remain the most productive route to a working credential, because they attack the user rather than the mechanism.

## Core Protection Methods

The defenses that matter, mapped to what they actually prevent:

| Control | Defeats |
|---|---|
| **Multifactor authentication** | Every attack that ends with a working password — spraying, stuffing, phishing, cracking |
| **Strong, salted, slow password hashing** | Offline cracking and rainbow tables after a database theft |
| **Breach-list screening and length requirements** | Dictionary, hybrid, and spraying attacks |
| **Account lockout and cross-account detection** | Online guessing; cross-account detection catches spraying that lockout misses |
| **Least privilege and tiered administration** | Turns a compromised account into a contained one, and limits what escalation yields |
| **Separate named administrative accounts** | Elevation from a compromised standard session, while keeping the audit trail a shared root password would destroy |
| **Encrypting credentials in transit and at rest** | Sniffing and theft of stored secrets |
| **Access reviews and prompt deprovisioning** | Privilege creep and orphaned accounts (see [[Identity and Access Provisioning Lifecycle]]) |
| **Logging and monitoring of authentication events** | Detection — nothing above prevents everything, and the account review depends on the trail |
| **Security awareness training** | Phishing and social engineering, which no technical control fully closes |

The structural point: **prevention is layered because every individual control has a bypass.** MFA is the single highest-value addition, and monitoring is what covers the cases where it fails.

## Key Points

- **Risk is a threat meeting a vulnerability at an asset; vulnerability is the element the organization controls.**
- **Vertical escalation gains higher rights; horizontal escalation moves into another account at the same level.**
- **Password spraying tries one password across many accounts; credential stuffing replays pairs breached elsewhere.**
- **Salting defeats rainbow tables; a slow hash defeats bulk cracking.**
- **Pass-the-hash works because legacy authentication proves knowledge of the hash, so only a password change invalidates it.**
- **`sudo` elevates from the user's existing session, so a compromised session inherits it; a separately-held credential contains that, and a separate named admin account gives both containment and accountability.**
- **Spoofing falsifies an identifier that was never verifiable; sniffing is defeated by encryption, not by network trust.**
- **MFA is the highest-value single control, and monitoring covers what prevention misses.**
