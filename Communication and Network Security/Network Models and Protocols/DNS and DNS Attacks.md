## How DNS Works

The **Domain Name System** translates human-readable **fully qualified domain names (FQDNs)** into IP addresses (and back). An FQDN has a hostname, a domain, and a top-level domain (www.example.com.). It is a **distributed, hierarchical database**: root servers point to TLD servers, which point to the **authoritative** name servers for each domain.

A client's **stub resolver** asks a **recursive resolver** (the ISP's or the company's), which walks the hierarchy on the client's behalf and **caches** the answer for the record's **TTL**. Queries normally use **UDP 53**; zone transfers and large responses use **TCP 53**.

Common record types: **A** (IPv4), **AAAA** (IPv6), **CNAME** (alias), **MX** (mail server), **NS** (name server), **PTR** (reverse lookup), **TXT** (free text, used for SPF/DKIM/DMARC), **SOA** (zone authority).

Before DNS, name resolution used a local **hosts file**, which still exists and is still consulted **before** DNS on every operating system. That is why it is an attack target.

DNS was designed without authentication: the resolver trusts the **first response whose transaction ID and port match**. Almost every DNS attack exploits that.

## DNS Poisoning

**DNS poisoning** is any technique that makes a client resolve a name to the wrong address, redirecting it to a system the attacker controls. The methods, from the network to the client:

| Technique | Where | How |
|---|---|---|
| **Rogue DNS server** | Network | Attacker's server answers queries, usually after a rogue DHCP server or ARP poisoning has pointed clients at it, or by sniffing and replying faster than the real server |
| **DNS cache poisoning** | Recursive resolver | Attacker injects a forged response into the resolver's cache (guessing transaction ID and source port, or exploiting a bug), so **every client** of that resolver gets the bad answer until TTL expires |
| **DNS pharming** | Resolver or client | A general term for redirecting legitimate traffic to a fake site by manipulating resolution, whether at the resolver, the hosts file, or the router |
| **Altering the hosts file** | Client | Malware or an insider adds an entry; hosts file wins over DNS |
| **Corrupting the IP configuration** | Client | Changing the client's configured DNS server to the attacker's (malware, rogue DHCP, compromised home router) |
| **DNS query spoofing** | Path | Attacker on the path sees the query and sends a forged reply before the real one arrives |
| **Proxy falsification** | Client | Changing the browser's proxy settings (or using a malicious **PAC** file / WPAD) so all web traffic goes through the attacker's proxy; not DNS itself but the same effect |

## Defenses Against DNS Poisoning

- **DNSSEC** (DNS Security Extensions): authoritative servers **digitally sign** records; a validating resolver checks the signature chain up to the root. It provides **integrity and origin authentication, not confidentiality**, and protects the resolver-to-authoritative leg. Adoption is partial.
- **DNS over HTTPS (DoH)** and **DNS over TLS (DoT)** encrypt the **client-to-resolver** leg, stopping on-path spoofing and eavesdropping. Trade-off: DoH bypasses enterprise DNS filtering and monitoring unless the organization controls the resolver.
- **Resolver hardening**: random source ports and transaction IDs, limiting recursion to internal clients, keeping resolver software patched, short cache TTLs for critical records, and **split DNS** (internal names never visible outside).
- **Client hardening**: protect the hosts file and network settings with endpoint controls, use DHCP snooping and DAI on switches to stop rogue DHCP/ARP, and run a **DNS filtering / sinkhole** service that blocks known malicious domains.
- **Monitoring**: watch for sudden changes in resolved addresses, unexpected DNS servers in traffic, and DNS tunneling (large or frequent TXT queries used for exfiltration or command and control).

## Domain Hijacking

**Domain hijacking** (domain theft) is taking over the **registration** of a domain: through stolen registrar credentials, social engineering of the registrar, an expired registration that the attacker re-registers, or abuse of the transfer process. The attacker then controls the real DNS records, so every resolver worldwide points to them and even DNSSEC does not help (they can re-sign). Defenses: **registrar lock**, strong MFA on the registrar account, auto-renewal with monitored contact addresses, and monitoring of WHOIS and NS records.

A related trick is **typosquatting** / URL hijacking: registering a lookalike name (examp1e.com, example.co) and waiting for mistyped visits or for use in phishing.

## Homograph Attack

A **homograph attack** registers a domain whose characters **look identical** to a legitimate one but are different Unicode code points, for example a Cyrillic "а" instead of Latin "a". Internationalized domain names are encoded as **Punycode** (xn--...) so the browser bar can show the lookalike while the real name differs. Defenses: browsers rendering mixed-script names as Punycode, user awareness, and email/web filters that flag lookalike domains.

## Key Points

- **DNS trusts the first matching response; the hosts file is checked before DNS.** Both facts drive the attacks.
- **Cache poisoning hits a resolver and all its clients; hosts file and IP configuration attacks hit one client; rogue DHCP and ARP poisoning are the usual way to install a rogue DNS server.**
- **DNSSEC gives signed, authenticated records (integrity, not confidentiality); DoH/DoT encrypt the client-to-resolver path.**
- **Domain hijacking attacks the registration, not resolution**, so registrar lock and MFA are the controls.
- **Homograph attacks use lookalike Unicode characters; Punycode display exposes them.**
