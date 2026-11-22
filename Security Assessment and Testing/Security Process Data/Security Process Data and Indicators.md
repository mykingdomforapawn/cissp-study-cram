**Collecting security process data** means gathering evidence that security processes are running and working, then reporting it upward so management can act. The processes themselves are documented elsewhere in the vault; this note covers **what data each one yields** and **how it is measured and reported**.

## Account Management

The provisioning, review, and deprovisioning process is covered in full in [[Identity and Access Provisioning Lifecycle]]. As a source of process data, it yields:

- **Access review and recertification results** — how many entitlements were revoked at review, which is a direct measure of accumulated **privilege creep**.
- **Provisioning and deprovisioning timeliness** — especially **time from termination to account disablement**, which is the metric that exposes a broken offboarding handoff.
- **Counts of dormant, orphaned, and shared accounts** outstanding.

## Backup Verification

A backup that has never been restored is an assumption, not a control. The process data:

- **Restore tests actually performed**, and whether the restored data was complete and usable. **Successful backup jobs are not evidence of recoverability** — only a test restore is.
- **Measured restore time against the RTO**, and data loss at the restore point against the RPO (see [[Business Impact Analysis]]).

## Disaster Recovery and Business Continuity

The exercise types — tabletop and structured walkthrough, simulation, parallel test, and full interruption — along with their relative cost and risk, are covered in [[Approval and Implementation]]. What they produce as process data:

- **Whether exercises occurred on schedule**, and at what level of rigour.
- **Findings and plan corrections** arising from each, and whether they were closed before the next one.
- **Measured recovery times** compared against the objectives the [[Business Impact Analysis]] set.

The value of an exercise is the **gaps it reveals and the plan updates that follow** — an exercise with no findings usually means it was not realistic enough.

## Training and Awareness

The three-tier model (awareness, training, education), delivery methods, and how effectiveness is measured are covered in [[Security Awareness, Training, and Education]]. The process data it yields is **completion rates by population** and, more meaningfully, **behavioural outcomes** such as phishing simulation click and report rates trended over time.

## Key Performance and Risk Indicators

Two distinct kinds of measure, and the distinction is **direction in time**:

| | Key Performance Indicator (KPI) | Key Risk Indicator (KRI) |
|---|---|---|
| **Measures** | How well a process is **performing** | How much **risk exposure** is building |
| **Direction** | **Lagging** — reports what has already happened | **Leading** — signals what may happen |
| **Question** | "Is our security program working?" | "Where is risk increasing?" |
| **Examples** | Mean time to detect and respond, patch compliance percentage, percentage of systems scanned, training completion | Number of unpatched critical vulnerabilities, count of exception approvals outstanding, privileged accounts without review, failed change rate |

**KPIs are lagging measures of performance; KRIs are leading indicators of risk.** A program needs both: KPIs show whether what is being done is done well, KRIs give warning while there is still time to act.

Properties of a useful indicator:

- **Tied to an objective** — a number with no decision attached to it is reporting, not measurement.
- **Measurable and consistently defined**, so a trend across periods means something.
- **Outcome-oriented rather than activity-oriented** — *time to detect and respond* beats *number of alerts generated*, just as it does for the physical KPIs in [[Physical Security Management]].
- **Trended over time**, since a single value has no context.

## Management Review and Approval

Process data has no effect until management acts on it. A formal **management review** is a scheduled meeting at which leadership examines the security program's results, and it is a requirement of management system standards such as ISO 27001 (see [[Audit Types and Reporting Standards]]).

- **Inputs** — assessment and audit findings, metrics and indicator trends, incidents, exercise results, outstanding exceptions, and the status of previous review actions.
- **Outputs** — decisions: approving remediation and resources, accepting residual risk, directing changes to the program (see [[Risk Response]]).
- **The output must be recorded**, because the record is what demonstrates that leadership exercised oversight — the due care argument in [[Organizational Security Processes]].

**Reporting must be matched to the audience.** Technical owners need finding detail; executives need trends, business risk, and the specific decisions being asked of them. A dashboard of raw scanner counts delivered to a board is data that cannot be acted on.

## Key Points

- **Collecting security process data means gathering evidence that processes run and work, and reporting it so management can act.**
- **Successful backup jobs are not evidence of recoverability — only a test restore is.**
- **The value of a DR or BC exercise is the gaps it reveals and the plan corrections that follow.**
- **KPIs are lagging measures of process performance; KRIs are leading indicators of rising risk exposure.**
- **A useful indicator is tied to an objective, consistently defined, outcome-oriented, and trended over time.**
- **Management review is a scheduled leadership examination of the program whose recorded decisions demonstrate due care.**
- **Report to the audience: detail for technical owners, trends and decisions for executives.**
