This is a comprehensive strategy that employs a series of layered defense mechanisms to protect data and information. The principle is simple: **redundancy**. If one security control fails, another layer acts as a backup to stop or slow down the attack, ensuring there is no single point of failure.

```text 
		   [ DATA ]
			  || 
		( Application ) 
			  || 
		 ( Endpoint ) 
			  || 
	      ( Network ) 
			  || 
	     ( Perimeter ) 
			  || 
	( Physical / Policies )
```

- **Physical & Administrative Layer (The Foundation)**
	* Goal: Preventing physical theft/access and establishing the rules of behavior.
	* Mechanism: Security guards, fences, ID badges, background checks, Acceptable Use Policies.
	* Example: A policy prohibits employees from writing passwords on sticky notes, and a security guard stops a stranger from walking into the server room.
- **Technical Layer: Network & Perimeter (The Moat)**
	* Goal: Filtering traffic and stopping attacks before they reach internal resources.
	* Mechanism: Firewalls, VPNs, DMZ (Demilitarized Zone), Intrusion Detection Systems (IDS).
	* Example: The corporate firewall identifies a connection attempt coming from a known malicious IP address and blocks it before it touches any computers.
- **Technical Layer: Endpoint, App & Data (The Core)**
	* Goal: Protecting the specific asset and the data itself, assuming the network might already be compromised.
	* Mechanism: Antivirus, patch management, file encryption, Multi-Factor Authentication (MFA).
	* Example: A hacker manages to bypass the firewall, but they cannot read the customer database because the files are encrypted (At Rest) and they don't have the decryption key.