This framework represents the core lifecycle of **Access Control** and **Identity Management**. It is the fundamental mechanism used to secure environments by ensuring that every user is verified, permissions are enforced, and all actions are traceable for accountability.

```text
	Identification (I am User X) 
		  | 
	Authentication (Prove it) 
		  | 
	Authorization (Access Granted) 
		  | 
	  [ Action ] 
		  | 
	   Auditing (Log the details) 
		  | 
	  Accounting (Summarize usage)
```

- **Identification (Claiming Identity)**
	* Goal: Claiming to be an identity when attempting to access a secured system.
	* Mechanism: Usernames, swipe cards, User IDs, account numbers.
	* Example: You enter your email address into the login box. You haven't proved who you are yet; you have only claimed to be that user.
- **Authentication (Proving Identity)**
	* Goal: Verifying that the subject is actually who they claim to be.
	* Mechanism: Passwords (something you know), Tokens (something you have), Biometrics (something you are).
	* Example: You enter your password and use your fingerprint. The system compares this against the database to confirm you are indeed John.
	* **Authentication Factor Types**: Factors are formally classified as Type 1 (something you know — password, PIN), Type 2 (something you have — token, smart card), and Type 3 (something you are — biometrics). **Multi-Factor Authentication (MFA)** requires two or more factors from *different* types. Two passwords is not MFA — a password plus a token is.
	* CIA link: Authentication enforces **Confidentiality** — only verified identities reach protected data. See [[CIA Triad]].
- **Authorization (Defining Permissions)**
	* Goal: Determining exactly what the authenticated user is allowed to do.
	* Mechanism: Access Control Lists (ACLs), Group Policies, file permissions (Read/Write).
	* Example: The system checks John's profile and sees he is an "Editor." He is allowed to *write* new articles but is denied permission to *delete* the website database.
	* **Least Privilege**: Grant only the minimum permissions required to perform a job — nothing more. Limits the damage a compromised or malicious account can cause.
	* **Need-to-Know**: Even with sufficient clearance level, a subject only gets access to the specific data relevant to their current role or task. Clearance grants eligibility; need-to-know grants actual access. Example: two employees with the same security clearance — one works on Project A, one on Project B. Neither can access the other's files.
	* CIA link: Authorization enforces **Confidentiality** (right people, right data) and protects **Availability** by ensuring legitimate users aren't over-restricted. See [[CIA Triad]].
- **Auditing (Recording Events)**
	* Goal: Capturing a detailed trail of events for security analysis and non-repudiation. It focuses on "what happened."
	* Mechanism: Security event logs, syslog, error logs, camera footage.
	* Example: The server records a specific log entry: *"User 'John' deleted file 'report.pdf' at 10:42 AM from IP address 192.168.1.5."*
	* CIA link: Auditing supports **Integrity** by detecting unauthorized changes, and enables **non-repudiation** — a subject cannot deny an action that was logged. See [[CIA Triad]].
- **Accounting (Accountability)**
	* Goal: Reviewing the logs to check for compliance violations to hold subjects accountable.
	* Mechanism: SIEM (Security Information and Event Management), log analysis tools, forensic audits.
	* Example: After a data breach, a security officer reviews the audit trail to prove that a specific employee accessed the confidential files at 2 AM, linking the action directly to their identity.

## AAA Protocols

The AAA framework is implemented in practice through dedicated protocols — covered in detail in the networking chapter. For reference: **RADIUS** handles network access (VPNs, Wi-Fi), while **TACACS+** handles device administration (routers, switches). The key structural difference is that TACACS+ separates Authentication, Authorization, and Accounting into independent steps, whereas RADIUS combines the first two.