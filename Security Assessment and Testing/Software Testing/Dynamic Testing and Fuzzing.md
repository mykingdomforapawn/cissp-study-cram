**Dynamic testing** evaluates software **as it runs**, in a live or staging environment, without needing the source code. It is the complement to the static techniques in [[Code Review and Static Testing]]: it sees the real, deployed, configured system, but only the paths its inputs actually reach.

## Dynamic Application Security Testing

**DAST** tools interact with a running application the way a user or attacker would, submitting input and observing responses. For web applications this is the web vulnerability scanning described in [[Vulnerability Scanning]].

- It tests the system **as deployed** — including server configuration, platform patch level, and runtime behaviour that static analysis cannot see.
- It needs **no source code**, so it works against third-party and black-box software.
- Its findings are **concrete** — a reproduced response, not a theoretical path — so false positives are fewer.
- But it covers **only the paths it reaches**: untested branches, error handlers, and administrative functions behind authentication are easily missed.
- And it can **modify or destroy data**, since the inputs it submits are real. **Dynamic testing belongs in a test environment**; running it against production risks both damage and misleading results.

### Synthetic Transactions

A **synthetic transaction** is a scripted, artificial interaction run against an application to verify it behaves correctly — logging in, searching, adding an item to a cart, completing a checkout against a test account. They are used both as a testing technique and, run continuously, as monitoring.

## Fuzz Testing

**Fuzzing** submits large volumes of **invalid, unexpected, malformed, or random** input to find inputs the software does not handle safely — crashes, hangs, memory corruption, or unhandled exceptions. It is looking for **failures of input handling**, which is where a large share of exploitable vulnerabilities live.

Two approaches:

| Type | How inputs are produced | Characteristics |
|---|---|---|
| **Mutation fuzzing** (dumb fuzzing) | Takes **real, valid sample inputs** and slightly modifies them — **bit flipping** and similar random alterations | Trivial to set up — needs only sample data, no knowledge of the format. Less efficient; deep paths behind checksums or strict parsing are rarely reached |
| **Generational fuzzing** (intelligent fuzzing) | **Builds inputs from scratch** using a model or specification of the expected format | Requires effort to model the protocol or format, but produces structurally valid inputs that pass early validation and reach far deeper code |

**Mutation modifies existing samples; generational constructs new ones from a model of the format.** Generational is more effective and more expensive.

**Zzuf** is a well-known mutation fuzzing tool. **Prefuzzing** — altering sample inputs before the run begins — is a technique for improving a mutation fuzzer's reach.

A fuzzer reports that the software **failed**, not why. Each crash still needs triage to determine whether it is exploitable, which is why fuzzing output is an input to analysis rather than a finished finding.

## Website Monitoring

Monitoring a live application continuously, rather than testing it in a window, comes in two forms:

| Approach | Mechanism | Sees |
|---|---|---|
| **Passive monitoring** — also **real user monitoring (RUM)** | Captures and analyzes the **actual traffic of real users**, through network capture or instrumentation in the page | What users genuinely experience, including conditions nobody thought to test. **Reactive** — a problem is observed only after it has already affected someone |
| **Synthetic monitoring** — also **active monitoring** | Runs **scripted synthetic transactions** on a schedule from defined locations | Problems **before a real user hits them**, and covers low-traffic paths. **Proactive**, but only measures what was scripted |

**Passive monitoring is reactive and reflects real experience; synthetic monitoring is proactive and covers only scripted paths.** A mature practice runs both: RUM to learn what is actually happening, synthetic transactions to catch outages on critical paths during quiet periods.

## Key Points

- **Dynamic testing runs the software and needs no source code; it tests the system as deployed, including configuration.**
- **Dynamic testing covers only the paths it reaches and can modify or destroy data, so it belongs in a test environment.**
- **Fuzzing submits invalid, unexpected, or random input to find input-handling failures.**
- **Mutation (dumb) fuzzing slightly modifies previously used inputs by bit flipping and similar alterations; generational (intelligent) fuzzing builds inputs from a model of the expected format and reaches deeper code.**
- **A fuzzer reports that software failed, not whether the failure is exploitable — each crash needs triage.**
- **Passive monitoring (RUM) analyzes real user traffic and is reactive; synthetic monitoring runs scripted transactions and is proactive.**
