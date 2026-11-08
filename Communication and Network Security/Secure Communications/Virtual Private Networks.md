## Tunneling

**Tunneling** encapsulates one protocol inside another so it can cross a network that would not otherwise carry it, or would not carry it safely. The original packet becomes the **payload** of a new packet, and the intermediate network sees only the outer header.

Tunneling is a neutral mechanism, not a security control in itself:

- **Legitimate**: carrying a private IP packet across the internet, running IPv6 over IPv4, bridging two sites.
- **Hostile**: bypassing filters by wrapping a blocked protocol in an allowed one (SSH over HTTPS, data exfiltration over DNS). Tunnels are the standard **covert channel** and defeat filters that inspect only the outer layer — see [[Converged and Multilayer Protocols]].

Costs of tunneling: **overhead** (headers on headers, lower effective MTU and throughput), **inefficient routing** (traffic detours to the tunnel endpoint), and **blind spots** (IDS, DLP, and firewalls cannot see inside an encrypted tunnel).

## What a VPN Is

A **virtual private network** is a tunnel that is also **authenticated and encrypted**, giving a private link across an untrusted network. It provides confidentiality, integrity, and peer authentication for everything inside it — including protocols that have no security of their own, which is its main value.

What a VPN does **not** do: it does not protect data before it enters or after it leaves the tunnel, it does not make an infected endpoint safe, and it does not authenticate the user beyond whatever credential the VPN itself checks. Encryption ends at the **tunnel endpoint**, not at the application server.

A VPN always needs an **intermediary network** to run over — it is a tunnel through something, so two systems with no network between them cannot be linked by one. The intermediary is usually the internet, but it does not have to be: a VPN between two systems **on the same LAN** is valid and is how sensitive internal traffic is protected on an untrusted internal network.

**Deployment shapes:**

| | Endpoints | Typical use |
|---|---|---|
| **Site-to-site** (gateway-to-gateway) | Two VPN appliances; hosts are unaware | Connecting branch offices or a datacenter over the internet instead of a leased line |
| **Remote access** (host-to-gateway) | Client software on a laptop to a concentrator | Teleworkers reaching the corporate network |
| **Host-to-host** | Two individual systems | Protecting one sensitive flow, e.g. IPsec transport mode between servers |

## Always-On, Split vs Full Tunnel

**Always-on VPN** establishes the tunnel automatically whenever the device has connectivity, before the user is involved. It removes the choice (and the forgetting) from the user, guarantees that policy and inspection apply everywhere, and keeps the device manageable off-site. The costs are bandwidth through the corporate gateway and a hard dependency on gateway availability.

|                               | Full tunnel                                                              | Split tunnel                                                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| **What goes through the VPN** | **All** traffic, including internet browsing                             | Only traffic destined for corporate networks; the rest goes direct                                                               |
| **Security**                  | Stronger: everything passes corporate filtering, inspection, and logging | Weaker: the host is simultaneously on the untrusted local network and the corporate network, a potential **bridge** between them |
| **Performance / cost**        | Higher latency, all traffic consumes gateway and corporate bandwidth     | Efficient; cloud and video traffic goes direct                                                                                   |

**Full tunnel is the secure default.** Split tunneling is a deliberate performance trade-off, acceptable when the endpoint itself is hardened and monitored. The classic risk is a malware-infected or dual-homed host silently relaying from the home network into the corporate one.

## Common VPN Protocols

| Protocol        | Layer | Notes                                                                                                                                                                                                                                                 |
| --------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PPTP**        | 2     | Microsoft's early protocol; encapsulates PPP, authenticates with MS-CHAPv2. **Cryptographically broken** — do not use                                                                                                                                 |
| **L2F**         | 2     | Cisco's equivalent of PPTP; no encryption of its own; historical                                                                                                                                                                                      |
| **L2TP**        | 2     | Merger of PPTP and L2F; itself provides **no encryption**, so it is deployed as **L2TP/IPsec**. Can carry non-IP protocols and supports multi-hop                                                                                                     |
| **IPsec**       | 3     | The workhorse. **AH** = integrity and authentication, **ESP** = encryption; **transport mode** protects the payload, **tunnel mode** the whole packet; **IKE** negotiates keys and builds **security associations**. Detail in [[Network Encryption]] |
| **SSL/TLS VPN** | 5-7   | Runs over TCP 443, so it crosses firewalls and NAT that block IPsec; often clientless through a browser portal. The common remote-access choice today                                                                                                 |
| **SSH**         | 7     | Port forwarding tunnels arbitrary TCP through an authenticated session; an administrator's VPN substitute, not an enterprise one                                                                                                                      |
| **OpenVPN**     | 5-7   | Open-source, uses TLS for key exchange and its own data channel over UDP or TCP; widely used in commercial and self-hosted VPNs                                                                                                                       |
| **WireGuard**   | 3     | Modern, small codebase, fixed modern cipher suite, fast to connect; increasingly the default in new deployments                                                                                                                                       |

**IPsec vs TLS VPN**: IPsec is transparent to applications and protects everything on the host, but needs a client and struggles with NAT (hence **NAT-T** encapsulating ESP in UDP). A TLS VPN is easier to deploy and firewall-friendly, but historically gives access to a defined set of applications rather than the whole network.

## Operational Concerns

- **Authentication strength**: a VPN with a shared password is a password away from the internal network. **MFA** on remote access is the expected control, and certificates beat passwords.
- **Posture and least privilege**: authenticate the device as well as the user, and terminate the tunnel into a **restricted segment**, not flat into the internal LAN. Zero trust treats a VPN-connected host as untrusted anyway.
- **Availability**: the concentrator is a single point of failure and a DDoS target; it also becomes the organization's bottleneck when everyone works remotely.
- **Logging**: VPN logs are the record of who was inside the network and when.

## Key Points

- **Tunneling = encapsulating one protocol in another; a VPN = a tunnel that is authenticated and encrypted.**
- **Encryption ends at the tunnel endpoint; a VPN protects the transit, not the endpoints or the data beyond it.**
- **Full tunnel sends everything through the gateway (secure default); split tunnel sends only corporate traffic and risks bridging the untrusted local network into the corporate one.**
- **Always-on removes the user's choice to connect, at the cost of gateway dependency.**
- **PPTP is broken; L2TP has no encryption of its own and is paired with IPsec; IPsec works at layer 3 with AH/ESP and transport/tunnel modes; TLS VPNs cross firewalls on 443.**
- **Site-to-site joins networks and is invisible to hosts; remote access connects one user's device.**
