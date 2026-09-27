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

## Third-Party Governance

**Third-party governance** is the system of external oversight applied to an organization — or applied by an organization to its own suppliers. The obligation to submit to it can come from law, regulation, industry standards, contractual terms, or licensing conditions. The method varies, but it generally involves an outside investigator or auditor, and the assessment methods above are how it is carried out in practice.

The direction matters. An organization is simultaneously the subject of third-party governance (its regulators and customers oversee it) and the party exercising it (it oversees its own vendors). The same instruments — documentation review, on-site assessment, audit — apply in both directions.

### Authorization to Operate

An **authorization to operate (ATO)** is formal permission for a system or a supplier to be used in a given environment, granted on the strength of evidence that security requirements are met. It is most familiar from government and military contexts but the concept generalizes to any organization that gates a supplier before use.

The consequence worth understanding: **failing to provide sufficient documentation to meet third-party governance requirements can cost an ATO.** Where a review finds a supplier no longer meeting the minimum requirements its authorization was granted against, withdrawing that authorization is the response the situation calls for — writing a report records the finding but leaves an inadequately secured supplier in production. Documentation is not a formality here; it is the evidence the authorization rests on, and an authorization without evidence has nothing holding it up.

Where the organization sets minimum security requirements for a third party, those requirements are modeled on its **own existing security policy** — the operating principle being that a party handling your data should be held to at least the standard you hold yourself to. An audit or scan of the vendor reveals their current state, which is a different question from what they ought to meet.
