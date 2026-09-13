The Business Impact Analysis (BIA) is the second element of BCP (see [[BCP vs DRP]]): it identifies critical business functions and quantifies the cost of losing them, which drives every prioritization decision later in the plan. It runs in five stages:

1. **Identifying priorities** — catalog business functions and the assets/processes that support them
2. **Risk identification** — identify the threats that could disrupt each function (see [[Risk Management Concepts]])
3. **Likelihood assessment** — estimate how probable each threat is
4. **Impact analysis** — quantify the consequence if the threat materializes
5. **Resource prioritization** — rank functions/assets by criticality to guide where recovery resources go first

As with general risk assessment, this can be done **quantitatively** (dollar figures — EF, SLE, ALE) or **qualitatively** (relative ratings); see [[Risk Assessment]] for those techniques and formulas in full.

## Continuity Metrics

The priorities stage produces the key time-based metrics that continuity planning is built around:

- **MTD (Maximum Tolerable Downtime)** — the longest a business function can be unavailable before causing unacceptable harm to the organization
- **RTO (Recovery Time Objective)** — the target time to restore a function or system after disruption; must be less than MTD
- **RPO (Recovery Point Objective)** — the maximum acceptable amount of data loss, measured as a point in time (e.g., "last night's backup")

MTD is the business constraint; RTO and RPO are the technical targets set to satisfy it.
