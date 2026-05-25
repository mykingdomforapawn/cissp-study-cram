Social engineering exploits human psychology rather than technical vulnerabilities to gain unauthorized access, information, or action. It is the most reliable attack vector because people, unlike systems, cannot be patched. See [[Personnel Security Lifecycle]], [[Security Awareness, Training, and Education]].

## Psychological Principles

Attackers exploit predictable cognitive biases to bypass rational evaluation:

- **Authority** — people comply with requests from perceived figures of power (boss, IT, auditor, law enforcement). Impersonating authority short-circuits skepticism.
- **Urgency** — pressure to act immediately reduces deliberation. "Your account will be suspended in 24 hours" bypasses verification habits.
- **Consensus** — people follow what they believe others are doing. "Everyone on your team has already submitted their credentials."
- **Scarcity** — limited availability triggers fear of missing out. Fake limited-time offers prompt hasty action.
- **Familiarity/Liking** — people help people they like or recognize. Attackers build rapport or impersonate known contacts.
- **Trust** — established relationships lower defenses; attackers invest time building trust before making a malicious request.
- **Intimidation/Fear** — threats of consequences (legal action, job loss, arrest) suppress the instinct to verify.

## Elicitation Techniques

- **Eliciting information** — drawing out sensitive details through seemingly innocent conversation; using flattery, feigned ignorance, or false statements the target feels compelled to correct.
- **Prepending** — adding a legitimate-looking prefix to a message or domain ("RE:", "SAFE:", "IT-DEPT-") to make it appear part of a trusted thread or to bypass filters.

## Digital and Communication Attacks

- **Phishing** — mass email campaign impersonating a trusted entity to steal credentials or deliver malware. Broad targeting, low personalization.
- **Spear phishing** — targeted phishing using specific details about the victim (name, role, recent activity) to increase believability.
- **Whaling** — spear phishing aimed at executives or high-value targets. Higher investment in personalization.
- **Vishing** — voice phishing; phone calls impersonating IT support, banks, or government agencies to extract information or push actions.
- **Smishing** — SMS phishing; text messages with malicious links or requests. High open rates make it effective.
- **Spam** — bulk unsolicited messages; used as a delivery vehicle for phishing, malware, and scams.
- **Invoice scam** — fake invoices sent to finance teams for goods or services never rendered, relying on process gaps or urgency to get them paid.
- **Hoax** — false information spread to create panic or manipulate behavior (e.g., fake virus warnings that prompt users to delete legitimate files).
- **Typosquatting** — registering domains that are common misspellings of legitimate sites (e.g., "paypa1.com") to intercept traffic from users who mistype.

## Identity Attacks

- **Impersonation** — directly pretending to be someone else — a vendor, IT technician, executive — to gain trust or access.
- **Masquerading** — using stolen or fabricated credentials to assume another identity within a system; broader than impersonation in that it persists beyond initial access.
- **Identity fraud** — using stolen personal information to open accounts, conduct transactions, or assume a victim's identity at scale.

## Physical Attacks

- **Shoulder surfing** — observing someone's screen or keyboard to capture credentials, PINs, or sensitive data. Effective in public spaces and open offices.
- **Tailgating** — following an authorized person through a secured door without authenticating; relies on social pressure not to challenge the follower.
- **Piggybacking** — similar to tailgating but the authorized person knowingly holds the door; the distinction is consent.
- **Dumpster diving** — retrieving discarded documents, drives, or devices containing sensitive information. Shredding policies and secure disposal are the countermeasure.

## Large-Scale Attacks

- **Social media** — platforms used to gather reconnaissance (OSINT on targets), spread disinformation, run influence operations, or deliver phishing via direct messages and fake profiles.
- **Influence campaigns** — coordinated efforts to shape public opinion or behavior through disinformation, fabricated content, and social media manipulation. Both state-sponsored and criminal variants exist.
- **Hybrid warfare** — combining conventional military operations with cyber, information warfare, and social engineering to destabilize an adversary; influence campaigns are a core component.

## Countermeasures

- **Security awareness training** — the primary control; humans are the target so humans must be the defense.
- **Verification procedures** — call-back policies, out-of-band confirmation for sensitive requests.
- **Clear escalation paths** — defined process for reporting suspected social engineering attempts.
- **Technical controls** — spam filters, anti-phishing email gateways, MFA, domain monitoring for typosquatting.
- **Physical controls** — mantrap/airlock entry, visitor escort policies, clean desk policy, document shredding.
