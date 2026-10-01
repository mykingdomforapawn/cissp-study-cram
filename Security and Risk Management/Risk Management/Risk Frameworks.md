Frameworks provide repeatable processes, common vocabulary, and defensible decisions that ad-hoc risk management lacks. Two NIST frameworks are the most exam-relevant; others are worth recognizing by name and purpose.

## NIST CSF (Cybersecurity Framework)

Outcome-based and voluntary — defines *what* to achieve, not *how*. Organized around six functions:

1. **Govern** — establish risk strategy, policies, and accountability (added in CSF 2.0)
2. **Identify** — understand assets, risks, and the business context
3. **Protect** — implement safeguards to limit impact
4. **Detect** — identify cybersecurity events in a timely manner
5. **Respond** — take action when an incident is detected
6. **Recover** — restore capabilities after an incident

**Version note:** Govern arrived with CSF 2.0 in 2024. CSF 1.1 had five functions, Identify through Recover, and a great deal of existing documentation, training material, and tooling still describes it that way. Adding Govern was an acknowledgement that the other five presuppose someone has set the risk strategy and assigned accountability — previously treated as context, now part of the framework itself. See [[Security Control Frameworks]].

## NIST RMF (Risk Management Framework, SP 800-37)

More prescriptive than CSF; primarily used in federal and government contexts. Seven steps:

1. **Prepare** — establish context and risk management roles
2. **Categorize** — classify the system by impact level (FIPS 199)
3. **Select** — choose appropriate controls from SP 800-53
4. **Implement** — put controls in place
5. **Assess** — verify controls work as intended (see [[Security Controls]])
6. **Authorize** — management formally accepts residual risk
7. **Monitor** — continuously track control effectiveness

## Risk Maturity Model (RMM)

Rates how mature an organization's risk management *process* is, not how much risk it has. Five levels:

1. **Ad Hoc** — chaotic, no defined process; risk management happens reactively if at all
2. **Preliminary** — loose, informal attempts; each department assesses risk its own way
3. **Defined** — a common, standardized risk framework is adopted organization-wide
4. **Integrated** — risk management is woven into business processes, with metrics tracking effectiveness and risk feeding into strategy decisions
5. **Optimized** — focus shifts from reacting to threats to achieving objectives; lessons learned feed back into the process and risk management supports strategic planning

## Other Frameworks

- **ISO 27005** — risk management standard within the ISO 27000 family; aligns with ISO 27001 for information security management systems
- **FAIR** (Factor Analysis of Information Risk) — quantitative model for expressing risk in financial terms; useful when dollar-denominated outputs are needed
- **OCTAVE** (Carnegie Mellon) — asset-driven, team-based approach suited to organizations assessing their own risk without external consultants
