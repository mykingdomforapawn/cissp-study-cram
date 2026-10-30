## What the OSI Model Is

The **Open Systems Interconnection (OSI) Reference Model** (ISO, 1984) is a seven-layer conceptual framework that describes how data moves from an application on one host to an application on another. No real protocol stack implements it exactly; its value is as a **common vocabulary** for placing protocols, devices, and attacks at a layer and for reasoning about what a control at one layer can and cannot see.

Each layer provides services to the layer above it and uses the services of the layer below. A layer on the sending host communicates logically with the **same layer** on the receiving host (peer-to-peer), but physically only through the layers beneath it.

## Encapsulation and De-encapsulation

As data travels **down** the stack on the sender, each layer wraps the data from above in its own header (and, for the data link layer, a trailer). This is **encapsulation**. On the receiver the process reverses as data moves **up** the stack: each layer strips its header, inspects it, and hands the payload to the next layer. This is **de-encapsulation** (or decapsulation).

The unit of data at each layer has a name, the **protocol data unit (PDU)**:

| Layer | PDU |
|---|---|
| 7, 6, 5 Application, Presentation, Session | Data (or protocol data unit) |
| 4 Transport | Segment (TCP) / Datagram (UDP) |
| 3 Network | Packet |
| 2 Data Link | Frame |
| 1 Physical | Bits |

Security consequence: a control working at a given layer only sees that layer's header and everything above it as payload. A router filters on IP addresses, not on usernames; an application-layer proxy can read the HTTP request but a layer 2 switch cannot.

## The Seven Layers

Mnemonic from top to bottom: **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing. From bottom up: **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way.

| # | Layer | Responsibility | Typical protocols / devices |
|---|---|---|---|
| 7 | **Application** | Interface between the network and the user's application; the protocols the application speaks | HTTP, FTP, SMTP, DNS, SNMP, Telnet, SSH; application firewalls, proxies, gateways |
| 6 | **Presentation** | Data formatting, character encoding, compression, and (historically) encryption so that different systems can interpret the data | ASCII, JPEG, MPEG, TLS is often placed here or at session |
| 5 | **Session** | Establishes, maintains, and tears down sessions between applications; dialog control (simplex, half-duplex, full-duplex) | NFS, SQL sessions, RPC, NetBIOS |
| 4 | **Transport** | End-to-end delivery between processes: segmentation, sequencing, flow control, error recovery, port numbers | TCP, UDP, TLS (by some sources) |
| 3 | **Network** | Logical addressing and **routing** between networks | IP, ICMP, IGMP, IPsec, routing protocols; routers, layer 3 switches |
| 2 | **Data Link** | Framing, physical (MAC) addressing, error detection on a single link; split into **LLC** and **MAC** sublayers | Ethernet, ARP, PPP, L2TP; switches, bridges |
| 1 | **Physical** | Transmission of raw bits over the medium: voltages, connectors, cabling, radio | Cables, hubs, repeaters, NICs, wireless radios |

Points worth remembering per layer:

- **Application layer** is not the application itself; a browser is not layer 7, HTTP is.
- **Presentation** is where encryption and compression are conventionally placed, though modern protocols blur this.
- **Transport** is where **ports** identify the sending and receiving process. TCP is connection-oriented and reliable; UDP is connectionless and best-effort (see [[TCP-IP Model and Transport Protocols]]).
- **Network** handles routing and fragmentation. Routers make forwarding decisions on destination IP addresses; firewalls doing packet filtering work here (plus transport headers).
- **Data Link** converts packets into frames and uses **MAC addresses** (48-bit, first 24 bits the vendor's OUI). ARP maps IP to MAC at this boundary (see [[IP, ICMP, and ARP]]). Switches separate collision domains but not broadcast domains.
- **Physical** is where **tapping, jamming, and cable damage** happen; physical security and media choice are the controls (see [[Transmission Media]]).

## Routing Protocols

Routers exchange reachability information with **routing protocols** and build a routing table. Two families:

| Family | How it works | Examples |
|---|---|---|
| **Distance-vector** | Each router shares its whole table with neighbors; best path is chosen by hop count or a simple metric. Simple, slow to converge, prone to loops | **RIP** (hop count, max 15), **IGRP/EIGRP** (Cisco) |
| **Link-state** | Each router floods the state of its links to all routers; every router builds a full map and computes shortest paths. Faster convergence, more CPU/memory | **OSPF**, **IS-IS** |

**Interior gateway protocols** (RIP, OSPF, EIGRP, IS-IS) run inside one autonomous system. **BGP** is the **exterior gateway protocol** of the internet, a path-vector protocol between autonomous systems. Security concern: routing protocols without authentication can be fed false routes (route injection, BGP hijacking) that redirect or black-hole traffic. Defenses are authentication of routing updates, filtering of accepted prefixes, and for BGP, RPKI.

**Static routing** uses manually configured routes; **dynamic routing** uses these protocols.

## Key Points

- **Encapsulation adds a header per layer on the way down; de-encapsulation strips it on the way up.**
- **PDU names: data, segment/datagram, packet, frame, bits.**
- **A control at a layer sees only that layer's header and above as payload**, which is why packet filters cannot see application content and proxies can.
- **Routers are layer 3, switches and bridges layer 2, hubs and repeaters layer 1.**
- **Distance-vector = hop count, slow (RIP); link-state = full map, fast (OSPF); BGP between autonomous systems.**
