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

**Rollback plan** — not a tier in the hierarchy but frequently listed alongside them: the predefined means of returning to a prior state after a change fails to meet expectations. Where the three plans above look forward, a rollback plan is the prepared retreat, and preparing it is part of authorizing the change rather than a reaction to the failure.

## Business Cases

A **business case** is a documented argument, or stated position, establishing a need to make a decision or take some form of action. Making one means demonstrating a business-specific need to alter an existing process or adopt a particular approach.

Security work is frequently funded this way, and the framing matters: a business case argues from organizational need rather than from technical desirability. "This control closes a known exposure that carries this much risk" is a business case; "this is best practice" is not. It is the mechanism by which a security initiative competes for resources alongside everything else the organization could spend them on, which is also why security that cannot articulate its business case tends not to get funded.

## Risk from Mergers, Acquisitions, and Divestitures

Periods of heavy corporate activity raise an organization's risk level distinctly, because environments built under different assumptions are being joined together or pulled apart at speed. Characteristic risks:

- **Inappropriate information disclosure** — data becomes visible to people in the other organization before anyone has decided it should be
- **Data loss** — records fall between two systems during migration, or are abandoned in an environment nobody retains ownership of
- **Downtime** — integration work touches production systems that were never designed to interoperate
- **Failure to achieve sufficient return on investment** — the security and integration cost of the combination is underestimated in the valuation

Worth distinguishing from these: increased worker compliance is a *precaution* one would want during such a period, not a risk of it, and better insight into insider motivations is a possible *result* of investigating incidents, not a risk either. The distinction is between what the activity exposes the organization to and what the organization might do or learn in response.

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