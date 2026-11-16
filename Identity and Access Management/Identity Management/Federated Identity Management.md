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

### XML as the Substrate

**XML** (Extensible Markup Language) is the data format the enterprise federation protocols were built on. Unlike HTML, which describes presentation with a fixed tag set, XML lets the parties **define their own tags** and so carry arbitrary structured attributes — department, clearance, entitlement — alongside the identity. That extensibility is what made it the basis for **SAML** assertions and for **SPML** (provisioning, now largely displaced by SCIM) and **XACML** (expressing authorization policy). The newer protocols moved to **JSON and JWT**, which carry the same information far more compactly.

A SAML assertion is a **signed XML document** making one or more statements about a subject:

- **Authentication statement** — this subject authenticated, at this time, by this method.
- **Attribute statement** — these are the subject's attributes (group, role, email).
- **Authorization decision statement** — this subject may or may not perform this action.

The signature is what makes the assertion trustworthy; **XML signature wrapping**, where an attacker relocates a signed element and adds forged content, is the characteristic attack, and strict schema validation is the defense.

### OAuth 2.0 Roles

OAuth's vocabulary is worth having straight, because the delegation idea lives in it:

| Role | Who it is |
|---|---|
| **Resource owner** | The user, who owns the data |
| **Client** | The application requesting access on the user's behalf |
| **Authorization server** | Issues the access token after the user consents |
| **Resource server** | Holds the data and accepts the token |

The user **consents to a scope** — a bounded set of permissions — and the client receives a token rather than the user's password. The token should be short-lived, paired with a refresh token, and bound to the scope granted. **OIDC** adds an **ID token** (a signed JWT describing who the user is) on top of this flow, which is precisely what plain OAuth lacks.

### Comparing the Four

| | SAML 2.0 | OAuth 2.0 | OIDC | SCIM |
|---|---|---|---|---|
| **Answers** | Who is this user? | May this app act for the user? | Who is this user? | Which accounts should exist? |
| **Format** | XML assertion | Access token | JWT ID token | JSON over REST |
| **Typical use** | Enterprise web SSO | API and third-party app delegation | Consumer and modern app login | Automated provisioning and deprovisioning |
| **Era** | Enterprise, browser-based | Mobile and API | Mobile and API | Any |

**If the stem says delegated access or "on behalf of", it is OAuth; if it says login or identity, it is SAML or OIDC; if it says account creation or removal, it is SCIM.**

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
- **SAML assertions are signed XML making authentication, attribute, or authorization statements; OAuth and OIDC use JSON tokens.**
- **OAuth roles: resource owner, client, authorization server, resource server — the user consents to a scope and the client gets a token, never the password.**
