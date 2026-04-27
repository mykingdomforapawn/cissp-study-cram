Governance is the oversight that ensures security strategies align with business goals. It moves from high-level visions down to daily tasks. Security must support the organization's mission, not obstruct it. The roles responsible for executing governance are covered in [[Organizational Roles and Responsibilities]], the processes used to verify it in [[Organizational Security Processes]], and the frameworks it aligns with in [[Security Control Frameworks]].

**Risk Appetite** is the amount of risk an organization is willing to accept in pursuit of its goals. It is set by senior management at the strategic level and acts as the boundary within which all tactical and operational decisions must stay — controls are designed to bring risk *down to* the appetite, not necessarily to zero.

```text
	[ Strategic Plan ] (The "Vision" - Long Term) 
		   | 
		   v 
	[ Tactical Plan ] (The "Project" - Mid Term) 
		   | 
		   v 
   [ Operational Plan ] (The "Daily" - Short Term)
```

- **Strategic Plan (The "Vision")** 
	* Definition: A high-level document defining the organization's long-term security goals and risk appetite. It aligns security with business objectives. 
	* Timeframe: Long-term (3 to 5 years). 
	* Responsibility: Senior Management, Board of Directors, C-Level Executives. 
- **Tactical Plan (The "Project")** 
	* Definition: Specific initiatives and projects designed to implement the strategic goals. It bridges the gap between the broad vision and daily work. 
	* Timeframe: Mid-term (6 to 18 months).
	* Responsibility: Middle Management (e.g., Security Managers, Project Managers). 
- **Operational Plan (The "Daily")** 
	* Definition: Detailed, step-by-step procedures and tasks required to maintain security controls and keep systems running. 
	* Timeframe: Short-term (Daily, Weekly, Monthly). 
	* Responsibility: Operational Staff (e.g., SysAdmins, Security Analysts, Help Desk).

## Policy Hierarchy

Governance produces a cascade of documents, each more specific than the last. The levels map directly onto the planning tiers above:

| Document | Mandatory? | Planning Level | Example |
|---|---|---|---|
| **Policy** | Yes | Strategic | "All sensitive data must be encrypted." |
| **Standard** | Yes | Tactical | "AES-256 must be used for data at rest." |
| **Baseline** | Yes | Tactical | "All Windows workstations must have BitLocker, antivirus, and auto-updates enabled." |
| **Guideline** | No | Tactical | "Consider using a password manager." |
| **Procedure / SOP** | Yes | Operational | Step-by-step instructions for encrypting a laptop before travel. |

The key distinctions: policies state *what* must be achieved; standards define *how* to measure compliance; baselines define the *minimum security configuration* for a specific platform or system type — the floor every deployment must meet; guidelines offer *recommended* approaches; procedures (also called SOPs — Standard Operating Procedures) describe *exactly how* to carry out a task. Guidelines are the only non-mandatory level.