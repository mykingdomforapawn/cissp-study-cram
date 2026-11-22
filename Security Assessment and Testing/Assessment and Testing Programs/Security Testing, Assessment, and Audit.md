Three activities are often used interchangeably in conversation but are distinct: **testing**, **assessment**, and **audit**. They differ in scope, in who performs them, and above all in **who the results are written for**. The methods used to gather evidence are covered in [[Organizational Security Processes]]; this note covers how the three fit together into a program.

## The Three Activities

| | Security Test | Security Assessment | Security Audit |
|---|---|---|---|
| **Question answered** | Does this control work? | Is our security posture adequate? | Can an independent party attest that controls operate as claimed? |
| **Scope** | Narrow — one control or system | Broad — a system, process, or whole organization | Defined by a standard or regulation |
| **Performed by** | Internal staff, often automated and continuous | Internal team or hired consultants | **Auditors independent of the function being examined** |
| **Audience** | The technical team that owns the control | Management | **Third parties** — regulators, customers, the board |
| **Output** | Pass/fail results, findings to remediate | Report with findings **and recommendations** | Formal **opinion** against a standard |

The key distinctions:

- An **assessment includes testing**, but adds analysis and recommendations. A test alone produces data; an assessment produces judgement.
- **An assessment recommends mitigation; it does not perform it.** Vulnerability scanning, risk assessment, and threat assessment are all part of an assessment, and the report ends in recommendations. Actually fixing the findings is remediation work owned by the system owners, and sits outside the assessment.
- An **audit never recommends**. The auditor states whether controls meet the standard; recommending a fix and then auditing it would destroy independence.
- **Independence is what makes an audit an audit.** Internal staff can test and assess their own systems; they cannot credibly audit them.

### Writing the Report

**The assessment report is addressed to management**, which determines how it must be written:

- **Plain language, not technical jargon.** The audience makes resourcing and risk decisions; a report they cannot read produces no decision.
- **Lead with business risk and impact**, with technical detail supporting rather than driving the narrative.
- **Include recommendations** and the relative priority among them, so the reader knows what to act on first.

Detailed technical findings still belong in the report, but as an appendix for the owners who will act on them (see [[Security Process Data and Indicators]] on matching reporting to audience).

## Building a Testing Program

Security testing must be **scheduled by risk, not by convenience**. The factors that set the frequency for a given system:

- **Criticality and sensitivity** — the more valuable the asset, the more often it is tested.
- **Likelihood of technical failure** and **likelihood of attack** — exposed, complex, or frequently changed systems need more attention.
- **Regulatory or contractual requirement** — some cadences are not negotiable (PCI DSS, for example, mandates specific scanning intervals).
- **Difficulty and cost of testing**, and the **disruption** it causes — a full-interruption test of a production system is expensive enough to justify doing it rarely.

A mature program combines **automated testing that runs continuously** with **manual testing done periodically**, and treats the results as a feed into risk management (see [[Risk Assessment]]) rather than as a checklist.

## Reviewing and Acting on Results

Testing is worthless if the findings are not consumed. The program must define:

- **Who reviews results** — technical owners for raw findings, management for trends and exceptions.
- **How findings are prioritized** — by business risk, not by the scanner's severity label alone.
- **What happens when remediation is not possible** — a documented **exception** with compensating controls and an expiry date, approved at the right level (see [[Risk Response]]).
- **Whether the fix worked** — re-testing to validate remediation closes the loop.

Manual review by a knowledgeable person remains necessary because automated tools report what they can measure, not what matters. A scanner cannot tell that a "critical" finding sits on an isolated test box, or that a "low" one is on the system holding all the customer data.

## Key Points

- **A test answers whether a control works; an assessment adds analysis and recommendations for management; an audit produces a formal opinion for a third-party audience.**
- **Auditors must be independent of what they audit, and do not make recommendations — doing so would compromise that independence.**
- **An assessment includes testing; an audit is distinguished by independence and audience, not by technique.**
- **An assessment report recommends mitigation but does not include performing it.**
- **Assessment reports are addressed to management and written in plain language, avoiding technical jargon.**
- **Test frequency is driven by criticality, likelihood of failure or attack, regulatory requirements, and the cost and disruption of testing.**
- **Combine continuous automated testing with periodic manual testing, and always validate that remediation actually worked.**
