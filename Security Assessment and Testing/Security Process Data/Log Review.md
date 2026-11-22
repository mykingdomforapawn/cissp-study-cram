Logs are the raw material of **accountability** — the final A of the [[AAA Framework]]. Collecting them is necessary but not sufficient: **a log nobody reviews provides no detective control**, only evidence after the fact. Log review is the process that turns stored records into detection. The operational monitoring built on top of this belongs to security operations; this note covers the review process itself.

## What Log Review Is For

- **Detecting incidents** that preventive controls did not stop — the detective control.
- **Supporting investigation** after an event, by reconstructing what happened and in what order.
- **Verifying that controls operate** — evidence for assessments and audits (see [[Security Testing, Assessment, and Audit]]).
- **Demonstrating compliance**, where retention and review are mandated (see [[Compliance]]).

**NIST SP 800-92** is the reference guide for computer security log management.

## Trustworthy Logs

A log is only as good as its integrity, because the first thing a competent attacker does is edit or delete it.

- **Centralize immediately** — forward records to a separate log server or SIEM as they are generated, so local deletion on a compromised host does not destroy the record.
- **Protect from modification** — write-once storage, append-only transport, restricted access. **Administrators of a system should not be able to alter that system's logs**, or the log cannot be used as evidence against them (a separation of duties argument).
- **Synchronize clocks** via NTP. **Without a common time base, records from different systems cannot be correlated**, which destroys most of the investigative value.
- **Retain for a defined period**, set by regulation, investigative need, and storage cost. Too short loses evidence of slow-moving intrusions; too long raises cost and privacy exposure.
- **Record enough** — timestamp, source, user or process identity, action, target, and outcome. Logs that record success but not failure miss the attack in progress.

## Doing the Review

The volume problem is the central difficulty: no organization can read everything it logs.

- **Automated analysis first.** A **SIEM** aggregates, normalizes, and correlates records across sources, raising alerts on rules and anomalies. Automation handles the volume; humans handle the judgement.
- **Sampling** reviews a representative subset when full review is impractical. It is a reasonable assurance measure, but it is **statistical, so it will miss individual events** and cannot be relied on to catch a targeted attack.
- **Clipping levels** suppress routine noise by setting a threshold below which activity is not reported — a handful of failed logins is normal, thirty in a minute is not. The threshold is the trade-off: set too high, real attacks hide beneath it; set too low, analysts drown and begin ignoring alerts.
- **Prioritize by sensitivity.** Privileged account activity, authentication failures, configuration and policy changes, and access to classified data warrant closer and more frequent review than routine traffic.

**Reviewing privileged user activity is a specific control requirement**, because administrators hold the access that other controls cannot restrain — their actions are governed by monitoring rather than prevention.

## Key Points

- **Logs provide accountability, but a log nobody reviews is not a detective control.**
- **NIST SP 800-92 is the guide to security log management.**
- **Forward logs to a central server or SIEM immediately so a compromised host cannot destroy the record.**
- **System administrators must not be able to modify that system's own logs, or the logs cannot serve as evidence against them.**
- **Clock synchronization via NTP is required, or records from different systems cannot be correlated.**
- **Sampling is statistical and will miss individual events; clipping levels suppress routine noise but hide real attacks if set too high.**
- **Privileged user activity requires specific, closer review, because monitoring is the control that governs administrators.**
