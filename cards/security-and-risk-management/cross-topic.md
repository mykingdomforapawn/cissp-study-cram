---
tags:
  - anki
---
Cards that span two or more Security and Risk Management notes. The exam's
harder items rarely test one concept in isolation — these require combining
them. Format: `cards/CLAUDE.md`.

---

## Card 1

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
After treatment, residual risk on a critical system remains above the documented risk appetite. The business will not fund further controls this financial year. The CISO is asked to sign the acceptance so the project can close. What should happen <b>FIRST</b>?

**Options**
*Escalate for a senior management acceptance decision — residual risk above appetite is a business decision, and accountability for accepting it cannot be delegated to the CISO.
Have the CISO sign the acceptance and record it in the risk register — records the decision at the wrong level of authority.
Reclassify the risk as within appetite to reflect the funding reality — adjusts the measurement to fit the decision rather than the reverse.
Implement the cheapest available control to bring residual risk down — acts before establishing whether the business accepts the exposure at all.

**Source**
[[Risk Response]], [[Organizational Roles and Responsibilities]]

## Card 2

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
A quantitative analysis shows a proposed safeguard has positive value, and it is approved and deployed. A follow-up assessment finds residual risk is still above appetite. What does this indicate?

**Options**
*The safeguard was individually cost-effective but insufficient — a positive cost-benefit result says nothing about whether the remaining exposure is acceptable, so further treatment is required.
The original quantitative analysis must have been wrong — the analysis answered a different question, namely whether that control was worth its cost.
Risk appetite should be raised to reflect what the organization can actually afford — appetite reflects business objectives and is not adjusted to ratify a shortfall.
The residual risk should now be accepted, since the cost-effective option has been taken — acceptance is only valid when residual risk falls within appetite.

**Source**
[[Risk Assessment]], [[Risk Response]]

## Card 3

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
An organization purchases cyber insurance covering breach costs and regulatory fines. A regulator subsequently asks what steps the organization took to protect the data before the incident. What is the <b>MOST</b> important point for the organization to understand?

**Options**
*Transferring financial consequence does not discharge the obligation to exercise due care — the regulator is asking whether known risks were acted upon, which insurance does not answer.
The insurance policy is sufficient evidence that the risk was formally managed — a policy demonstrates a treatment decision, not that controls were implemented.
Due diligence is satisfied because the organization assessed the risk before buying cover — assessing risk is diligence; the regulator's question concerns care.
Regulatory fines covered by insurance fall outside the scope of the regulator's inquiry — coverage of a penalty has no bearing on whether conduct was negligent.

**Source**
[[Risk Response]], [[Organizational Security Processes]]

## Card 4

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
A manufacturing control system is past end of secure life and cannot be replaced for two years. Security proposes segmentation, enhanced monitoring, and restricted access. Which combination correctly describes what has been done, and what still remains?

**Options**
*Compensating controls have been applied as mitigation — the remaining residual risk must still be formally accepted by an accountable owner and reviewed periodically.
Compensating controls have been applied, which constitutes avoidance of the legacy risk — avoidance would mean eliminating the system or the activity entirely.
The risk has been transferred to the operations team that runs the system — transfer moves financial consequence to a third party; assigning operational duty is not transfer.
Preventive controls have been applied and the risk is now fully mitigated — no control set reduces risk to zero, and the residual position still needs an owner.

**Source**
[[Legacy Risk]], [[Security Controls]], [[Risk Response]]

## Card 5

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
A legacy application cannot support MFA. The security team deploys session monitoring and jump-host access, then documents the arrangement. An architect argues the application is now adequately protected. Which principle <b>BEST</b> challenges that conclusion?

**Options**
*Assume breach — each remaining layer should be designed as though the compensating controls have already been bypassed, so the data itself still needs its own protection.
Least privilege — relevant to how much access is granted, but it does not address whether the layering is sufficient.
Separation of duties — concerns splitting a process across people and has no bearing on the adequacy of these controls.
Vendor diversity — addresses shared flaws across products at different layers, which is not what is at issue.

**Source**
[[Defense in Depth]], [[Security Controls]]

## Card 6

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
Threat modelling of a new service identifies that users can perform high-value actions the system cannot later attribute to them. Which STRIDE category, security property, and AAA step form the correct chain?

**Options**
*Repudiation, countered by non-repudiation, supported through auditing — attributable logging is what prevents a subject denying an action.
Spoofing, countered by authentication, supported through identification — spoofing concerns impersonating an identity, not denying an action.
Tampering, countered by integrity, supported through authorization — tampering is unauthorized modification of data.
Information disclosure, countered by confidentiality, supported through authentication — disclosure concerns exposure of data rather than attribution of actions.

**Source**
[[Threat Modeling]], [[AAA Framework]], [[CIA Triad]]

## Card 7

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
An organization's policy states that sensitive data must be encrypted. No standard or baseline was ever issued, teams implemented it inconsistently, and an auditor now raises a finding. Which characterization is <b>MOST</b> accurate?

**Options**
*The governance cascade is incomplete — a mandatory policy with no standard or baseline beneath it leaves the requirement unmeasurable and unenforceable in practice.
The policy itself is defective and should be rewritten to name specific algorithms — policies state what must be achieved; technical specifics belong in a standard.
The teams are non-compliant and should face disciplinary action — enforcement is weak where no measurable requirement was ever published.
A guideline should have been issued to steer implementation — guidelines are non-mandatory and cannot produce consistency.

**Source**
[[Security Governance & Management]], [[Organizational Security Processes]]

## Card 8

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
A vendor storing regulated customer data suffers a breach. The client organization discovers it never reviewed the vendor's security posture before signing, holds no right-to-audit clause, and has no contractual breach notification timeline. Which failure is <b>MOST</b> fundamental?

**Options**
*Due diligence was never exercised in vendor selection — the security posture was never investigated, so nothing that followed could be grounded in an understanding of the risk.
The right-to-audit clause was omitted from the contract — a serious gap, but a consequence of never having assessed the vendor in the first place.
Breach notification timelines were not agreed — affects the speed of response rather than whether the risk was understood.
The vendor failed to meet minimum security requirements — no baseline was ever defined for the vendor to meet.

**Source**
[[Vendor, Consultant, and Contractor Agreements]], [[Supply Chain Risk Management]], [[Organizational Security Processes]]

## Card 9

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
A contractor's engagement ended four months ago, but their account remained active and was later used in an intrusion. The account had been provisioned with the same broad permissions as the vendor's full team. Which two failures does this represent?

**Options**
*Offboarding was not triggered by engagement end, and least privilege was never applied when the account was provisioned — the access should have been scoped to the engagement and expired with it.
Separation of duties and job rotation both failed — neither control governs the provisioning or expiry of third-party access.
Background screening and NDA coverage were inadequate — contractual and screening gaps, neither of which explains an account outliving its engagement.
Mandatory vacation and access review both failed — mandatory vacation applies to employees in fraud-sensitive roles, not to contractor provisioning.

**Source**
[[Vendor, Consultant, and Contractor Agreements]], [[AAA Framework]]

## Card 10

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
A department head insists that everyone at their clearance level should be able to read a dataset, and asks the database team to grant it. The dataset belongs to a different business unit. Who decides, and on what basis?

**Options**
*The owning business unit's asset owner decides, applying need-to-know — clearance establishes eligibility, while need-to-know determines actual access to specific data.
The database team decides, applying least privilege — custodians implement access decisions rather than making them.
The department head decides for their own staff, since they hold the same clearance — clearance alone does not confer access to another unit's data.
The CISO decides, applying the classification scheme — security defines the scheme but does not own individual datasets.

**Source**
[[Organizational Roles and Responsibilities]], [[AAA Framework]]

## Card 11

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
Separation of duties has been implemented for payment approval, yet an audit uncovers a fraud carried out by two colluding employees. Management asks what control should be added. Which is <b>MOST</b> appropriate?

**Options**
*Job rotation and mandatory vacation — detective controls that surface schemes surviving a preventive split, by putting a different person into the process.
A second approval step, requiring three signatories — raises the collusion threshold but repeats a preventive control that has already been defeated.
Stricter least privilege on both accounts — reduces the permissions each holds without addressing coordinated misuse of legitimate ones.
Additional security awareness training for the finance team — addresses recognition of external attacks, not deliberate insider collusion.

**Source**
[[Personnel Security Lifecycle]], [[Security Controls]]

## Card 12

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
An organization suffers a successful spear phishing attack against finance staff who had all completed awareness training within the last quarter. Which response reflects defence in depth <b>BEST</b>?

**Options**
*Add out-of-band verification for payment requests and strengthen mail filtering — the administrative layer will sometimes fail, so other layers must be in place to catch what it misses.
Repeat and intensify awareness training for the finance team — relies more heavily on the single layer that has already been shown to fail.
Replace awareness training with technical controls, since the training demonstrably did not work — removes a layer instead of adding to it.
Accept that determined spear phishing cannot be defended against and focus on incident response — abandons prevention entirely where layered controls remain available.

**Source**
[[Defense in Depth]], [[Security Awareness, Training, and Education]], [[Social Engineering]]

## Card 13

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
A vulnerability is disclosed in a third-party library. The organization has no component inventory and cannot determine its exposure. Management asks for the <b>FIRST</b> action in handling this specific incident, as distinct from fixing the underlying process.

**Options**
*Establish which applications actually contain the affected component — exposure cannot be assessed or treated until the scope is known.
Begin adopting software bills of materials across the estate — the correct process fix, but it does not address the live exposure now.
Apply virtual patching at the web application firewall across all applications — a broad mitigation applied before the affected scope is understood.
Formally accept the risk until the next release cycle — acceptance without knowing the exposure is not an informed decision.

**Source**
[[Supply Chain Risk Management]], [[Risk Management Concepts]]

## Card 14

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
A federal system has completed the Assess step of the NIST Risk Management Framework, and known weaknesses remain. Who takes the next decision, and what exactly is being decided?

**Options**
*A designated senior official authorizes the system — they formally accept the residual risk on the organization's behalf and permit it to operate.
The security assessor authorizes the system, since they hold the evidence of control effectiveness — assessors evaluate controls and do not accept risk.
The system owner remediates every remaining weakness before operation is permitted — the framework anticipates residual risk being accepted, not eliminated.
The control set returns to the Select step until no weaknesses remain — no system reaches a state of zero residual risk.

**Source**
[[Risk Frameworks]], [[Organizational Roles and Responsibilities]]

## Card 15

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
A dismissed administrator is suspected of deleting audit logs on their final day. Investigators find the account was disabled only after the termination meeting, and that log deletion is not separately restricted. Which two failures does this show?

**Options**
*The unfriendly termination procedure was not followed, and audit log integrity was not protected independently of administrative privilege — attribution fails when an administrator can erase their own trail.
Screening and NDA coverage were inadequate — pre-employment and contractual controls, neither of which governs revocation timing or log protection.
Least privilege and job rotation both failed — an administrator legitimately holds elevated access, and rotation would not have prevented deletion.
Separation of duties and mandatory vacation both failed — these address fraud concealed over time, not access retained during a dismissal.

**Source**
[[Personnel Security Lifecycle]], [[AAA Framework]], [[CIA Triad]]

## Card 16

**Domain**
1 — Security and Risk Management / Cross-Topic

**Question**
A qualitative risk workshop produces ratings that the board finds unconvincing, noting that the most senior attendee's views dominated and that no record explains how conclusions were reached. Which combination <b>BEST</b> addresses both concerns?

**Options**
*Gather independent anonymous judgments with the Delphi technique, then record the outcome in a risk register — anonymity removes the dominant voice, and the register supplies the owners and decisions the board found missing.
Switch to a fully quantitative assessment and present a heat map to the board — the data for monetary valuation may not exist, and a heat map records no reasoning.
Have the CISO override the ratings using professional judgment and document the result — replaces one dominant voice with another.
Repeat the workshop with junior staff excluded so ratings are consistent — removes the dissenting input rather than protecting it.

**Source**
[[Risk Assessment]], [[Organizational Roles and Responsibilities]]
