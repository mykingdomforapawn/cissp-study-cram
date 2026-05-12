Third parties who perform work alongside or inside the organization — vendors providing services, consultants on time-bound engagements, contractors filling skill gaps — are people-shaped extensions of the workforce. They get access, handle data, and can cause the same kinds of incidents as employees, but they sit outside the standard HR lifecycle. This note covers the personnel angle: agreements, access, and offboarding. For the hardware/software supply side, see [[Supply Chain Risk Management]].

## Why Treat Them Separately

- **No direct employment relationship** — HR controls (background checks, mandatory training, performance reviews) don't apply automatically. They must be negotiated into the contract.
- **Loyalty is divided** — a contractor's primary obligation is to their employer, not to the client organization. Their interests can diverge.
- **Access is often broad and time-bound** — engagements have hard end dates that frequently slip, leaving stale privileged access.
- **Visibility is reduced** — third-party personnel may not appear in the organization's HRIS, making lifecycle tracking harder.

## Multiparty Risk

When multiple organizations interconnect — sharing data, integrating systems, or working a joint engagement — each party's security posture becomes a risk factor for every other party. A breach at the weakest link can cascade through the network of trust, and an incident often involves data or systems that span several organizations at once.

- A compromise at a single contractor can expose every client they serve.
- A joint venture's shared environment is only as secure as the least mature partner's controls.
- Incident response is harder: notification, forensics, and remediation must coordinate across legal entities with different priorities and timelines.
- Liability and accountability are diluted — when something goes wrong, "whose breach was it?" is often genuinely unclear.

The control response is contractual (defined security baselines, right-to-audit, breach notification SLAs) combined with technical isolation (segmented access, scoped credentials) so that one party's failure doesn't automatically become everyone's failure.

## Agreements

- **Master Services Agreement (MSA)** — the umbrella contract governing the overall relationship, including security obligations, liability, and IP ownership.
- **Statement of Work (SoW)** — defines a specific engagement under the MSA: scope, deliverables, duration, and personnel.
- **NDA** — signed by the contracting entity *and* often by individual contractors who will touch sensitive data.
- **Background check clause** — requires the vendor to screen their personnel to a defined standard before assignment to the engagement.
- **Right-to-audit clause** — permits the client organization to verify the vendor's security controls and personnel practices.
- **Data handling and breach notification** — defines how the vendor handles client data and the timeline for notifying the client of any incident.

For the broader vendor-agreement landscape (SLA, MOU, ISA, BPA), see [[Supply Chain Risk Management]].

## Access Controls

- **Time-bound accounts** — accounts provisioned with an automatic expiry tied to the engagement end date. Manual revocation alone is unreliable.
- **Least privilege, tightly scoped** — access only to systems and data needed for the specific engagement, not the contractor's full role at their employer.
- **Separate identity** — contractors typically get a distinct account naming convention (e.g., `c-jdoe`) so they're visible in logs and access reviews.
- **No shared credentials** — each contractor has their own account; "the contractor account" used by a rotating team is unauditable.
- **MFA and session monitoring** — privileged third-party access is a known target; additional controls are warranted.

## Lifecycle Differences

- **Onboarding** — contractor signs NDA and AUP equivalents, completes any required training, receives time-bound access. Often compressed into hours rather than days.
- **Ongoing** — periodic access reviews verify the contractor is still on the engagement and still needs the access they have. Stale contractor access is one of the most common audit findings.
- **Offboarding** — engagement end triggers automated account disablement. Devices and credentials returned. The vendor's HR offboarding (the contractor leaving their employer) should also trigger client-side revocation, but rarely does without explicit contractual obligation.

## Vendor Management System (VMS)

A **Vendor Management System (VMS)** is the platform that operationalizes everything above — a centralized system of record for third-party relationships, replacing the scattered mix of spreadsheets, shared inboxes, and tribal knowledge that most organizations start with.

Typical responsibilities:

- **Contract repository** — MSAs, SoWs, NDAs, insurance certificates, and audit reports stored in one place with expiry tracking.
- **Onboarding workflow** — drives background checks, training completion, and access requests as a checklist tied to the engagement.
- **Identity and access integration** — feeds the IAM system so that contractor accounts inherit the engagement's end date automatically, and revocation happens without a manual ticket.
- **Performance and risk tracking** — captures SLA adherence, incident history, audit findings, and renewal decisions.
- **Offboarding triggers** — engagement closure, contract expiry, or vendor termination automatically initiates access removal and asset return.

The value is visibility and consistency. Without a VMS, third-party risk is managed differently by each department, and the population of active contractors is usually larger than anyone realizes. With one, the same controls apply uniformly and audit evidence is a query, not a scavenger hunt.
