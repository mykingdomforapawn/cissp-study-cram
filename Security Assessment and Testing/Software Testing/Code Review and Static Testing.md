Software testing splits along one fundamental line: **static** techniques examine code **without running it**; **dynamic** techniques examine software **while it runs** (see [[Dynamic Testing and Fuzzing]]). Static testing catches flaws earliest, where they are cheapest to fix (see [[Information System Lifecycle]]).

## Code Review

**Code review** is the single most effective software assurance technique, and it is a human activity: developers other than the author read the code looking for defects.

Forms, from least to most formal:

- **Pair programming** — two developers at one workstation; review is continuous and informal.
- **Over-the-shoulder** — the author walks a colleague through the change.
- **Pass-around / tool-assisted review** — the change is distributed, commonly through a pull request, and reviewed asynchronously. The normal modern practice.
- **Formal inspection** — a structured meeting with defined roles and entry and exit criteria.

### Fagan Inspection

The **Fagan inspection** is the most formal and rigorous review process, with six defined steps:

| Step | Purpose |
|---|---|
| **1. Planning** | Assemble the team, assign roles, confirm the material meets entry criteria |
| **2. Overview** | The author explains the code's purpose and design to the inspectors |
| **3. Preparation** | Inspectors **individually** study the material beforehand — the step that does the real work |
| **4. Inspection** | The team meets and walks the material systematically, **identifying defects without fixing them** |
| **5. Rework** | The author corrects the defects found |
| **6. Follow-up** | The moderator verifies the rework is complete and correct, closing the loop |

Two properties define it: inspectors **prepare individually before the meeting**, and the meeting **finds defects rather than solving them** — debating fixes in the room destroys the throughput that makes inspection work.

Its cost is why it is reserved for high-assurance code — safety-critical systems, cryptographic implementations, authentication logic — rather than applied everywhere.

## Static Application Security Testing

**SAST** tools analyze source code, bytecode, or binaries automatically, without execution. They trace data flow from untrusted inputs (sources) to dangerous operations (sinks) to find injection flaws, buffer issues, hardcoded secrets, unsafe API use, and weak cryptography.

Strengths and limits:

- **Full code coverage is possible** — the tool sees every path, including those no test case exercises.
- **Findings point to an exact line**, so remediation is direct.
- **It runs early**, before anything is deployed, and fits naturally into CI pipelines (see [[Microservices, IaC, and Immutable Architecture]]).
- **It produces many false positives**, because it cannot know which paths are actually reachable or which inputs are already validated elsewhere.
- **It cannot find runtime, configuration, or environment flaws** — the deployed system is not what it examined.
- **It cannot find business logic flaws**, because it has no notion of what the application is supposed to do.

**Static and dynamic testing are complementary, not alternatives**: static sees all the code but not the running system; dynamic sees the running system but only the paths it reaches.

## Key Points

- **Static testing examines code without executing it; dynamic testing examines software while it runs.**
- **Manual code review by someone other than the author is the most effective software assurance technique.**
- **The Fagan inspection is the most formal review, with six steps: planning, overview, preparation, inspection, rework, follow-up.**
- **Fagan inspectors prepare individually beforehand, and the inspection meeting identifies defects rather than fixing them.**
- **SAST can achieve full code coverage and points to exact lines, but generates many false positives.**
- **Static testing cannot find runtime, configuration, or business logic flaws — which is why dynamic testing is also required.**
