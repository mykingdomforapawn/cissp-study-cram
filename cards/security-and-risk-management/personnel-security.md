---
tags:
  - anki
---
Anki cards for the Personnel Security notes. Format: `cards/CLAUDE.md`.

---

## Card 1

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
A contractor arrives on site to begin work on a system holding customer data. The engagement paperwork is still with legal and the individual NDA is unsigned. The project manager asks security to provision access now and collect the signature at the end of the week. What is the <b>BEST</b> response?

**Options**
*Withhold access until the NDA is signed — confidentiality obligations must be in place before any sensitive information is disclosed.
Provision read-only access as a compromise until the NDA is signed — read access still discloses confidential information with no protection in place.
Provision access and record an exception in the risk register for later review — documenting an exception does not create the legal protection the NDA provides.
Provision access on the basis that the master services agreement already binds the vendor — an entity-level agreement may not bind the individual who will handle the data.

**Source**
[[Employment Agreements and Policies]]

## Card 2

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
An employee resigns. During the exit interview HR wants to remind them in writing of the obligations that continue to bind them after their last day. Which obligation <b>MOST</b> clearly survives termination?

**Options**
*The non-disclosure agreement — confidentiality obligations continue after employment, typically indefinitely or for a defined post-employment period.
The acceptable use policy — governs use of company resources during employment and lapses when access ends.
The code of conduct — sets behavioural expectations for the period of employment.
The annual security awareness training requirement — a condition of continued employment rather than a surviving obligation.

**Source**
[[Employment Agreements and Policies]]

## Card 3

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
An organization substantially revises its acceptable use policy to cover generative AI tools. Staff acknowledged only the previous version, at onboarding. An employee later violates provisions that exist solely in the new version. What weakens enforcement <b>MOST</b>?

**Options**
*Employees were never required to re-acknowledge the revised policy — enforcement against updated terms is weak without a fresh acknowledgement record.
The revised policy was not reviewed by external counsel — legal review improves drafting but is not what binds the employee.
The violation was detected by automated monitoring rather than by a supervisor — the detection method does not affect enforceability.
The employee had received no training on generative AI tools — training supports awareness, but acknowledgement is the binding record.

**Source**
[[Employment Agreements and Policies]]

## Card 4

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
A systems administrator holding domain administrator rights is being dismissed for misconduct. HR has scheduled the termination meeting for 14:00. What should happen to the administrator's access?

**Options**
*Accounts are disabled immediately before the meeting begins — the risk of sabotage or exfiltration is highest in an unfriendly termination, so revocation must precede notification.
Accounts are disabled at the end of the day, once the exit interview is complete — leaves a window in which a hostile administrator retains full privileges.
Passwords are reset while the accounts stay enabled for handover — a reset does not terminate active sessions or existing keys, and the account remains usable.
Access continues through a supervised notice period — appropriate for a friendly departure, not a dismissal for misconduct.

**Source**
[[Personnel Security Lifecycle]]

## Card 5

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
A finance department suspects that an employee is concealing a fraud requiring small daily adjustments to stay hidden. The employee has not taken leave in three years. Which control is <b>MOST</b> likely to expose the scheme?

**Options**
*Mandatory vacation — a continuous enforced absence with no system access exposes fraud that depends on daily intervention to remain concealed.
Separation of duties — splitting the task prevents future single-actor fraud but does not surface a scheme already running.
Least privilege — reducing permissions limits future exposure without revealing existing concealed activity.
Security awareness training — addresses recognition of attacks against staff, not detection of insider fraud.

**Source**
[[Personnel Security Lifecycle]]

## Card 6

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
A payments process is redesigned so that the person who initiates a wire transfer cannot also approve it. What is the <b>PRIMARY</b> security benefit?

**Options**
*Completing a fraudulent transfer now requires collusion between two people, which is far harder to organize and conceal — forcing collusion is the control.
Errors are reduced because a second person reviews every transfer — accuracy improves, but fraud prevention is the security objective.
Each participant needs fewer privileges overall — that is least privilege, a related but distinct principle.
The transfer is recorded twice, strengthening the audit trail — a side effect rather than the purpose of the split.

**Source**
[[Personnel Security Lifecycle]]

## Card 7

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
A quarterly review finds that a developer who transferred off the payments team six months ago still holds production database access from that former role. Which control failed, and what is the <b>BEST</b> systemic fix?

**Options**
*Periodic access review — access should be re-evaluated whenever someone's responsibilities change, not only on a fixed calendar, or privilege accumulates silently in between.
Offboarding; the account should have been disabled — the developer is still employed, so offboarding does not apply.
Least privilege was never established; the account should be rebuilt from scratch — the access was appropriate when granted and only became excessive later.
Separation of duties; the developer should never have held production access — a payments developer may legitimately have held it in the prior role.

**Source**
[[Personnel Security Lifecycle]]

## Card 8

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
Three companies form a joint research consortium in which every participant will disclose proprietary designs to both others. Legal wants a single instrument rather than a web of pairwise agreements. Which is <b>MOST</b> appropriate?

**Options**
*A multilateral NDA — binds three or more parties to protect every other party's confidential information under one agreement.
A bilateral NDA between each pair of companies — achieves equivalent protection but produces exactly the combinatorial overhead legal wants to avoid.
A unilateral NDA signed by each participant — protects only one disclosing party, which does not fit mutual disclosure.
A memorandum of understanding covering confidentiality — records intent and is not binding.

**Source**
[[Personnel Security Lifecycle]]

## Card 9

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
A monitoring platform flags that a service account which has historically only run nightly backup queries has begun issuing bulk reads against a customer database during business hours. Which capability produced this detection?

**Options**
*User and entity behaviour analytics — extends behavioural baselining to non-human entities such as service accounts, devices, and applications.
User behaviour analytics — baselines human user accounts and would not have profiled a service account.
Data loss prevention — inspects content leaving the environment rather than baselining account behaviour.
A SIEM correlation rule — matches known patterns, whereas this detection came from a deviation against a learned baseline.

**Source**
[[Personnel Security Lifecycle]]

## Card 10

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
Following a series of injection flaws in its products, an organization wants its development teams to reliably write correct input validation. Which intervention is being described?

**Options**
*Training — role-specific and skill-building, aimed at performing a security-relevant task correctly.
Awareness — broad, shallow recognition of what to watch for, which does not build a technical skill.
Education — conceptual understanding aimed at security professionals and leadership, deeper than what is needed here.
Certification — evidence of individual knowledge, not an organizational intervention that changes coding practice.

**Source**
[[Security Awareness, Training, and Education]]

## Card 11

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
A security manager reports a falling phishing simulation click rate but suspects the figure overstates real progress. Which additional metric <b>BEST</b> indicates that awareness is producing the desired behaviour?

**Options**
*The proportion of recipients who actively report the simulated message — reporting demonstrates engaged detection rather than mere non-interaction.
The average score on the annual awareness quiz — measures recall rather than behaviour.
The percentage of employees completing training on time — measures participation, not effectiveness.
The number of phishing emails blocked by the mail gateway — measures a technical control, not human behaviour.

**Source**
[[Security Awareness, Training, and Education]]

## Card 12

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
A finance team is successfully targeted by an invoice fraud email. The organization's annual awareness refresher is nine months away. What is the <b>MOST</b> effective immediate action?

**Options**
*Deliver focused training to the affected team now, while the incident is concrete — event-driven training lands far better than a deferred general refresher.
Bring the annual refresher forward for the whole organization — broad and poorly matched to the specific lesson available.
Add the incident as a case study in next year's refresher — delays the lesson until its relevance has faded.
Increase the frequency of phishing simulations for the finance team — useful reinforcement, but it does not teach the process failure that allowed the payment.

**Source**
[[Security Awareness, Training, and Education]]

## Card 13

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
An attacker researches a company's CFO on social media, then sends a highly personalized email appearing to come from the CEO and requesting an urgent transfer. How is this attack <b>BEST</b> classified?

**Options**
*Whaling — spear phishing directed at an executive or other high-value target, with correspondingly high personalization.
Spear phishing — accurate in general terms, but whaling is the precise term when the target is an executive.
Vishing — voice-based phishing, whereas this attack was delivered by email.
Pretexting — a fabricated scenario is present, but the targeting and delivery make whaling the precise classification.

**Source**
[[Social Engineering]]

## Card 14

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
An employee badges into a secure area and, seeing someone behind them carrying boxes, deliberately holds the door open. That second person was not authorized to enter. Which term describes this <b>MOST</b> precisely?

**Options**
*Piggybacking — the authorized person knowingly grants entry, and that consent is what distinguishes it from tailgating.
Tailgating — the follower slips through without the authorized person's knowledge or consent.
Impersonation — requires the attacker to claim a specific identity, which is not described here.
Shoulder surfing — observation of screens or keyboards, unrelated to physical entry.

**Source**
[[Social Engineering]]

## Card 15

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
An organization has twice paid fraudulent payment requests that appeared to come from senior executives. Awareness training has already been delivered to the finance team. Which control <b>BEST</b> addresses the remaining exposure?

**Options**
*A mandatory call-back procedure that verifies payment requests through an independently sourced channel — out-of-band verification defeats even a convincing impersonation.
Stronger spam and anti-phishing filtering at the mail gateway — reduces volume but cannot reliably stop a well-crafted targeted message.
Multi-factor authentication on executive mailboxes — protects the accounts, but does not help when the sender address is merely spoofed.
More frequent awareness refreshers for the finance team — reinforcement has already been tried and left this exposure open.

**Source**
[[Social Engineering]]

## Card 16

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
An audit repeatedly finds active accounts belonging to contractors whose engagements ended months earlier. The current process relies on the sponsoring manager raising a revocation ticket at engagement end. What is the <b>BEST</b> remediation?

**Options**
*Provision contractor accounts with an automatic expiry tied to the engagement end date — removes reliance on the manual step that is already routinely missed.
Send managers a monthly reminder to review their contractors — still depends on the manual action that is failing.
Require contractors to confirm annually that they still need their access — self-attestation by the account holder is a weak control.
Consolidate contractor accounts into a single shared account per vendor — improves visibility of the population but makes activity unattributable.

**Source**
[[Vendor, Consultant, and Contractor Agreements]]

## Card 17

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
A company outsources claims processing, which requires the vendor to store regulated personal data. Legal asks which contractual provision would let the company verify the vendor's security controls after the contract is signed. Which clause?

**Options**
*A right-to-audit clause — permits the client to examine the vendor's security controls and personnel practices during the relationship.
A breach notification clause — obliges the vendor to report incidents but grants no verification rights.
A background check clause — requires the vendor to screen its personnel but does not allow control verification.
A service level agreement — defines expected service levels and remedies, not rights of inspection.

**Source**
[[Vendor, Consultant, and Contractor Agreements]]

## Card 18

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
A consultancy already has an umbrella contract with a client covering liability, IP ownership, and security obligations. A new six-week engagement is now agreed. Which document defines that engagement's scope, deliverables, duration, and named personnel?

**Options**
*A statement of work — defines a specific engagement operating under the umbrella agreement.
A master services agreement — is the umbrella already in place, so a second one is unnecessary.
A business partnership agreement — establishes the terms of a partnership rather than a discrete engagement.
A memorandum of understanding — records non-binding intent and is unsuitable for paid work.

**Source**
[[Vendor, Consultant, and Contractor Agreements]]

## Card 19

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
An employee receives a call from someone identifying themselves as the head of internal audit, who states that a regulatory filing is due within the hour and demands the employee read out a system password immediately. Which two psychological principles is the caller relying on <b>MOST</b> directly?

**Options**
*Authority and urgency — a claimed position of power short-circuits skepticism, and time pressure removes the opportunity to verify.
Scarcity and consensus — scarcity exploits fear of missing out, and consensus relies on what others are said to be doing, neither of which is present here.
Familiarity and trust — these depend on an established relationship the caller has not claimed.
Intimidation and liking — liking works by building rapport, which contradicts the pressure being applied.

**Source**
[[Social Engineering]]

## Card 20

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
Users report emails whose subject lines begin with "RE:" as if continuing an existing thread, sent from a domain differing from the corporate one by a single transposed letter. Which two techniques are in use?

**Options**
*Prepending and typosquatting — a legitimate-looking prefix makes the message appear part of a trusted exchange, and the near-identical domain survives a quick glance.
Pretexting and impersonation — a fabricated scenario and a claimed identity, neither of which describes the subject line or the domain.
Elicitation and masquerading — drawing out information through conversation, and assuming an identity inside a system after credentials are stolen.
Hoax and spam — false information spread to cause panic, and bulk unsolicited messaging.

**Source**
[[Social Engineering]]

## Card 21

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
An attacker recovers printed account statements and a decommissioned drive from a skip behind an office building. Which countermeasure would have been <b>MOST</b> effective?

**Options**
*A secure disposal policy with document shredding and certified media destruction — removes the recoverable material at source.
A clean desk policy — protects material during the working day but does not govern how it is discarded.
Visitor escort procedures — control access to the interior, whereas the skip is outside the controlled perimeter.
Security awareness training on tailgating — addresses a different physical attack entirely.

**Source**
[[Social Engineering]]

## Card 22

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
An organization is hiring both a treasury analyst who will authorize payments and a graphic designer who will work on marketing collateral. HR proposes running an identical background check package, including a credit history check, on both. What is the <b>BEST</b> objection?

**Options**
*Screening depth should scale with the sensitivity of the role — a credit check is a relevant fraud indicator for the treasury role and not justifiable for the designer.
Credit history checks are never permissible in pre-employment screening — they are legitimate for finance-adjacent roles where financial pressure is a genuine risk indicator.
Both candidates should instead receive the deeper package applied to the treasury role — uniformly maximal screening is disproportionate and costly.
Background checks should be run after the offer rather than before — timing is a separate question and does not address the mismatch in depth.

**Source**
[[Personnel Security Lifecycle]]

## Card 23

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
A hiring manager wants to post a newly created role immediately and work out its system access once someone is in the seat. What is the <b>PRIMARY</b> security argument for documenting duties, data sensitivity, and required privileges before the role is advertised?

**Options**
*The documented role is the foundation for least privilege and separation of duties — without it, access is granted ad hoc, drifts over time, and accountability blurs.
It allows the recruiter to describe the role accurately to candidates — a hiring benefit rather than a security control.
It determines which employment agreements the new hire must sign — the standard agreements apply regardless of how the role is documented.
It establishes the salary band appropriate to the level of responsibility — a compensation question with no security dimension.

**Source**
[[Personnel Security Lifecycle]]

## Card 24

**Domain**
1 — Security and Risk Management / Personnel Security

**Question**
Each department at a company manages its own contractors through spreadsheets and shared inboxes. Nobody can state how many third-party personnel currently hold access, and audit findings on stale contractor accounts recur every year. What is the <b>BEST</b> systemic response?

**Options**
*Implement a vendor management system as the single system of record, integrated with identity management — engagement end dates then drive revocation automatically, and the active contractor population becomes a query rather than a scavenger hunt.
Issue a policy requiring every department to maintain its contractor spreadsheet accurately — preserves the fragmentation that causes the problem.
Run a quarterly manual reconciliation of contractor accounts against departmental records — detects the drift repeatedly without preventing it.
Require all contractors to be converted to employees — a disproportionate response that removes the flexibility contracting exists to provide.

**Source**
[[Vendor, Consultant, and Contractor Agreements]]
