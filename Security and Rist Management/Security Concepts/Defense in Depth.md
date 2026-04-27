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

The underlying philosophy is **assume breach**: design each inner layer as if all outer layers have already failed. This is why no single layer is trusted to hold on its own. See [[CIA Triad]] for the security objectives each layer protects, and [[AAA Framework]] for the identity controls embedded within the layers.

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

## Control Types

Defense in Depth is not only about *where* controls sit (layers) but also *what* they do. A well-designed strategy mixes all types across all layers so that gaps in one type are covered by another.

**By function:**

| Type | Purpose | Example |
|---|---|---|
| **Preventive** | Stops an attack before it happens | Firewall, door lock, access control |
| **Detective** | Identifies an attack in progress or after the fact | IDS, audit logs, security cameras |
| **Corrective** | Restores normal state after an incident | Backups, patching, incident response |
| **Deterrent** | Discourages attacks by raising perceived risk | Visible cameras, warning banners, guards |
| **Compensating** | Alternative control when the primary isn't feasible | Increased monitoring when MFA can't be deployed |

**By category:**

| Category | Description | Example |
|---|---|---|
| **Administrative** | Policies, procedures, training | Acceptable Use Policy, background checks |
| **Technical** | Software and hardware controls | Firewalls, encryption, antivirus |
| **Physical** | Tangible barriers | Fences, locks, server room access controls |

These two dimensions are independent — a security camera is both Physical (category) and Detective (function). A firewall is Technical and Preventive.

## Vendor Diversity

Using the same product at multiple layers creates a hidden single point of failure — one vulnerability in that vendor's software bypasses both. Intentionally mixing vendors across layers ensures that a flaw in one product doesn't silently collapse the whole strategy.