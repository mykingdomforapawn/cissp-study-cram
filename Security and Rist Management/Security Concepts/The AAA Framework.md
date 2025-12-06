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
- **Authorization (Defining Permissions)**
	* Goal: Determining exactly what the authenticated user is allowed to do.
	* Mechanism: Access Control Lists (ACLs), Group Policies, file permissions (Read/Write).
	* Example: The system checks John's profile and sees he is an "Editor." He is allowed to *write* new articles but is denied permission to *delete* the website database.
- **Auditing (Recording Events)**
	* Goal: Capturing a detailed trail of events for security analysis and non-repudiation. It focuses on "what happened."
	* Mechanism: Security event logs, syslog, error logs, camera footage.
	* Example: The server records a specific log entry: *"User 'John' deleted file 'report.pdf' at 10:42 AM from IP address 192.168.1.5."*
- - **Accounting (Accountability)**
	* Goal: Reviewing the logs to check for compliance violations to hold subjects accountable.
	* Mechanism: SIEM (Security Information and Event Management), log analysis tools, forensic audits.
	* Example: After a data breach, a security officer reviews the audit trail to prove that a specific employee accessed the confidential files at 2 AM, linking the action directly to their identity.