Not every subject is a person. Devices and software identities authenticate too, and they are usually the weakest-governed credentials in an environment — they do not forget passwords, so nobody notices they were never rotated.

## Device Authentication

The device itself proves identity before its user is even considered, so that a correct password from an unmanaged laptop is not enough.

- **Certificate-based** — a device certificate issued at enrollment, often protected by a **TPM** so the key cannot be copied to another machine. See [[Portable Devices and TPM]].
- **802.1X** — port-based network access control; the device authenticates to the switch or access point before the port opens. See [[Authentication Protocols]].
- **Device registration / MDM** — the device is enrolled, identified, and continuously checked for posture (patch level, encryption, jailbreak). See [[Mobile Device Deployment]] and [[Network Access Control and Endpoint Security]].
- **Device fingerprinting** — inferred identification from attributes; useful as a risk signal, trivially spoofed as a control.

**Device trust** is a pillar of zero trust: identity plus device health, evaluated per request rather than once at the perimeter.

## Service Authentication

**Service accounts**, machine identities, and workload identities authenticate services to each other with no human present.

- Use **certificates, API keys, or signed tokens**, not interactive passwords.
- Grant **least privilege** and scope to a single purpose; service accounts accumulate rights because nobody owns them.
- **Deny interactive logon** so the account cannot be used as a person.
- **Rotate automatically.** Static long-lived secrets in config files and scripts are the classic weakness — see [[Credential and Session Management]].
- Prefer **platform-managed identities** that issue short-lived credentials on demand, removing the stored secret entirely.
- Assign a **human owner** so the account appears in access reviews.

## Mutual Authentication

**Both parties prove identity to each other**, rather than only the client proving itself to the server. This is what defeats impostor servers: evil twin access points, phished login pages, and on-path interception.

Examples: **mutual TLS** (client and server certificates), **EAP-TLS**, **Kerberos** (the service also proves itself to the client), **MS-CHAPv2**. A server-only TLS handshake authenticates the server to the client — mutual TLS adds the reverse, which is why it is the common choice between services.

## Key Points

- **Device identity uses certificates, TPM-bound keys, and 802.1X; fingerprinting is a signal, not a control.**
- **Service accounts need least privilege, no interactive logon, an owner, and automatic rotation — short-lived managed identities are better than stored secrets.**
- **Mutual authentication means both sides prove identity, and it is what stops impostor servers.**
