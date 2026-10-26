Electronic equipment emits signals that can be captured at a distance, and the devices people use to enter and read information each add their own exposure.

## Emanation Security

All electronic equipment produces **electromagnetic emanations**: radio-frequency and electromagnetic signals that are a by-product of operating. Cables, monitors, and keyboards act as small antennas, and the emanations can carry the data being processed. An attacker who captures and decodes them can reconstruct what is being displayed or typed without ever touching the system. This is a **side-channel** attack (see [[Cryptographic Attacks]]), and the monitor version is known as **Van Eck phreaking**.

**TEMPEST** is the name for the (originally US government) standards and research on investigating, studying, and controlling these emanations. In practice it also names the shielding countermeasures.

| Countermeasure | How it helps |
|---|---|
| **Faraday cage** | A grounded enclosure of conductive material (a shielded room or container) that blocks electromagnetic signals from leaving, or entering |
| **White noise** | Generating random electromagnetic noise that masks the real emanations |
| **Control zone** | A shielded or controlled area, such as a whole facility or room, that confines emissions inside a boundary |
| **Shielded cabling and equipment** | Shielded cables and TEMPEST-certified devices that emit less |
| **Distance and placement** | Emission strength falls with distance, so keeping sensitive equipment away from the perimeter helps |

Shielding is expensive, so it is used where the data justifies it, such as classified processing facilities. **Fiber-optic** cable emits no electromagnetic signal.

## Input and Output Devices

Input and output devices connect the processor to people and to the outside world. Each is a point where information can leave or where unauthorized input can enter.

- **Monitors.** The screen can be read by anyone with a view (**shoulder surfing**), including through windows or on camera, and the display itself produces emanations. Countermeasures are privacy filters, positioning screens away from windows and public areas, and screen locks. Where emanations matter, shielding applies.
- **Printers.** Printed output can be left in trays and picked up by the wrong person. Modern printers and multifunction devices also have their own **storage**, a network connection, and **firmware**, and keep copies of jobs on internal disks. They need the same patching, access control, and sanitization as any computer. Controls are secure-print release (the job prints only after the user authenticates at the device), restricted physical placement, and wiping storage before disposal.
- **Keyboards and mice.** A **hardware keylogger** placed between the keyboard and the computer records every keystroke, and is difficult to spot because software cannot see it. **Wireless** keyboards and mice can be intercepted or spoofed over the air, which lets an attacker read keystrokes or inject their own. Keystrokes also emit electrical and acoustic signals. Controls are physical inspection of connections, wired devices or encrypted wireless links, and restricting USB ports.
- **Modems (POTS).** A modem on a plain old telephone line lets someone dial straight into a system, **bypassing the firewall**. Attackers find them by **war dialing**, calling number ranges to find ones answered by a modem. Rogue modems that employees attach themselves are the usual hazard, since they create a back door that the perimeter controls never see. Controls are removing unneeded modems, banning unapproved ones, requiring strong authentication and **callback** (the system hangs up and calls back a known number) on those that remain, and war dialing your own number ranges to find strays.

## Key Points

- **Emanations carry data.** Electronic equipment leaks signals that can be captured remotely, and TEMPEST names the standards and shielding that control it.
- **Countermeasures** are a Faraday cage, white noise, and control zones, which are used where the data's value justifies the cost. Fiber does not radiate.
- **Printers are computers.** They store data, run firmware, and sit on the network, as well as leaving paper in a tray.
- **Keyloggers and wireless input** are the keyboard and mouse risks, and they are hard to see from software.
- **A modem is a back door** past the firewall, found by war dialing and mitigated by removal, strong authentication, and callback.
