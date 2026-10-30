## Overview

Application layer protocols define how applications exchange data: the request and response format, the commands, and the port they listen on. Most of the original TCP/IP application protocols send **credentials and content in cleartext**. For each one the useful knowledge is the port, what it does, whether it is secure, and what replaced it.

## The Common Protocols

| Protocol | Port | Purpose | Security status |
|---|---|---|---|
| **Telnet** | TCP 23 | Remote terminal access | Cleartext, including passwords. Replaced by **SSH** |
| **FTP** | TCP 20 (data), 21 (control) | File transfer with authentication | Cleartext. Replaced by **SFTP** (SSH, port 22) or **FTPS** (FTP over TLS, ports 989/990) |
| **TFTP** | UDP 69 | Trivial file transfer, no authentication | Used for booting devices and pushing configs; must be restricted to internal networks |
| **SMTP** | TCP 25 | Sending and relaying mail between servers | Cleartext unless **STARTTLS**; submission from clients uses 587 with TLS; implicit TLS 465 |
| **POP3** | TCP 110 | Retrieve mail, usually downloading and deleting from server | Cleartext; **POP3S** on 995 |
| **IMAP** | TCP 143 | Retrieve mail, keeping it on the server with folder sync | Cleartext; **IMAPS** on 993 |
| **DHCP** | UDP 67 (server), 68 (client) | Assigns IP address, mask, gateway, DNS automatically | No authentication: rogue DHCP servers can hand out malicious gateways and DNS. Defense: **DHCP snooping** on switches |
| **HTTP** | TCP 80 | Web content | Cleartext. Replaced by **HTTPS** |
| **HTTPS** | TCP 443 | HTTP over **TLS** | Confidentiality and integrity, server (and optionally client) authentication |
| **LPD** | TCP 515 | Line printer daemon, network print spooling | Legacy, no authentication |
| **X Window** | TCP 6000 to 6063 | Remote GUI display | Cleartext; should be tunneled through SSH |
| **NFS** | TCP/UDP 2049 | Network file system sharing (Unix) | Historically host-based trust only; use NFSv4 with Kerberos |
| **SNMP** | UDP 161 (agent), 162 (trap) | Monitoring and managing network devices | v1/v2 use cleartext **community strings** (default "public"/"private"); **SNMPv3** adds authentication and encryption |

The four to five mail and transfer protocols are the classic "which secure version replaces which insecure one" pairs: Telnet to SSH, FTP to SFTP/FTPS, HTTP to HTTPS, POP3/IMAP/SMTP to their TLS variants, SNMPv1/2 to SNMPv3.

## Patterns Across These Protocols

- **Cleartext credentials** are the common flaw: a sniffer on the path sees the password. The fix is either the TLS wrapped variant or tunneling over SSH/VPN.
- **No authentication of the server** (DHCP, TFTP, DNS) allows rogue servers. The fix is on the network side: switch features such as DHCP snooping, restricting the service to a management network, or DNSSEC.
- **Default configurations** (SNMP community strings, anonymous FTP, open relays on SMTP) are a configuration management problem more than a protocol problem.
- **Port numbers are identification, not security.** Moving a service to an unusual port hides it from casual scans only.

Email specifics, including SPF, DKIM, DMARC, S/MIME and PGP, are covered in [[Email Encryption]]. SSH, TLS and the other protective protocols are in [[Secure Communication Protocols]].

## Key Points

- **Telnet 23, SSH 22, FTP 20/21, SFTP 22, SMTP 25, POP3 110, IMAP 143, HTTP 80, HTTPS 443, DNS 53, DHCP 67/68, TFTP 69, SNMP 161/162.**
- **Every legacy protocol has a secure replacement**: usually the same protocol wrapped in TLS or carried over SSH.
- **SNMPv3 is the only SNMP version with authentication and encryption.**
- **DHCP and TFTP have no authentication**; the defense is network placement and switch features, not the protocol.
