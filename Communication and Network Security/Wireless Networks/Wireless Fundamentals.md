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

## WPS, MAC Filtering, Captive Portals

- **Wi-Fi Protected Setup (WPS)** was meant to simplify joining a network with a button press or an 8-digit PIN. The PIN is validated in two halves, which reduces the search space to about 11,000 attempts, so WPS PIN can be brute-forced in hours. **Disable WPS.**
- **MAC address filtering** allows only listed MACs to associate. MACs are sent in cleartext in every frame and are trivially spoofed, so this is an administrative nuisance for attackers, not a security control.
- A **captive portal** redirects a newly connected client to a web page before granting access: to accept terms, enter credentials, pay, or register a guest. Common for guest and hotel networks and for NAC onboarding. It authenticates the user at the web layer but does not by itself encrypt the wireless traffic; an open network with a captive portal is still sniffable unless the client uses TLS or a VPN. **Enhanced Open (OWE)** addresses this with encryption on open networks.

## General Wi-Fi Security Procedure

The usual checklist for deploying a wireless network securely:

1. Change the AP's **default administrator credentials** and manage it only from the wired side or over HTTPS.
2. Keep AP **firmware** updated.
3. Change the **default SSID**; decide on broadcast based on usability (hiding adds little).
4. Use **WPA3** (or at minimum WPA2) with **AES**; in an organization use **enterprise mode with 802.1X** rather than a shared passphrase (see [[Wireless Security Protocols]]).
5. **Disable WPS**; MAC filtering optional.
6. Place and tune APs with a **site survey**; adjust power and antennas.
7. **Segment** wireless from the wired LAN: treat it as an untrusted segment behind a firewall, with guest traffic separated by VLAN and with no path to internal resources.
8. Use a **VPN or TLS** for sensitive traffic even over the encrypted WLAN.
9. Use a **wireless IDS/IPS** to detect rogue APs, evil twins, and deauthentication attacks (see [[Wireless Attacks]]).
10. Periodically re-survey and audit, and treat the AP as a network device subject to the same configuration management as switches.

## Key Points

- **Wireless has no physical boundary; the signal reaches the parking lot.** Site surveys, antenna placement, and power tuning limit, but do not eliminate, exposure.
- **Hiding the SSID and MAC filtering are not security controls**; both are defeated by a sniffer.
- **WPS PIN is brute-forceable in hours; disable it.**
- **Captive portals authenticate users but do not encrypt the air.**
- **Treat the WLAN as an untrusted segment: firewall it from the wired LAN, use WPA3/WPA2 enterprise, and still encrypt above it.**
