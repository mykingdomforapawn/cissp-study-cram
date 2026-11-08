## Why Email Is Hard to Secure

Email is the most-used business application and the most common delivery path for attacks, because the protocols that carry it were designed for a cooperative network and assume good faith.

| Protocol | Role | Port (plain / TLS) |
|---|---|---|
| **SMTP** | **Sending** mail between clients and servers and between servers | 25 (server-to-server), 587 submission, 465 implicit TLS |
| **POP3** | **Downloading** mail to one client, typically removing it from the server | 110 / 995 |
| **IMAP** | **Accessing** mail kept on the server, synchronized across devices | 143 / 993 |

**MIME** defines how non-text content (attachments, HTML, encodings) is carried; **S/MIME** adds encryption and signatures on top of it (see [[Email Encryption]]).

None of these protocols authenticate the **sender of a message**. SMTP accepts whatever "From" address the sender writes, so **spoofing is a feature of the protocol**, not a bug in an implementation.

## Email Security Goals

Stated as the services that must be added, since the protocols provide none of them:

- **Confidentiality** of message content, in transit and at rest — message encryption (S/MIME, PGP) and TLS between servers.
- **Integrity**: the message was not altered — digital signatures.
- **Authentication of the sender**, and **non-repudiation** that they sent it — digital signatures again. Note that **SPF/DKIM/DMARC authenticate the sending domain, not the human**.
- **Availability** of the mail service, and **delivery assurance** where it is needed (delivery and read receipts, with the caveat that they are advisory).
- **Access control** over mailboxes, including delegated and shared mailboxes.
- **Classification and retention**: email is a records-management and eDiscovery problem as much as a security one — mail is **discoverable evidence** and needs a retention schedule that is actually enforced.

## Email Security Issues

- **Spoofing and business email compromise (BEC)**: forged or lookalike sender domains used to redirect payments or request data. BEC is a large, purely financial loss category and usually involves no malware at all.
- **Phishing and spear phishing**: credential harvesting and malware delivery, targeted or mass (see [[Social Engineering]]).
- **Malicious attachments and links**: macro documents, script files, archives hiding executables, and links to credential-harvesting pages.
- **Spam**: unsolicited bulk mail; the cost is bandwidth, storage, user time, and the attachments and links it carries.
- **Open relay**: a mail server that accepts and forwards mail from anyone to anyone. It will be found and used to send spam, and the organization's address space ends up **blacklisted**. Servers must relay only for authenticated users or their own domains.
- **Mail bombing**: flooding a mailbox or server to deny service.
- **Information leakage**: sensitive data sent to the wrong recipient (autocomplete), forwarded off-domain, or exposed in long quoted threads and metadata.
- **Lack of transit encryption**: SMTP between servers uses **opportunistic TLS**, which can be stripped; without it, mail crosses the internet in cleartext.
- **Hoaxes and chain mail**: minor, but they consume attention and train users to forward uncritically.

## Email Security Solutions

**Sender authentication** — three complementary DNS-based records, and the usual trio of answers:

| Mechanism | What it does | Limit |
|---|---|---|
| **SPF** (Sender Policy Framework) | A DNS record lists the **IP addresses allowed to send** for the domain; the receiver checks the connecting server against it | Breaks on forwarding; checks the envelope sender, not the visible From |
| **DKIM** (DomainKeys Identified Mail) | The sending server **signs** the message with a private key; the public key is in DNS, so the receiver verifies integrity and origin | Survives forwarding but says nothing about what to do on failure |
| **DMARC** | Ties SPF and DKIM to the **visible From domain** (alignment), tells receivers what to do on failure (**none / quarantine / reject**), and provides **reporting** back to the domain owner | Only protects exact-domain spoofing; lookalike domains are unaffected |

**Message-level cryptography**: **S/MIME** (PKI, enterprise) and **PGP** (web of trust) for confidentiality, integrity, authentication, and non-repudiation end to end — detail in [[Email Encryption]]. Transit encryption (**STARTTLS**, with **MTA-STS** to prevent downgrade) protects the hop, not the message at rest.

**Gateway and content controls**: a **secure email gateway** doing spam filtering (reputation, heuristics, Bayesian), anti-malware scanning, **sandbox detonation** of attachments, URL rewriting and time-of-click checking, **DLP** on outbound mail, attachment-type blocking, and external-sender banners. Greylisting and blacklists/whitelists are the older building blocks.

**Infrastructure hygiene**: no open relays, authenticated submission, patched mail servers, hardened webmail with MFA (a stolen mailbox password is the start of most BEC), restricted auto-forwarding to external domains, and logging of mail flow.

**People and process**: awareness training with simulated phishing, an **easy reporting path** for suspicious mail, and out-of-band verification for payment and credential requests — the only real control against BEC, since it carries no technical indicator.

## Key Points

- **SMTP, POP3, and IMAP have no sender authentication and no encryption by default; spoofing is inherent to the protocol.**
- **SPF lists allowed sending IPs, DKIM signs the message, DMARC aligns them with the visible From and sets the policy (none/quarantine/reject) plus reporting.**
- **S/MIME and PGP protect the message end to end; TLS only protects a hop.**
- **An open relay will be abused for spam and gets the domain blacklisted.**
- **BEC is a financial attack with no malware; out-of-band verification, not filtering, is the control.**
- **Email is discoverable evidence and needs a retention policy.**
