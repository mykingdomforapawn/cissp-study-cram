These three concepts of the triad form the **security objective**. If any one of these pillars is breached, the system is considered insecure. It helps security professionals prioritize what they need to protect based on the specific needs of the data.

```text
		 Confidentiality
			 /    \
			/      \
		   /        \
		  /          \
	Integrity ---- Availability
```

- **Confidentiality (Privacy)**
	* Goal: Ensuring that sensitive information is disclosed only to authorized individuals.
	* Mechanism: Encryption, passwords, two-factor authentication. 
	* Example: Only you can see your balance in the bank account. A stranger looking at the network traffic sees only encrypted gibberish, not your account number.
- **Integrity (Accuracy)**
	* Goal: Ensuring that data is accurate, reliable, and has not been altered by unauthorized people (or by accident). 
	* Mechanism: File permissions, version control, checksums/hashing.
	* Example: When you transfer $50, the system deducts exactly $50. It doesn't accidentally change to $500 or $5 due to a glitch or a hacker.
- **Availability (Access)**
	* Goal: Ensuring that authorized users have access to the information and resources when they need them.
	* Mechanism: Backups, redundancy (backup servers), protection against Denial of Service (DoS) attacks.
	* Example: When you open the app on payday to pay your rent, the banking server is online and lets you log in immediately.

While the CIA triad represents the security goals, the DAD triad represents the **failures** or the objectives of an attacker. If you fail to maintain CIA, you usually result in DAD (Disclosure, Alteration, and Destruction). It is the **Anti-Model** to the CIA Triad and the two models map directly to one another. Security professionals implement CIA to prevent DAD.

```text
			Disclosure 
			  /    \
			 /      \
		    /        \
		   /          \
	Alteration ---- Destruction
```

- **Confidentiality** prevents **Disclosure**.
- **Integrity** prevents **Alteration**. Integrity also underpins **non-repudiation** — ensuring a party cannot deny an action they performed (e.g., digital signatures). See threat modeling for full coverage.
- **Availability** prevents **Destruction**.

## Context-Dependent Prioritization

Different domains weight the triad differently — which pillar dominates depends on the context:

| Domain | Top priority | Reasoning |
|---|---|---|
| Military / intelligence | Confidentiality | Disclosure of secrets causes the greatest harm |
| Financial systems | Integrity | Altered transaction data is catastrophic |
| Emergency services / healthcare | Availability | Systems must be reachable when lives depend on it |

## Trade-offs Between Pillars

Strengthening one pillar can weaken another:

- **Confidentiality vs. Availability**: Heavy encryption and strict access controls slow down or block access, reducing availability.
- **Integrity vs. Availability**: Checksums, approval workflows, and write locks protect integrity but add latency and friction.
- **Availability vs. Confidentiality**: Replication and redundancy (more copies in more places) increase the attack surface for disclosure.

Security professionals don't maximize all three simultaneously — they balance them based on the asset's business context.