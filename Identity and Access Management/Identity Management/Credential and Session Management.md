Credentials have to be stored, issued, replaced, and retired, and authenticated sessions have to be ended. Both are places where an otherwise sound authentication design leaks.

## Credential Management Systems

An enterprise **credential management system** is the authoritative store and issuing mechanism for credentials — enterprise password vaults, PAM (privileged access management) systems, key and secret stores.

- Credentials are held **encrypted and centrally**, released to a subject only after that subject authenticates to the vault.
- **Check-out / check-in** of privileged accounts, with automatic **rotation after each use**, so a shared administrator password is never persistently known.
- **Session recording and command logging** for privileged access, giving accountability for shared accounts.
- Strong authentication to the vault itself, because the vault is now the whole organization's single point of compromise.
- A **break-glass** account exists for vault outages, stored offline and alarmed on use.

**CMS** in the smartcard sense also means a **credential management system** for certificate and card lifecycle: issuance, renewal, revocation, and replacement of lost cards, tied to [[Public Key Infrastructure]].

## Credential Manager Applications

The user-level equivalent: browser and standalone **password managers** that store per-site credentials under one master secret.

- Enable long, unique, random passwords per site — the single most effective fix for credential reuse.
- Automatic form filling is also a **phishing defense**: the manager will not fill a credential on the wrong domain.
- Risk concentrates on the **master password and the device**; a compromised endpoint or master secret exposes everything. Protect the vault with MFA, and prefer managed enterprise deployments over unvetted personal apps.

## Scripted Access

**Scripted access** automates a login sequence — logon scripts, batch jobs, scheduled tasks, automation and CI pipelines.

The problem is **hardcoded credentials**: a password in a script is stored in cleartext, copied into version control and backups, readable by anyone who can read the file, and effectively never rotated. Mitigations, best first:

1. Replace the secret with a **platform-managed identity** issuing short-lived tokens.
2. Fetch the secret at runtime from a **vault**, never store it in the script.
3. If a stored credential is unavoidable: restrict file permissions, scope the account minimally, and rotate on a schedule.

See [[Device and Service Authentication]].

## Session Management

A session persists authentication, so an unattended or stolen session bypasses every control at the front door.

- **Idle (inactivity) timeout** — terminate or lock after a period of no activity.
- **Absolute session timeout** — end the session regardless of activity, forcing reauthentication.
- **Screen savers and automatic device locks** with password resume, plus a **clean desk / lock-your-screen** policy.
- **Reauthentication for sensitive actions**, independent of session age.
- **Explicit logout that invalidates server-side state**, not merely the client's cookie.
- **Secure session tokens**: high entropy, transmitted over TLS, `HttpOnly` and `Secure` cookies, **regenerated at login** to prevent session fixation, and bound where possible to the client. See [[Web Applications]] and [[Network Attacks]] for hijacking and fixation.

Federated sessions add a second layer: ending the IdP session does not necessarily end the SP sessions it created, which is what **single logout** addresses — imperfectly, which is why short SP session lifetimes matter.

## Key Points

- **Privileged vaults check out accounts and rotate them after use, so shared passwords are never persistently known.**
- **Password managers fix reuse and resist phishing by domain matching; the master secret becomes the concentrated risk.**
- **Hardcoded credentials in scripts are the classic weakness — use managed identities or runtime vault retrieval.**
- **Idle timeout, absolute timeout, screen lock, and server-side invalidation on logout; regenerate the session ID at login.**
