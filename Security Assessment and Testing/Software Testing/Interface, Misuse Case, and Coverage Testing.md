Beyond static and dynamic analysis of code, three techniques address what those miss: **the seams between components**, **what an attacker would do**, and **how much of the code was tested at all**.

## Interface Testing

Modern systems are assemblies of components, and **defects concentrate at the boundaries between them** — where one team's assumptions meet another's. Interface testing exercises those boundaries explicitly, rather than testing each component in isolation and assuming they fit.

Three interface categories:

| Interface | What is tested |
|---|---|
| **Application Programming Interfaces (APIs)** | The contract exposed to other software: authentication, authorization on every call, parameter validation, error handling, rate limiting, versioning |
| **User interfaces (UIs)** | What a human touches — GUI, CLI, web. Includes whether client-side validation is enforced again on the server |
| **Physical interfaces** | Connections to hardware and the physical world — critical in ICS, SCADA, and embedded systems where a software defect moves something (see [[Industrial Control Systems]]) |

The security point about APIs: **a control enforced in the user interface is not enforced at all if the API beneath it can be called directly.** Interface testing is how that gap is found.

It matters most in microservices and integration-heavy architectures, where components are deployed independently and a change on one side can silently break the contract on the other (see [[Microservices, IaC, and Immutable Architecture]]).

## Misuse Case Testing

A **use case** describes what a user is supposed to do. A **misuse case** (or abuse case) describes **what an attacker would try to do** — and testing them means deliberately attempting those actions to confirm the system refuses.

The method:

1. Model the normal use cases.
2. Identify the **misuse cases** that threaten them — who would attack this, and how.
3. Test that the system **blocks, detects, and logs** each attempt.

Examples: submitting someone else's order ID to see another customer's data; replaying a password reset token; ordering a negative quantity to produce a refund; skipping directly to the payment-confirmation step.

Misuse case testing is the **testing-phase counterpart to [[Threat Modeling]]**, which does the same reasoning at design time. Its particular value is finding **business logic flaws** — defects that are invisible to scanners and static analysis because the code is working exactly as written, just permitting something it should not.

## Test Coverage Analysis

**Coverage analysis measures how much of the software the tests actually exercised**, expressed as:

```
coverage = ( items tested / total items ) × 100
```

Coverage criteria, roughly from weakest to strongest:

| Criterion | Requires |
|---|---|
| **Statement (line)** coverage | Every line of code executed at least once |
| **Branch (decision)** coverage | Every decision evaluated **both true and false** |
| **Condition** coverage | Every individual boolean sub-expression evaluated both ways |
| **Loop** coverage | Loops executed zero times, once, and many times |
| **Function** coverage | Every function or procedure called at least once |

The essential caution: **coverage measures what was executed, not what was verified.** A test suite can run every line while asserting almost nothing, and 100% coverage says nothing about whether the behaviour is correct or whether the right cases were chosen.

Low coverage, however, is a reliable warning — **untested code is where defects survive**, and security-critical paths such as error handling, authentication failure, and authorization denial are precisely the branches that normal testing tends to leave unexecuted.

## Key Points

- **Interface testing exercises the boundaries between components — APIs, user interfaces, and physical interfaces — where assumptions clash and defects concentrate.**
- **A control enforced only in the user interface is not enforced, because the API beneath it can be called directly.**
- **Misuse case testing deliberately attempts what an attacker would do and verifies the system blocks, detects, and logs it.**
- **Misuse case testing is the test-phase counterpart to design-time threat modeling, and is the main way business logic flaws are found.**
- **Coverage analysis reports the percentage of items exercised: statement, branch, condition, loop, and function coverage.**
- **Branch coverage requires every decision to be evaluated both true and false, making it stronger than statement coverage.**
- **Coverage measures what was executed, not what was verified — 100% coverage does not mean correct behaviour.**
