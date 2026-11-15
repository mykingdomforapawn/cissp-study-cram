**Federation** extends SSO **across organizational boundaries**. Users authenticate to their own organization and are accepted by a partner's or a cloud provider's systems, with **no account or password held by the relying party**.

Three roles:

- **Identity provider (IdP)** — authenticates the user and asserts their identity and attributes.
- **Service provider (SP) / relying party (RP)** — consumes the assertion and grants access.
- **Federation trust** — the agreed relationship, backed by exchanged signing certificates and metadata, plus a legal agreement on identity vetting, attribute meaning, and incident notification.

From the user's side nothing changes: they keep logging in with their **existing organizational account**, and the federation service brokers that identity to the partner — no second account is issued to them, whatever the deployment model.

The security model: the SP never sees the credential, and revoking the account at the IdP cuts access everywhere — provided session lifetimes are short enough to matter.

## Protocols

| Protocol | Purpose | Format |
|---|---|---|
| **SAML 2.0** | Federated **authentication** (and attributes) between enterprises | XML assertions |
| **OAuth 2.0** | **Authorization** — delegated access to resources on a user's behalf; it does *not* authenticate the user | Access tokens |
| **OpenID Connect (OIDC)** | **Authentication layer on top of OAuth 2.0**; adds an identity token | JSON / JWT |
| **SCIM** | **Provisioning** — pushing account creation, updates, and deletion between IdP and SP | JSON over REST |

**SAML authenticates, OAuth authorizes, OIDC adds authentication to OAuth, SCIM provisions.** Using OAuth alone as a login mechanism is the classic design error — the token proves access was granted, not who the user is.

## Deployment Models

| Model | Where identities live | Fits |
|---|---|---|
| **On-premise federation** | Internal directory and federation server, assertions issued outward | Existing directory investment, data residency requirements |
| **Cloud-based federation** | Identity-as-a-service (IDaaS) provider holds or brokers identities | Cloud-first organizations; shifts availability and trust to a third party |
| **Hybrid** | On-premise directory remains authoritative, synchronized or federated to a cloud IdP | Most enterprises in transition; the sync link becomes critical infrastructure |

The cloud models move an authentication outage and an identity breach into a **third party's** hands — a vendor risk to manage like any other (see [[Supply Chain Risk Management]]).

## Just-in-Time Provisioning

With **JIT provisioning**, the SP creates the account **at first successful login**, from the attributes in the assertion, instead of being pre-populated.

- Removes the need to create accounts in advance and keeps attributes fresh at each login.
- Cost: accounts exist only where someone has logged in, and **deprovisioning is not automatic** — JIT creates but does not delete. Pair it with SCIM or periodic review (see [[Identity and Access Provisioning Lifecycle]]).

## Key Points

- **Federation = SSO across organizations; the IdP authenticates, the SP trusts the assertion and holds no credential.**
- **SAML authenticates, OAuth 2.0 authorizes, OIDC is authentication on top of OAuth, SCIM provisions.**
- **On-premise, cloud, and hybrid federation differ in who holds the identities and therefore who holds the risk.**
- **JIT provisioning creates accounts at first login but does not remove them.**
