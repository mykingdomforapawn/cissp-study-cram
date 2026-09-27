Control frameworks provide structured approaches for implementing, measuring, and communicating security controls. They give organizations a common language and a baseline to work from, and they underpin the governance structures in [[Security Governance & Management]] and the audit methods in [[Organizational Security Processes]].

The frameworks below don't form a strict hierarchy — they operate in parallel domains that complement each other: COBIT handles business/governance alignment, ISO/NIST define security standards, and ITIL manages IT operations.

```text 
		  [ COBIT ] <-- Governance (Business Goals) 
			 | 
	[ ISO 27000 / NIST ] <-- Security Standards (The Rules) 
			 | 
	      [ ITIL ] <-- Service Management (The Operations) 
```

**ISO/IEC 27000 Series (The International Standard)**
* Goal: To establish and maintain an Information Security Management System (ISMS). It is the global standard for security.
* Note: It is paid/commercial (you have to buy the PDF) and is very broad/flexible.
* **ISO 27001 vs. 27002**: ISO 27001 defines the *requirements* for an ISMS and is the certifiable standard — organizations get audited and certified against it. ISO 27002 is the code of practice that provides *implementation guidance* for controls. You certify to 27001; you use 27002 as the how-to guide.

**NIST Frameworks (The US Government Standard)**
* **SP 800 Series**: Originally for US federal agencies, now the de-facto standard for detailed technical controls. Public and free. More prescriptive than ISO.
* **Cybersecurity Framework (CSF)**: A separate, higher-level framework organizing security into functions rather than controls. Where SP 800 provides detailed controls, the CSF provides a risk management lifecycle.
	- **CSF 1.1** defines **five** functions: **Identify → Protect → Detect → Respond → Recover**.
	- **CSF 2.0** (2024) adds **Govern** as a sixth, covering risk strategy, policy, and accountability — the things the original five assumed were happening somewhere off to the side.
	- Both numbers are in circulation, and much existing material still describes five. When a source says five, it is describing 1.1. See [[Risk Frameworks]] for the six-function breakdown.

**COBIT (Control Objectives for Information and Related Technologies)**
* Goal: Aligning IT goals with business goals. It is a governance framework, not just a security framework.
* Key Concept: It asks, "Does this IT project actually help the business make money?"
* Note: Used heavily by auditors and for regulatory compliance (SOX).
* **Six key principles** for the governance and management of enterprise IT:
	- **Provide Stakeholder Value** — IT exists to deliver value to those with a stake in the organization
	- **Holistic Approach** — governance covers people, process, and technology together, not technology alone
	- **Dynamic Governance System** — the system adapts as the organization and its environment change
	- **Governance Distinct from Management** — governance sets direction and monitors; management plans and runs. Conflating the two removes the oversight
	- **Tailored to Enterprise Needs** — the framework is adapted to the organization rather than adopted wholesale
	- **End-to-End Governance System** — covers all information and technology, not just the IT department

**ITIL (Information Technology Infrastructure Library)**
* Goal: Managing IT as a "Service" (IT Service Management - ITSM). It focuses on quality and customer satisfaction.
* Key Concept: Focuses on processes like **Change Management**, **Incident Management**, and **Problem Management**.
* Note: Security is just one part of ITIL (Service Design); the main focus is keeping IT operations running smoothly.

**PCI DSS (Payment Card Industry Data Security Standard)**
* Goal: Protecting cardholder data — credit and debit card information — wherever it is stored, processed, or transmitted.
* Note: Unlike the frameworks above, PCI DSS is not a government standard or an international body's publication. It is imposed contractually by the payment card brands, and compliance is a condition of being allowed to process card payments.
* Key Concept: This makes it prescriptive where ISO and COBIT are flexible. It specifies requirements rather than objectives, and non-compliance carries commercial consequences (fines, increased transaction fees, loss of processing rights) rather than regulatory ones.
* It is the clearest example of an **industry-imposed** framework, as distinct from a voluntary standard or a legal requirement.