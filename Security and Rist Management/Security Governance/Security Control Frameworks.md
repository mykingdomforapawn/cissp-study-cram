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
* **Cybersecurity Framework (CSF)**: A separate, higher-level framework organizing security into five functions: **Identify → Protect → Detect → Respond → Recover**. Where SP 800 provides detailed controls, the CSF provides a risk management lifecycle. Both are from NIST; both are tested as distinct frameworks.

**COBIT (Control Objectives for Information and Related Technologies)**
* Goal: Aligning IT goals with business goals. It is a governance framework, not just a security framework.
* Key Concept: It asks, "Does this IT project actually help the business make money?"
* Note: Used heavily by auditors and for regulatory compliance (SOX).

**ITIL (Information Technology Infrastructure Library)**
* Goal: Managing IT as a "Service" (IT Service Management - ITSM). It focuses on quality and customer satisfaction.
* Key Concept: Focuses on processes like **Change Management**, **Incident Management**, and **Problem Management**.
* Note: Security is just one part of ITIL (Service Design); the main focus is keeping IT operations running smoothly.