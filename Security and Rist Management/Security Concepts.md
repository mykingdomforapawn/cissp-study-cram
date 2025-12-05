## The CIA Triad
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