How roles are structured and managed is itself a governance control. See [[Security Governance & Management]] for the planning and policy context these roles operate within.

**Senior Manager (The Ultimate Responsibility)** 
* Goal: Bears the final responsibility for all security incidents and the protection of the organization's assets. 
* Key Task: Signing off on security policies, approving budgets, and accepting risk (Risk Acceptance). 
* Note: They can delegate the *work*, but they cannot delegate the *liability*. 

**Security Professional (The Advisor)** 
* Goal: Designing, implementing, and managing the security controls. 
* Key Task: Writing policies (for management to sign), configuring firewalls, incident response. 
* Note: They are the functional experts, but they do not "own" the risk—management does. 
 
**Asset Owner (The Classifier)** 
* Goal: The individual (usually a business unit manager) who is ultimately responsible for a specific subset of data or system.
* Key Task: Determining the data classification (e.g., "Top Secret" vs. "Public") and deciding who gets access (permissions).
* Note: They decide *what* needs to be protected and *how* sensitive it is.

**Custodian (The Implementer)** 
* Goal: The technical hands-on person who manages the data on behalf of the Asset Owner. 
* Key Task: performing backups, patching systems, implementing the access controls defined by the Owner. 
* Note: If the Owner is the "Architect," the Custodian is the "Builder/Maintenance Crew."

**User (The Operator)** 
* Goal: Any individual who accesses data or systems to perform their job duties. 
* Key Task: Following policies, using strong passwords, not sharing credentials, reporting suspicious activity. 
* Note: They are the "front line" and often the weakest link in security. 

**Auditor (The Validator)** 
* Goal: providing an independent assessment of the security controls to ensure compliance. 
* Key Task: Reviewing logs, checking policy adherence, reporting findings to Senior Management. 
* Note: Auditors must be independent to avoid conflicts of interest (they should not check their own work).

## Personnel Governance Controls

How roles are assigned and rotated is a governance mechanism in itself — these controls prevent fraud, limit abuse, and reduce over-reliance on individuals. They are mandated at the governance level (see [[Security Governance & Management]]) and enforced through HR and management processes.

- **Separation of Duties**: No single person controls an entire sensitive process end-to-end. Critical tasks are split across multiple roles so that fraud or error requires collusion. Example: the person who initiates a wire transfer cannot also be the one who approves it.

- **Job Rotation**: Employees periodically move between roles. This exposes any irregularities that relied on one person's continuous presence to stay hidden, and cross-trains staff as a secondary benefit. Example: rotating who manages the backup system reveals if someone has been quietly deleting logs.

- **Mandatory Vacation**: Employees are required to take leave and a colleague temporarily covers their duties. Fraud that requires daily intervention to conceal — such as skimming from accounts — surfaces during the absence. Example: a financial controller taking forced leave reveals discrepancies a substitute notices immediately.