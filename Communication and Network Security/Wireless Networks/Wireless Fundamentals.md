## 802.11 Basics

Wireless LANs follow the **IEEE 802.11** family of standards. Radio replaces the cable, which changes the security model fundamentally: **the medium is shared with everyone in range**, including people outside the building, so there is no physical boundary to rely on.

| Standard | Band | Max speed (nominal) | Marketing name |
|---|---|---|---|
| 802.11 | 2.4 GHz | 2 Mbps | |
| 802.11a | 5 GHz | 54 Mbps | |
| 802.11b | 2.4 GHz | 11 Mbps | |
| 802.11g | 2.4 GHz | 54 Mbps | |
| 802.11n | 2.4 / 5 GHz | 600 Mbps | Wi-Fi 4 |
| 802.11ac | 5 GHz | 6.9 Gbps | Wi-Fi 5 |
| 802.11ax | 2.4 / 5 / 6 GHz | 9.6 Gbps | Wi-Fi 6 / 6E |
| 802.11be | 2.4 / 5 / 6 GHz | 46 Gbps | Wi-Fi 7 |

**2.4 GHz** travels further and penetrates walls better but has only three non-overlapping channels and shares the band with microwaves, Bluetooth, and many other devices. **5 GHz and 6 GHz** are faster with many more channels but shorter range. Wireless media access uses **CSMA/CA** (see [[Signaling and Media Access]]).

**Modes:** in **infrastructure mode** clients connect through a **wireless access point (WAP)** that bridges them to the wired LAN; in **ad hoc** (peer-to-peer, IBSS) mode devices talk directly. Variants of infrastructure mode: **stand-alone** (an AP with no wired connection, clients talk only to each other), **wired extension** (the usual case), **enterprise extension** (many APs sharing one SSID with roaming, usually managed by a wireless controller), and **bridge** (two APs linking two wired networks). **Wi-Fi Direct** is a modern peer-to-peer form.

## SSID

The **service set identifier** is the network name. A **BSSID** is the MAC of one AP's radio; an **ESSID** is the shared name across many APs in an extended service set. APs broadcast the SSID in **beacon frames**.

**Disabling SSID broadcast** (hiding the SSID) is often recommended but is a weak measure: the SSID still appears in cleartext in probe and association frames, so any wireless sniffer finds it in seconds. It stops casual connection attempts only. Changing the **default SSID** matters more, because defaults reveal the vendor and often the default admin credentials.

## Channels and Site Surveys

Channels are subdivisions of the band. Overlapping channels on neighboring APs cause interference and reduce throughput; in 2.4 GHz only channels **1, 6, and 11** do not overlap. Channel width (20/40/80/160 MHz) trades speed for interference.

A **site survey** is a formal assessment of the radio environment: walking the facility with measurement tools to map signal strength, interference, and coverage, then placing APs and choosing channels and power levels so that coverage is adequate **inside** and minimal **outside** the intended area. A survey is repeated after deployment and periodically, and it also detects **rogue access points**. The output is a **heat map**.

## Antenna Management

Antenna type and placement control **where** the signal goes, which is a security control as much as a performance one.

- **Omnidirectional** antennas (the standard rubber duck or internal antenna) radiate in all horizontal directions; place APs centrally so that the signal covers the building and fades at the walls.
- **Directional** antennas (Yagi, panel, parabolic, cantenna) focus the signal in one direction; used for point-to-point bridges and to cover a long corridor or keep signal away from the street.
- **Power level** adjustment: reduce transmit power so that the usable signal ends near the building boundary. Attackers use high-gain antennas, so this limits rather than prevents exposure.
- Mount APs away from exterior walls and windows, and consider the floor above and below.

Where power and antenna tuning are not enough, **shielding** contains the signal. A **Faraday cage** (a conductive enclosure, shielded room, or shielded building materials) blocks electromagnetic fields in both directions, so a wireless network inside the cage works normally for devices inside while its signals cannot be received, or detected, outside. It is the answer when an organization wants internal wireless with no possibility of external detection or access. An **air gap** is not: it works only when wireless is absent altogether. See [[Emanations and Input Output Devices]].

## WPS, MAC Filtering, Captive Portals

- **Wi-Fi Protected Setup (WPS)** was meant to simplify joining a network with a button press or an 8-digit PIN. The PIN is validated in two halves, which reduces the search space to about 11,000 attempts, so WPS PIN can be brute-forced in hours. **Disable WPS.**
- **MAC address filtering** allows only listed MACs to associate. MACs are sent in cleartext in every frame and are trivially spoofed, so this is an administrative nuisance for attackers, not a security control.
- A **captive portal** redirects a newly connected client to a web page before granting access: to accept terms, enter credentials, pay, or register a guest. Common for guest and hotel networks and for NAC onboarding. It authenticates the user at the web layer but does not by itself encrypt the wireless traffic; an open network with a captive portal is still sniffable unless the client uses TLS or a VPN. **Enhanced Open (OWE)** addresses this with encryption on open networks.

## General Wi-Fi Security Procedure

The usual checklist for deploying a wireless network securely:

1. Keep AP **firmware** updated.
2. Change the AP's **default administrator credentials** and manage it only from the wired side or over HTTPS.
3. Enable **WPA3** (or at minimum **WPA2**) with **AES**; avoid WEP and TKIP (see [[Wireless Security Protocols]]).
4. In an organization, use **enterprise authentication** (802.1X with EAP and RADIUS) rather than a shared passphrase.
5. Change the **default SSID**; defaults reveal the vendor and often the default credentials.
6. Change the AP's **default wireless MAC address (BSSID)**, which can also identify the vendor and model.
7. **Decide whether to disable SSID broadcast**: it only stops casual discovery, since the name still appears in probe and association frames.
8. Enable **MAC filtering** as an extra layer if the administrative cost is acceptable; it is spoofable and must never be the only control.
9. Decide between **static IP addressing and DHCP**, with the trade-offs in mind:
    - **DHCP** is easy to manage and scales, but hands an address to any device that associates, so an intruder gets a working configuration automatically.
    - **Static addressing** (or DHCP reservations and a small scope) means an intruder has to guess a valid address, but it adds administrative overhead and does not hide the range from a sniffer.
10. Treat wireless as **external or remote access**: place it in its own segment behind a firewall, with guest traffic on a separate VLAN and no path to internal resources.
11. Treat wireless as an **entry point for attackers**: assume the signal is reachable from outside and design the controls (segmentation, authentication, monitoring) accordingly.
12. Deploy a **wireless IDS/IPS (WIDS/WIPS)** to detect rogue APs, evil twins, and deauthentication attacks (see [[Wireless Attacks]]).
13. Use a **VPN or TLS** for sensitive traffic even over the encrypted WLAN.
14. Use a **captive portal** where guests or unmanaged devices must authenticate or accept terms; it does not encrypt the air.
15. **Track and log events** (associations, authentication failures, WIDS alerts, configuration changes) and review them.

Additional measures that complement the list: **disable WPS**, place and tune APs with a **site survey** (power and antennas), re-survey and audit periodically, and treat the AP as a network device under the same configuration management as switches.

## Key Points

- **Wireless has no physical boundary; the signal reaches the parking lot.** Site surveys, antenna placement, and power tuning limit, but do not eliminate, exposure.
- **Hiding the SSID and MAC filtering are not security controls**; both are defeated by a sniffer.
- **A Faraday cage keeps internal wireless from being received or detected outside; an air gap cannot, since it excludes wireless entirely.**
- **WPS PIN is brute-forceable in hours; disable it.**
- **Captive portals authenticate users but do not encrypt the air.**
- **Treat the WLAN as an untrusted segment: firewall it from the wired LAN, use WPA3/WPA2 enterprise, and still encrypt above it.**
- **Treat wireless as external access and as an entry point for attackers: segment it, authenticate it, monitor and log it.**
