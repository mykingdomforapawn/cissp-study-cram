---
tags:
  - anki
---
Anki cards for the Security Governance notes. Format: `Cards/CLAUDE.md`.

---

## Card 1

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
A board asks the CISO to formally assume accountability for all information security risk, so that executives are shielded from liability following a breach. The CISO objects that the arrangement misrepresents how accountability works. Which statement <b>BEST</b> describes the problem?

**Options**
*Senior management may delegate the execution of security work but remains accountable for the outcome — liability for protecting organizational assets cannot be transferred downward.
The CISO lacks the authority over budget and staffing needed to manage all security risk — an authority gap, not the reason the arrangement fails.
Risk ownership belongs to the asset owner rather than to any executive — asset owners classify their data, but overall accountability still rests with senior management.
An external auditor must approve any transfer of risk ownership — auditors validate controls independently and play no part in assigning accountability.

**Source**
[[Organizational Roles and Responsibilities]]

## Card 2

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
A business unit deploys a new customer analytics platform. The database team asks who should decide whether the datasets it holds are labelled Internal or Confidential, and who should configure the resulting access restrictions. Which assignment is correct?

**Options**
*The business unit manager who owns the data determines the classification, and the database team implements the access controls as custodian — owners decide sensitivity, custodians execute.
The database team determines both the classification and the access controls — custodians implement decisions rather than making classification decisions.
The CISO determines the classification and the business unit implements the controls — security advises on the classification scheme but does not own individual datasets.
The platform's users determine classification based on how sensitive the data feels in practice — users follow policy and hold no classification authority.

**Source**
[[Organizational Roles and Responsibilities]]

## Card 3

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
To reduce cost, a company proposes that the same security engineer who designed and deployed its logging infrastructure also perform the annual internal audit of logging controls. What is the <b>PRIMARY</b> objection?

**Options**
*The engineer would be assessing their own work, which removes the independence an audit depends on — an auditor must have no stake in the outcome.
The engineer may not hold a formal audit qualification — a competence concern, but not the fundamental conflict.
An internal audit can never substitute for a third-party audit — internal audit is a legitimate function; independence within it is what matters here.
Findings would have to be reported to the engineer's own manager — reporting lines matter, but they are not what creates the conflict.

**Source**
[[Organizational Roles and Responsibilities]]

## Card 4

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
A company wants an internationally recognized certification showing that its information security management system meets a defined standard, so enterprise customers can rely on it during procurement. Which standard should the organization be certified <b>AGAINST</b>?

**Options**
*ISO/IEC 27001 — defines the requirements for an ISMS and is the certifiable standard in the series.
ISO/IEC 27002 — a code of practice giving implementation guidance for controls; organizations are not certified against it.
NIST SP 800-53 — a detailed US federal control catalogue rather than an international certification scheme.
COBIT — a governance framework for aligning IT with business goals, not an ISMS certification.

**Source**
[[Security Control Frameworks]]

## Card 5

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
A CIO is repeatedly asked by the board to demonstrate that IT investments actually advance business objectives, and needs a framework that auditors will also recognize for regulatory reporting. Which framework fits <b>BEST</b>?

**Options**
*COBIT — a governance framework built around aligning IT goals with business goals, and widely used by auditors and for compliance reporting.
ITIL — addresses IT service management and operational process quality rather than investment-to-business alignment.
ISO/IEC 27001 — establishes an information security management system, a narrower scope than overall IT governance.
NIST CSF — organizes cybersecurity outcomes and does not address IT investment justification.

**Source**
[[Security Control Frameworks]]

## Card 6

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
An organization suffers repeated outages caused by uncoordinated production changes. Leadership wants to adopt a recognized framework covering change, incident, and problem management. Which is <b>MOST</b> appropriate?

**Options**
*ITIL — an IT service management framework whose core processes include change, incident, and problem management.
NIST CSF — organizes security outcomes across its functions and is not a service management framework.
COBIT — governs IT-to-business alignment at a level above operational process design.
ISO/IEC 27002 — provides implementation guidance for security controls rather than IT operations processes.

**Source**
[[Security Control Frameworks]]

## Card 7

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
A security team has published the rule "all sensitive data must be encrypted." Engineering teams keep selecting different algorithms and key lengths. The team wants to remove that discretion without rewriting the original rule. Which document should they issue?

**Options**
*A standard — mandatory, and specifies how compliance is measured, such as requiring AES-256 for data at rest.
A guideline — a recommendation only, which cannot remove discretion.
A procedure — gives step-by-step instructions for carrying out a task rather than setting the mandatory technical requirement.
A revised policy — policies state what must be achieved; embedding algorithm choices at that level is the wrong altitude and ages badly.

**Source**
[[Security Governance & Management]]

## Card 8

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
Before any Windows workstation is issued, it must have full-disk encryption, endpoint protection, and automatic updates enabled. Which type of governance document defines this minimum required configuration?

**Options**
*A baseline — defines the minimum mandatory security configuration for a specific platform or system type.
A standard — mandates how a requirement is met, but the platform-specific configuration floor is specifically a baseline.
A guideline — non-mandatory advice, which cannot establish a required floor.
A policy — states the strategic requirement rather than the platform-specific configuration.

**Source**
[[Security Governance & Management]]

## Card 9

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
A security manager is asked to produce a document covering the next twelve months of security projects, translating the board's multi-year vision into funded initiatives. Which planning tier is this, and who normally owns it?

**Options**
*A tactical plan owned by middle management — mid-term initiatives bridging the strategic vision and daily operations.
A strategic plan owned by senior management — strategic plans span three to five years and set risk appetite rather than project schedules.
An operational plan owned by operational staff — operational plans cover daily, weekly, and monthly activity.
A procedure owned by the security team — procedures describe how to carry out a specific task.

**Source**
[[Security Governance & Management]]

## Card 10

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
An internal review eighteen months ago identified an unpatched internet-facing server and formally documented the risk. Remediation was never funded. That server is now the entry point for a breach. Which characterization is <b>MOST</b> accurate?

**Options**
*The organization exercised due diligence but failed due care, which constitutes negligence — the risk was known and nothing was done about it.
The organization failed due diligence because it did not detect the breach — due diligence concerns identifying and understanding risk, which did happen.
Both due diligence and due care were satisfied, because the risk was formally documented — documentation without remediation does not satisfy due care.
Neither concept applies, because no regulation required patching that server — due care is a general standard of conduct, not solely a regulatory obligation.

**Source**
[[Organizational Security Processes]]

## Card 11

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
A SaaS provider is repeatedly asked by enterprise prospects for independent evidence that its security controls operate effectively. Its internal security team already performs thorough annual control assessments. What should the provider do <b>NEXT</b>?

**Options**
*Engage an independent external firm to audit the controls against a recognized standard and issue a report customers can rely on — independence is exactly what internal assessment cannot supply.
Expand the scope and rigour of the internal assessment and share those results — more rigour does not create the independence the prospects are asking for.
Publish the organization's security policies and standards to the prospects — documents describe intent, not verified operating effectiveness.
Commission a penetration test and share the report — proves the exploitability of specific weaknesses, not the effectiveness of the control set.

**Source**
[[Organizational Security Processes]]

## Card 12

**Domain**
1 — Security and Risk Management / Security Governance

**Question**
Management wants to know which weaknesses exist across the whole estate, with the broadest possible coverage and no risk of disrupting production systems. Which activity is <b>MOST</b> appropriate?

**Options**
*A vulnerability assessment — identifies and catalogues weaknesses across a wide scope without exploiting them.
A penetration test — actively exploits weaknesses to demonstrate impact, with narrower scope and a real risk of disruption.
A third-party audit — evaluates compliance of controls against a standard rather than enumerating technical weaknesses.
An on-site assessment — observes how policies are implemented in practice rather than cataloguing technical vulnerabilities.

**Source**
[[Organizational Security Processes]]
