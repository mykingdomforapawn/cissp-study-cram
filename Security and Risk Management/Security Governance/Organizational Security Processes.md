Organizational security processes are the formal activities used to evaluate, verify, and maintain an organization's security posture. They exist to confirm that controls defined in [[Security Governance & Management]] and [[Security Control Frameworks]] are actually working as intended.

A key distinction:
- **Assessment** — evaluates whether controls are effective; typically collaborative, may be internal or external
- **Audit** — formal, independent examination for compliance; the auditor has no stake in the outcome

## Due Diligence and Due Care

Two concepts that define legal and ethical responsibility in security:

- **Due Diligence** — investigating and understanding risk; knowing what you *should* do. Example: a company reviews its software inventory and identifies unpatched systems.
- **Due Care** — actually implementing controls to address known risks; *doing* what you should do. Example: the company applies the patches.

Failing due care after due diligence is legal negligence. An organization that identified a vulnerability but took no action is liable when a breach results. The two always appear as a pair — diligence without care is just awareness of a problem you ignored.

## Assessment and Audit Methods

- **On-Site Assessment**
	* Goal: Directly observe how security policies are implemented in practice.
	* Mechanism: Visit the site, interview personnel, observe operating routines.
	* Example: An auditor walks the server room to verify that physical access controls match what the policy documents describe.

- **Document Exchange and Review**
	* Goal: Evaluate the processes by which data is handled and shared.
	* Mechanism: Review data flow documentation, data exchange agreements, and existing assessment records.
	* Example: A reviewer examines how customer data is transferred to a third-party processor to check for compliance with data handling policies.

- **Process/Policy Review**
	* Goal: Verify that written policies are complete, current, and enforceable.
	* Mechanism: Review policy documents, procedures, and standards against a compliance framework.
	* Example: A security officer reviews the Acceptable Use Policy to confirm it covers cloud storage — a gap introduced since the last revision.

- **Third-Party Audit**
	* Goal: Obtain an unbiased evaluation of the security infrastructure from an independent party.
	* Mechanism: External auditor with no stake in the outcome examines controls against a defined standard (e.g., ISO 27001, SOC 2).
	* Example: An external firm audits a SaaS company's controls and issues a SOC 2 report that customers can rely on as independent evidence of security practices.

## Vulnerability Assessment vs. Penetration Testing

Two related but distinct processes — covered in detail in the assessment chapter. For reference:
- **Vulnerability Assessment** — identifies and catalogs weaknesses without exploiting them; answers "what could be attacked?"
- **Penetration Testing** — actively exploits vulnerabilities to prove real-world impact; answers "what can actually be breached?"

A vulnerability assessment tells you the door is unlocked. A penetration test walks through it.
