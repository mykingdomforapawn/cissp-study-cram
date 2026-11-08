## The Problem

**Remote access** means a user or system outside the physical perimeter reaching internal resources. It moves the trust boundary from the building to an endpoint the organization does not physically control, on a network it does not run. Every control that depended on "being in the office" — physical access, network location, shoulder-surfing-free space, managed printers — must be re-established by other means.

**Telecommuting** (telework) is the organizational form of this: working from home, a client site, a hotel, or on the road.

## Remote Access Techniques

The three techniques differ in **where the data and the processing actually live**.

| Technique | How it works | Risk profile |
|---|---|---|
| **Service-specific** | The remote user reaches **one application or protocol only** — webmail, a published app, an API | Smallest attack surface; no general network access |
| **Remote control** | The remote user takes over a **physical or virtual desktop inside** the network (RDP, VNC, VDI, remote assistance). Only screen, keyboard, and mouse cross the link | Data stays inside; the endpoint is a thin terminal. Risks: credential theft gives a full interactive session, and clipboard/drive redirection reopens the data path |
| **Remote node** | The remote device becomes a **full member of the network** (the classic VPN client) and runs applications locally on its own data | Largest exposure: the untrusted endpoint is inside the network, and data lands on it |

A **screen scraper** reads a screen's contents programmatically — legitimately for terminal emulation and automating systems with no API, illegitimately as the mechanism behind remote-control spyware. Screen content is itself an exfiltration channel: a remote-control session that keeps data inside still shows the data.

Choosing between them is a trade-off between **convenience and data location**. If data must not leave the datacenter, remote control or published applications beat remote node.

## Remote Connection Security

- **Encrypt the channel**: VPN, TLS, or SSH. Never a protocol that exposes credentials or data in transit — see [[Virtual Private Networks]].
- **Strong authentication**: **MFA is the baseline** for remote access, because a password alone is exposed to phishing, reuse, and keylogging with no compensating physical control. Certificates or device identity authenticate the machine as well as the user.
- **Callback** is the legacy control: the server hangs up and dials the user back at a **pre-registered number**, proving location. Defeated by **call forwarding** and useless for mobile users; it is authentication by location.
- **Caller ID filtering** is the weaker relative — spoofable.
- **Endpoint posture**: patch level, disk encryption, anti-malware, screen lock, no split tunnel on an unmanaged device.
- **Restricted landing zone**: terminate remote sessions in a segment with its own rules rather than the flat internal LAN.
- **Session controls**: idle timeout, re-authentication, concurrent-session limits, and logging of who connected from where.

## Planning a Remote Access Policy

A remote access policy answers four questions explicitly, so that access is granted by rule rather than by request:

1. **Who** may work remotely, and for which roles and data classifications — remote work is not automatically appropriate for every job.
2. **What** may be used: corporate device only, or BYOD under conditions (see [[Mobile Device Deployment]]); which applications; whether data may be stored locally or printed at home.
3. **How** the connection is made: which VPN or portal, which authentication, full vs split tunnel, no untrusted public Wi-Fi without the tunnel.
4. **What protections are required** at the remote site: disk encryption, lock screens, physical security of the device and of printed material, separation from family-shared computers, and secure disposal of printouts.

It must also cover **failure and exit**: reporting and wiping a lost device, and revoking access on termination. Two things are easy to forget — who supplies the hardware, software, and connectivity, and the **training and awareness** that office workers absorb by proximity.

## Network Administrative Functions and Management

Remote administration is remote access with the highest possible privilege, so it gets extra controls:

- **Out-of-band management**: administer devices over a path separate from the production network (dedicated management network, console server, or a cellular/dial backup) so that administration survives an outage and is not reachable from user segments.
- **Jump host / bastion / privileged access workstation**: admins connect to one hardened, heavily logged system and from there to targets, rather than reaching devices directly.
- **Encrypted management protocols only**: SSH, HTTPS, SNMPv3 — never Telnet, HTTP, or SNMPv1/v2.
- **Session recording and command logging** for privileged sessions, with TACACS+ providing per-command authorization (see [[Authentication Protocols]]).

**Monitoring and management** of the network more broadly means keeping a current picture of what is on it and how it behaves: configuration backups and versioning, change control for every device change, synchronized time (**NTP**) so logs correlate, and centralized collection of syslog, SNMP traps, and flow records. The operational detail is in [[Network Devices]]. The monitoring infrastructure itself is a high-value target, since it holds credentials for everything.

## Third-Party Connectivity

Partners, suppliers, managed service providers, and customers often need a connection into the network. Each one is a **trust relationship that bypasses the perimeter**, and the organization inherits the weaker party's security.

- **Formalize it before connecting**: an agreement covering security requirements, permitted access, incident notification, audit rights, and termination. **ISA** (interconnection security agreement) describes the technical connection; MOU/MOA, SLA, and contracts cover the relationship (see [[Vendor, Consultant, and Contractor Agreements]]).
- **Assess the third party** before and periodically after connection, and treat their compromise as a plausible path into you — the supply chain attack pattern in [[Supply Chain Risk Management]].
- **Isolate the connection**: terminate it in an **extranet** segment with explicit rules for exactly the systems and ports needed, never flat internal access (see [[Network Segmentation]]).
- **Identify and log individually**: named accounts for vendor staff, not a shared one; MFA; time-limited or just-in-time access rather than standing access.
- **Plan the disconnection**: links that outlive the contract are a recurring finding. Termination of the relationship must revoke the access.

## Key Points

- **Service-specific = one application; remote control = taking over a desktop inside the network (data stays in); remote node = the device joins the network as a full member (data leaves).**
- **MFA plus an encrypted tunnel is the baseline for remote access; callback authenticates by location and is defeated by call forwarding.**
- **A remote access policy names who may connect, with what device, how, and what protections are required at the remote site — including device loss and termination.**
- **Administer devices out-of-band through a jump host with encrypted protocols and per-command logging.**
- **Third-party connections inherit the partner's security: contract first, isolate into an extranet, name and time-limit accounts, and disconnect when the relationship ends.**
