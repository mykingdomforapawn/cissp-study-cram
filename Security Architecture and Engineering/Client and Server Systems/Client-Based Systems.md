A client is the endpoint that a user works on: a PC, laptop, phone, or browser. It runs code and keeps data locally, and it is usually the least controlled and most exposed part of a system. Two client-side concerns are code that arrives from elsewhere and runs locally, and data the client keeps for speed.

## Mobile Code

**Mobile code** is code that is downloaded from a remote system and executed on the client, usually automatically and with little or no user involvement. Examples are **Java applets**, **ActiveX** controls, **JavaScript** and other scripts in web pages, **WebAssembly**, browser extensions, and macros embedded in documents.

The risk is that the code runs on the user's machine with the user's privileges, and the user often does not know it is there. A malicious or compromised site can use it to steal data, install malware (**drive-by download**), or track the user.

| | Java applet | ActiveX control |
|---|---|---|
| **Origin** | Sun/Oracle Java, runs in the Java virtual machine | Microsoft, runs as native code in Internet Explorer |
| **Protection** | **Sandbox** that confines the applet and limits its access to the client's files and system | **Digital signature** that identifies the publisher, and no sandbox |
| **Consequence** | A flaw in the sandbox or JVM is needed to escape | Once the user trusts and runs it, it has the user's full privileges |

Applets, ActiveX, and Flash are all deprecated: modern browsers do not support Java or Flash natively, Flash is abandoned and actively blocked, and ActiveX only ever ran in Internet Explorer on Windows, not in current browsers such as Edge. **JavaScript** is the mobile code that remains in every modern browser, so it is now the main one to control. They show the two possible defenses: **confine** the code (sandbox) or **trust** the publisher (signing). Signing proves who wrote the code, not that it is safe (see [[Digital Signatures]]). Confinement is the stronger of the two (see [[Techniques for Ensuring CIA]]).

Don't confuse an applet with a **servlet**: an applet is code sent to the *client* and run there, while a servlet runs on the *server*.

**Controls:**
- Run code in a sandbox, and keep browsers and plug-ins patched.
- Remove or disable unneeded plug-ins and scripting, and use script blockers.
- Allow only signed code from trusted publishers, and use application allow lists.
- Apply content security policies and web filtering, and endpoint protection.
- Disable macros in documents by default.

## Local Caches

A **cache** is a local copy of data kept so it does not have to be fetched again. Clients keep several, and each can be poisoned, read, or left behind.

| Cache | Holds | Attack or exposure |
|---|---|---|
| **ARP cache** | Mappings of IP addresses to MAC addresses on the local network | **ARP cache poisoning**: forged replies make the client send traffic to the attacker's MAC address, which enables man-in-the-middle and denial of service |
| **DNS cache** | Mappings of names to IP addresses | **DNS cache poisoning**: false answers send the client to an attacker's server for a legitimate name (**pharming**) |
| **Browser / temporary internet files** | Pages, images, and scripts already viewed | Sensitive pages and files remain on disk after the session, which is a risk on shared or lost machines |
| **Credential and offline file caches** | Cached logon credentials and offline copies of server files | Stolen credentials or data from a lost device |

A poisoned entry keeps working until it expires or is flushed (its **time to live**), so one forged answer can affect many connections.

**Controls:**
- **ARP:** static entries for critical hosts, and switch features that validate ARP traffic (such as dynamic ARP inspection).
- **DNS:** authenticated DNS responses (**DNSSEC**), trusted resolvers, and encrypted DNS.
- **Browser:** instruct pages not to be cached (such as `no-store`), clear the cache at logoff, and use private browsing on shared machines.
- **Local data:** full-disk encryption, and wiping or reimaging devices before reuse (see [[Data Storage Devices]]).

## Key Points

- **Today's concern is JavaScript.** Java applets, ActiveX, and Flash are deprecated or unsupported in current browsers.
- **Mobile code runs locally with the user's privileges**, so it needs confinement or trust. Applets use a sandbox, ActiveX relies on signing.
- **A signature identifies the author, not the safety of the code.**
- **Applet is client-side, servlet is server-side.**
- **Caches hold trust.** Poisoning an ARP or DNS cache redirects traffic, and browser caches leave data behind on the device.
