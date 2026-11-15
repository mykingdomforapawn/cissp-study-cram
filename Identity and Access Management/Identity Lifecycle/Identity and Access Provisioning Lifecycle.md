An account's life runs **provisioning → maintenance → review → deprovisioning**. Each stage has a characteristic failure, and all of them end in the same place: subjects holding access they should not have.

The HR-side process (screening, agreements, termination procedure) is in [[Personnel Security Lifecycle]]; this note covers the account itself.

## Provisioning and Onboarding

Creating the identity and granting initial access, after identity proofing (see [[Identity Proofing and Registration]]).

- Grant from a **role template**, never by **cloning an existing user's account** — copying a colleague propagates whatever accumulated rights they had.
- Apply **least privilege** and need-to-know from day one; it is far harder to remove access later than to withhold it.
- **Automate** provisioning from the authoritative HR system so account creation, changes, and removal are driven by employment status rather than by tickets. SCIM does this across federated services (see [[Federated Identity Management]]).
- Record **who approved** each grant and **why** — without this, later reviews have no baseline to judge against.
- Onboarding also covers credential issuance, acceptable-use acknowledgment, and security awareness training (see [[Security Awareness, Training, and Education]]).

## Role Definition and Transition

Access is assigned to **roles**, and users to roles — so the policy is stated once and reviewed in one place (see the abstraction discussion in [[AAA Framework]]).

- Roles are defined from **job functions**, with an owner responsible for what each role grants.
- **Transfers are the main risk.** When someone changes roles, the old role must be **removed, not merely supplemented**. Otherwise **privilege creep** (authorization creep) accumulates until a long-tenured employee can do nearly anything — and a single account quietly violates **separation of duties**.
- A **transfer should be treated as a deprovision plus a provision**, not an amendment.

## Account Maintenance

Keeping the account's state accurate across its life: role changes, name changes, temporary elevation, **leave of absence** — disable rather than delete for any absence of roughly **30 days or more**, since the employee is expected to return; resetting the password is not enough, because someone else could still log on, and credential reissue after loss.

Account types to watch:

- **Dormant / inactive** accounts — unused, unmonitored, still valid. Disable automatically after a defined period.
- **Orphaned** accounts — no valid owner remains, typically after a departure the process missed.
- **Shared and generic** accounts — destroy accountability; replace with named accounts, or vault them (see [[Credential and Session Management]]).
- **Service accounts** — need an owner and rotation; see [[Device and Service Authentication]].

## Account Access Review

Periodic verification that existing access is still justified — the control that catches what every other stage missed.

- **Recertification / attestation**: account and entitlement owners (managers, data owners — not IT) confirm or revoke each grant, on a schedule set by sensitivity. Privileged accounts are reviewed most often.
- Rubber-stamped approval is the usual failure; reviews work only when revocation actually happens and is verified.
- Look for privilege creep, dormant and orphaned accounts, excessive privilege, separation-of-duties conflicts, and accounts outside the authoritative source.
- Reviews are **detective**; automated provisioning from HR data is the **preventive** fix for the same problem.

## Deprovisioning and Offboarding

- **Disable immediately, delete later.** Disabling preserves encryption keys, file ownership, and audit trails; immediate deletion destroys evidence and orphans data.
- Disable **during the exit interview**, not after it. The point is to **prevent sabotage** by a departing employee who still has working access, and for **hostile terminations** the disable happens before or during the notification.
- Cover **everything**: SSO account, local and legacy accounts, VPN and remote access, cloud and SaaS services outside SSO, shared-account passwords the person knew, API keys and certificates, physical badges and keys, and MFA enrollments.
- **Transfer ownership** of data, mailboxes, and service accounts before removal.

## Key Points

- **Provision from role templates, never by cloning another user's account.**
- **Privilege creep comes from transfers — remove the old role, do not just add the new one.**
- **Access reviews are detective and must be done by business owners; automated HR-driven provisioning is the preventive control.**
- **Disable accounts immediately on departure and delete only later, to preserve keys and audit trails.**
