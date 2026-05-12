Personnel are the largest and least patchable attack surface — most breaches involve a human element. The personnel security lifecycle is the set of HR-driven controls that govern someone's relationship with the organization from before they are hired through after they leave. It complements technical controls: even a perfectly hardened system fails if the person operating it is unscreened, untrained, or unmonitored. See [[AAA Framework]], [[Organizational Roles and Responsibilities]].

```text
   Pre-employment           Employment              Termination
   ─────────────────        ─────────────────       ─────────────────
   Job description     →    Onboarding         →   Offboarding
   Screening                Oversight              Exit procedure
                            (rotation, SoD,
                             mandatory vacation)
```

## Pre-employment

- **Job Description and Responsibilities**
	* Goal: Define what the role does, what data it touches, and what privileges it needs *before* posting it.
	* Mechanism: Written role descriptions including duties, reporting line, sensitivity level, and required clearance.
	* Example: A database administrator role is documented as requiring elevated production access and quarterly access reviews — this drives both the screening depth and the access provisioning later.
	* Why it matters: Foundation for **least privilege** and **separation of duties**. Without a clear role definition, access drifts and accountability blurs.
- **Pre-employment Screening**
	* Goal: Verify the candidate is who they claim to be and surface disqualifying history before granting access.
	* Mechanism: Background checks, reference checks, criminal record, credit history (for finance-adjacent roles), education and certification verification, employment history.
	* Example: A candidate for a treasury role undergoes a credit check; an undisclosed bankruptcy is a fraud risk indicator for that specific position but irrelevant for a graphic designer.
	* Depth scales with role sensitivity — high-clearance roles get deeper investigation; entry-level roles get baseline checks.

## Onboarding

- **Employment Agreement Signing**
	* Goal: Bind the new hire to confidentiality, acceptable use, and conduct obligations *before* any access is granted.
	* Mechanism: Signed NDA, AUP, code of conduct, and any role-specific agreements (e.g., NCA, conflict-of-interest disclosure). See [[Employment Agreements and Policies]].
	* Example: A new engineer signs a standard NDA on day one. When the same engineer is later assigned to a joint development project with two partner companies, they sign an additional multilateral NDA covering disclosures among all three organizations.
	* **NDA scope variants** — worth knowing because the right form depends on who is disclosing to whom:
		- **Unilateral NDA** — one party discloses, the other protects. The standard employer-employee NDA.
		- **Bilateral (mutual) NDA** — both parties disclose and both protect. Common between business partners evaluating a deal.
		- **Multilateral NDA** — three or more parties, each bound to protect every other party's confidential information. Used in joint ventures, consortiums, and multi-party R&D. Avoids the combinatorial mess of pairwise bilateral NDAs.
- **Identity Provisioning and Initial Access**
	* Goal: Establish identity, grant minimum required access, and enable the person to do their job.
	* Mechanism: Account creation under least privilege, badge issuance, initial security awareness training (see [[Security Awareness, Training, and Education]]).
	* Example: New hire's accounts are provisioned with their team's standard role template — not a copy of their manager's permissions. First login only happens after agreements are signed.

## Employment (Oversight)

Ongoing controls that detect misuse, deter fraud, and limit the damage any one person can do.

- **Periodic Role and Access Review**
	* Goal: Catch drift between what a person's role actually requires today and what they're documented to do — and what access they still hold. Responsibilities, tasks, and privileges accumulate over time as people absorb work from departing colleagues, switch teams, or take on side projects.
	* Example: A manager's quarterly review surfaces that a developer who moved off the payments team six months ago still has production database access from their old role. Access is revoked, the job description is updated, and the access matrix now reflects current reality.
	* Without this, least privilege erodes silently and offboarding misses entitlements that were never recorded.
- **Job Rotation**
	* Goal: Periodically move people between roles so no single person becomes the only one who understands a critical process.
	* Example: A finance team rotates the reconciliation duty monthly. A long-running embezzlement scheme is uncovered when a new rotator notices irregular entries the previous person had normalized.
	* Why it matters: Surfaces fraud, reduces single-person dependency, and cross-trains for resilience.
- **Separation of Duties (SoD)**
	* Goal: Split a sensitive action across multiple people so no one can complete it alone. The defense is forcing **collusion** — bypassing SoD requires two or more people to conspire, which is far harder to organize and conceal than a single bad actor.
	* Example: The engineer who writes a database change is not the one who applies it to production. Other common splits: request/approval, payment-initiator/payment-approver, developer/deployer.
- **Mandatory Vacation**
	* Goal: Force another person to cover the role for a continuous period (typically one to two weeks with no system access), exposing schemes that depend on the original person being present and active.
	* Example: A trader who never takes vacation is required to disconnect for two weeks; the colleague covering positions discovers manipulated trade records.
- **Performance and Behavior Monitoring**
	* Goal: Detect risk indicators — disengagement, policy violations, anomalous access patterns — before they become incidents.
	* Mechanism: Regular performance reviews, supervisor escalations, and analytics platforms:
		- **UBA (User Behavior Analytics)** — baselines normal patterns for user accounts and flags deviations (off-hours access, unusual data volumes, atypical resource use).
		- **UEBA (User and Entity Behavior Analytics)** — extends UBA to non-human entities (service accounts, devices, applications), catching anomalies in automated activity that pure user-focused analytics miss.
	* Example: UEBA flags a service account suddenly making bulk queries against a customer database it has historically only touched for nightly backups — the credential had been compromised and reused by an attacker.

## Termination / Offboarding

- **Exit Procedure**
	* Goal: Cleanly revoke access and recover assets while reinforcing surviving obligations.
	* Mechanism: Account disablement (not just password change), badge return, device collection, exit interview, written reminder that NDA and other agreements survive termination.
	* Example: On the employee's last day, HR coordinates with IT to disable accounts at a specific time; the badge is collected at the exit interview where the departing employee acknowledges ongoing confidentiality obligations.
- **Friendly vs. Unfriendly Termination**
	* **Friendly** (resignation, retirement): standard offboarding over a notice period; access typically maintained until the last day with normal supervision.
	* **Unfriendly** (firing, layoff, suspected misconduct): immediate access revocation, escorted exit, no system access during any remaining notice. The risk of sabotage or data exfiltration is highest in this scenario, so speed matters more than ceremony.
	* Example: A terminated systems administrator is walked out the same day; their accounts are disabled before the meeting where the termination is communicated, not after.
