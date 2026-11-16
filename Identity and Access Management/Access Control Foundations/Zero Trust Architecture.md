**Zero trust** replaces the idea of a trusted internal network with per-request evaluation: **"never trust, always verify"**. Being inside the perimeter grants nothing. The principle is introduced in [[Secure Design Principles]]; this note covers how it is built and enforced.

## Why the Perimeter Model Failed

The traditional model is a hard shell around a soft interior: authenticate once at the edge, then move freely. Three changes broke it.

- **The perimeter dissolved** — cloud services, remote work, and partner access mean most resources and many users are outside it.
- **One compromise became total** — an attacker who phishes a single user inherits a trusted position and moves east-west unopposed (see [[Network Segmentation]]).
- **Trust was implicit and permanent** — nothing re-checked the session after login.

Zero trust inverts all three: no implicit trust from location, the smallest possible unit of access, and continuous re-evaluation.

## Core Tenets

Drawn from **NIST SP 800-207**:

- Every **resource** is protected individually — data, services, devices, not network zones.
- **All communication is secured** regardless of network location; the internal network gets no discount.
- Access is granted **per session**, to **one resource**, and never implies access to another.
- The decision is **dynamic**, based on identity, device posture, behavior, and other context — this is attribute- and risk-based authorization (see [[Access Control Models]]).
- Nothing is permanently trusted: the organization **monitors the integrity and posture** of everything it owns and re-evaluates.
- Authentication and authorization are **strictly enforced before** access, and re-enforced continually during the session.
- The organization **collects telemetry** on the current state and uses it to improve policy.

## Policy Enforcement Architecture

Zero trust splits the decision from the enforcement, giving two planes:

| Component | Plane | Role |
|---|---|---|
| **Policy engine (PE)** | Control | **Makes** the decision — evaluates policy against identity, device state, threat intelligence, and risk score |
| **Policy administrator (PA)** | Control | **Executes** the decision — establishes or tears down the session and issues credentials or tokens to the PEP |
| **Policy enforcement point (PEP)** | Data | **Enforces** it on the path between subject and resource — gateway, proxy, agent, or service mesh sidecar |

The PE and PA together form the **policy decision point (PDP)**. The subject never reaches the resource directly; the PEP sits in front of it and holds the connection open only while the decision remains valid.

Feeding the policy engine: identity management, device inventory and endpoint posture, SIEM and threat intelligence, data classification, and the compliance requirements that apply. The decision is only as good as these inputs — **a zero trust rollout that lacks an accurate identity and asset inventory cannot work**, which is why those come first.

## Implementation

Zero trust is an architecture reached incrementally, not a product. The usual path:

1. **Identify the protect surface** — the specific data, applications, assets, and services worth defending. Smaller and better defined than the whole attack surface.
2. **Map the transaction flows** to those resources, so policy can be written against real traffic.
3. **Place enforcement close to the resource** — microsegmentation, identity-aware proxies, host firewalls (see [[Network Segmentation]]).
4. **Write least-privilege policy per resource**, in attribute terms rather than by network address.
5. **Monitor and refine continuously** — the telemetry is both the detection mechanism and the input for the next policy revision.

**SASE** delivers much of this from the cloud, enforcing policy near the user wherever they are; see [[Secure Design Principles]].

## Limits and Costs

- It does not remove the need for perimeter and network controls — it removes the assumption that passing them means anything.
- The **policy engine becomes the critical asset**: compromise it and every decision is attacker-controlled; lose it and nothing is reachable.
- Continuous verification has a user-experience cost, which is why risk-based step-up is preferred over constant re-prompting.
- Legacy applications that cannot express identity or attributes have to be fronted by a proxy or left in a segmented enclave.

## Key Points

- **Zero trust grants nothing based on network location; every request is authenticated, authorized, and encrypted.**
- **Access is per session and per resource, and never implies access to anything else.**
- **The policy engine decides, the policy administrator establishes the session, the policy enforcement point enforces it on the data path.**
- **The policy engine and administrator are the control plane; the PEP is the data plane.**
- **Decisions depend on identity, device posture, and risk — so accurate identity and asset inventories are the prerequisite.**
- **NIST SP 800-207 is the reference architecture.**
