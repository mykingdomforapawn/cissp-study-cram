Audits are classified by **who performs them and who they are for**, and the formal reports they produce follow published standards. The methods auditors use to gather evidence are covered in [[Organizational Security Processes]]; the independence requirement is covered in [[Security Testing, Assessment, and Audit]].

## Internal, External, and Third-Party Audits

| Type | Performed by | Primary audience | Independence |
|---|---|---|---|
| **Internal audit** | The organization's own audit staff | Management and the board | Independent of the *function* audited, not of the organization |
| **External audit** | An independent audit firm hired by the organization | The organization, plus regulators and shareholders | Independent of the organization entirely |
| **Third-party audit** | An auditor engaged on behalf of, or at the demand of, an outside party | **That outside party** — a customer, regulator, or partner | Independent, and serving someone other than the audited organization |

The distinction that matters: an **internal audit function reports to the board or audit committee, not to the executives whose areas it audits** — otherwise the people being examined control the examiner. An **external** audit is commissioned by the organization about itself. A **third-party** audit is commissioned by someone who wants assurance *about* the organization, which is why its report carries weight with customers.

Auditing a supplier is part of third-party governance and vendor oversight (see [[Organizational Security Processes]]) and the agreements in [[Vendor, Consultant, and Contractor Agreements]].

## SOC Reports

**Service Organization Control (SOC)** reports are produced under **SSAE 18** in the United States and **ISAE 3402** internationally. They exist so that a service provider can be audited once and share the result, instead of being audited separately by every customer.

| Report | Covers | Who may receive it |
|---|---|---|
| **SOC 1** | Controls over **financial reporting** | Restricted — the customer's auditors |
| **SOC 2** | The five **trust services criteria**: security, availability, processing integrity, confidentiality, privacy | **Restricted** — shared under NDA with customers and prospects |
| **SOC 3** | The same scope as SOC 2, but only a summary opinion with no detail | **Public** — may be posted on a website |

**SOC 2 is the one that matters for security assurance**, and it is confidential. SOC 3 is the version that can be published, precisely because it omits the control detail an attacker would find useful.

## Type I and Type II

**There are only two types of SOC report — Type I and Type II.** "Type III" and "Type IV" do not exist; SOC 3 is a different *report*, not a third type. Both SOC 1 and SOC 2 come in these two types, and the difference between them is **time**:

- **Type I** — the auditor evaluates the **design** of controls at a **single point in time**. It says the controls were suitably designed and in place on that date. It says nothing about whether they worked.
- **Type II** — the auditor tests the **operating effectiveness** of controls **over a period**, typically six to twelve months. It says the controls actually functioned.

**A Type II report is substantially stronger assurance than a Type I**, and is what a customer assessing a critical vendor should ask for. A Type I is often a provider's first report, before enough history exists for a Type II.

## Other Audit Standards

- **ISO 27001** — certification against an information security management system (ISMS) standard; see [[Security Control Frameworks]]. Certification is issued by an accredited body, making it a third-party attestation.
- **ISO 27002** — the control guidance that supports 27001; organizations align to it but are not certified against it.
- **PCI DSS** — assessed by a Qualified Security Assessor (QSA) for large merchants, or via self-assessment questionnaire for smaller ones; see [[Compliance]].
- **COBIT** — the control objectives framework auditors frequently measure IT governance against.

## Key Points

- **Internal auditors must report to the board or audit committee rather than to the management they audit.**
- **A third-party audit is commissioned by an outside party seeking assurance about the organization, which is why its report carries weight with customers.**
- **SOC 1 covers financial reporting controls; SOC 2 covers the five trust services criteria; SOC 3 is the public summary of a SOC 2.**
- **SOC 2 reports are confidential and shared under NDA; SOC 3 is the one that can be posted publicly.**
- **Type I assesses control design at a point in time; Type II assesses operating effectiveness over a period and is far stronger assurance.**
- **Only two types exist — Type I and Type II. Do not confuse the type with the SOC 1/2/3 report number.**
- **SOC reports are produced under SSAE 18 (US) and ISAE 3402 (international).**
