## Two Worlds

Voice security splits into the **legacy circuit-switched world** (PSTN, PBX, analog and ISDN lines) and the **packet world** (VoIP over the data network). The attacks differ because the technology differs, but the targets are the same: **listening to calls, making calls at someone else's expense, and impersonating a caller**.

## The PSTN and POTS

The **public switched telephone network** is the global circuit-switched voice network; **POTS** (plain old telephone service) is the basic analog line into it. A call reserves a dedicated circuit end to end for its duration (see [[Switching and WAN Technologies]]).

Security characteristics:

- **No encryption and no authentication.** A PSTN call is protected only by the physical inaccessibility of the wiring and the switches. Tapping a line is a physical act, not a network one.
- **It is also a backdoor into the building.** A modem on an analog line bypasses the firewall entirely. **War dialing** — calling ranges of numbers to find modems and fax machines — is the reconnaissance for this; the control is an inventory of lines plus a prohibition on unauthorized modems.
- **It is a dependency**, used for alarm circuits, elevator phones, fire panels, out-of-band management, and fax. Replacing it with VoIP moves those dependencies onto the data network and its power supply.

## Phreaking

**Phreaking** is the attack on telephone systems: manipulating signaling to get free calls, unauthorized access, or control of switching equipment. It worked because telephone signaling originally traveled **in the same channel as the voice** (in-band signaling), so a caller who could generate the right tones could instruct the switch.

The **colored boxes**:

| Box | What it did |
|---|---|
| **Blue box** | Generated the 2600 Hz tone and MF signaling to seize a trunk and place free long-distance calls |
| **Red box** | Simulated the tones of coins dropping into a payphone |
| **Black box** | Manipulated line voltage so the called party's line never registered as answered, making calls unbilled |
| **White box** | A portable DTMF keypad for controlling a line from outside |

Modern networks use **out-of-band signaling** (SS7), so the tone attacks are dead. The general principle stands: **control data and user data on the same channel means users can forge control data.** SS7 has its own abuse (location tracking, SMS interception), because it assumes all interconnected carriers are trustworthy.

## PBX Fraud and Abuse

A **private branch exchange** is an organization's own telephone switch, connecting internal extensions to each other and to outside lines. A compromised PBX is a financial loss, not just a confidentiality one.

Typical abuse:

- **Toll fraud / long-distance theft**: an attacker gains dial access and routes expensive (often premium-rate international) calls through the organization, which pays the bill. Often discovered only on the invoice.
- **Direct inward system access (DISA)** abuse: the feature that lets employees call in and get an outside line, protected by a short PIN that is guessable or shared.
- **Default administrative credentials and maintenance modems** on the PBX itself.
- **Voicemail abuse**: default or weak mailbox PINs give access to messages, and some voicemail systems can place outbound calls.
- **Social engineering of operators** into transferring calls externally, or into resetting a PIN.

Controls: change default credentials, disable unused features (DISA, call forwarding to external numbers, out-dialing from voicemail), enforce non-trivial PINs, block or restrict international and premium-rate destinations by default, **restrict out-of-hours calling**, log and **review call detail records** for anomalies, and keep the PBX patched and off the public network. Auditing the phone bill is a genuine detective control here.

## Vishing and Caller ID Spoofing

**Vishing** is phishing over the voice channel: a call (or voicemail, or a callback number planted in an email) that pressures the victim into disclosing credentials, authorizing a payment, or installing something. It works because people trust a voice more than an email, because **caller ID is trivially forged** on VoIP, and now because synthetic voice can imitate a known person.

Defenses are mostly human and procedural, not technical: training that treats an inbound call as unauthenticated, **call-back to a known-good number** before acting on any request, out-of-band confirmation for payments and credential resets, and never reading a one-time code to a caller. See [[Social Engineering]].

**SPIT** (spam over internet telephony) is the bulk version, the voice equivalent of email spam.

## VoIP

**Voice over IP** carries calls as packets on the data network: **SIP** sets up and tears down calls, **RTP** carries the audio. Because it is just an application on the IP network, it inherits every IP attack and adds the consequences of being voice.

- **Eavesdropping**: unencrypted RTP can be captured and replayed as audio. Mitigation: **SRTP** for media and **SIP over TLS** for signaling.
- **Caller ID spoofing and registration hijacking**: SIP headers are forged easily; an attacker who registers as a user receives their calls.
- **Toll fraud**, the VoIP form of PBX fraud, against the SIP trunk or IP-PBX.
- **Denial of service**: voice is intolerant of latency, jitter, and loss, so degradation is as good as an outage. **QoS** is therefore a security control for availability (see [[Load Balancing and Quality of Service]]).
- **VLAN hopping** between the voice and data VLANs where segmentation is weak (see [[Switch and VLAN Security]]).

Controls: a **separate voice VLAN**, SRTP and TLS, authentication of endpoints, a **session border controller** at the edge to police SIP traffic, and QoS. Note the availability dependency: when the network or the power is down, so are the phones — which matters for **emergency calling**, and for **E911 location**, since an IP phone can be anywhere.

## Key Points

- **PSTN calls are unencrypted and unauthenticated; an unmanaged modem on an analog line bypasses the firewall, which is what war dialing looks for.**
- **Phreaking exploited in-band signaling (blue box = 2600 Hz free long distance, red box = fake coin tones, black box = unbilled calls); out-of-band signaling ended it.**
- **PBX fraud is a billing loss: default credentials, DISA, voicemail out-dialing. Controls are disabling unused features, restricting destinations, and reviewing call detail records.**
- **Vishing exploits spoofable caller ID and human trust; the control is calling back on a known-good number, not technology.**
- **VoIP = SIP for signaling, RTP for media; protect with SIP/TLS and SRTP, a voice VLAN, a session border controller, and QoS.**
