Building human security capability happens at three distinct levels, each targeting a different audience, depth, and outcome. The terms are often used interchangeably in casual conversation, but the formal distinction matters because the wrong approach for the wrong audience produces no behavior change. See [[Personnel Security Lifecycle]], [[Organizational Security Processes]].

## The Three Tiers

| Tier | Question Answered | Audience | Depth | Example Delivery |
|---|---|---|---|---|
| **Awareness** | *What* should I watch for? | All employees | Shallow, broad, frequent | Posters, phishing simulations, monthly security tips, lock-screen reminders |
| **Training** | *How* do I do this securely? | Role-specific (developers, admins, finance) | Practical, skill-building | Secure coding workshops, incident response drills, hands-on labs |
| **Education** | *Why* does this work this way? | Security professionals, leadership | Deep, conceptual | Degree programs, professional certifications (CISSP, CISM) |

- **Awareness** is about recognition. The goal is that a user can spot a phishing email or a tailgater — not that they understand the cryptography behind email signing.
- **Training** is about skill. The goal is that the person can perform a security-relevant task correctly: a developer writes input validation, an admin configures MFA, an analyst triages an alert.
- **Education** is about understanding. The goal is judgment in novel situations — knowing not just what to do but why, and being able to adapt when the playbook doesn't fit.

## Delivery and Reinforcement

- **Initial training** at onboarding sets the baseline, but a one-time session is essentially worthless within a few months. Knowledge decays without reinforcement.
- **Annual refreshers** are the regulatory minimum; **continuous micro-learning** (short, frequent touchpoints) produces better retention.
- **Event-driven training** follows incidents — after a phishing incident, the targeted team gets focused training while the lesson is concrete.
- Spaced repetition and gamification (leaderboards, simulated phishing scores) outperform one-off compliance modules.

## Measuring Effectiveness

Awareness programs are easy to run and hard to evaluate. Useful metrics:

- **Phishing simulation click-through rate** — the most common, declining trend over time indicates improving awareness.
- **Report rate** — even better: how many people actively report suspicious emails rather than just not clicking.
- **Quiz and assessment scores** — measures recall, but not behavior change.
- **Incident trends** — fewer personnel-caused incidents over time is the real outcome metric, though attribution is noisy.

## Social Engineering as a Focus

Most awareness programs center on social engineering because it bypasses technical controls entirely by targeting the human:

- **Phishing** — fraudulent messages (email, SMS, voice) impersonating a trusted party to extract credentials or trigger an action.
- **Pretexting** — fabricating a scenario to extract information (impersonating IT support, an auditor, a vendor).
- **Tailgating / Piggybacking** — following an authorized person through a physical access control without authenticating separately.
- **Baiting** — leaving infected media (USB drops) or offering something attractive to lure the target into a compromise.
- **Quid pro quo** — offering a benefit in exchange for information or access.

The defense is recognition. A workforce that pauses on unusual requests, verifies through a second channel, and reports anomalies neutralizes most social engineering before it lands.
