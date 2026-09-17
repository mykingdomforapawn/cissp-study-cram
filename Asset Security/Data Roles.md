[[Organizational Roles and Responsibilities]] already defines the generic Asset Owner and Custodian roles. When the asset in question is data specifically, that same set of roles shows up alongside a GDPR-flavored pair with its own legal weight:

- **Data Owner** — the business-side role (usually a manager) accountable for a specific data set: classification, access decisions, and ultimate liability — same role as the generic Asset Owner
- **Data Controller** — the GDPR-specific term for whoever determines *why* and *how* personal data is processed; overlaps with the Owner role but carries its own regulatory accountability independent of internal org-chart titles
- **Data Processor** — processes data on the controller's behalf and instructions, without deciding the purpose
- **Data Custodian** — the technical, hands-on role that implements the Owner/Controller's decisions day to day (backups, access provisioning, patching) — same role as the generic Custodian
- **Data Steward** — manages the day-to-day quality, accuracy, and business definitions of data (naming conventions, metadata, data dictionaries); an operational role, distinct from the security-focused Custodian
- **Data Subject** — the individual the data is about; not a role that handles the data, but the party whose rights (access, correction, deletion) the other roles' obligations exist to protect

Owner and Controller largely describe the same accountability from two angles (general governance vs. GDPR-specific), and the same is true of Custodian and Processor — the terms coexist because different sources/regulations use different vocabulary for the same underlying split between *who decides* and *who executes*.
