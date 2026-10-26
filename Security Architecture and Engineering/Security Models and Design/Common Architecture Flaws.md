Even a well-designed system can have weaknesses in its design, its code, or the way its parts interact. These are the common categories. The mechanisms that counter them (process isolation, hardware segmentation, root of trust) are in [[Security Capabilities of Information Systems]].

## Covert Channels

A **covert channel** is a communication path that breaks the security policy by moving information in a way the system was never designed to allow. It lets a process leak data to another that should not receive it, with no obvious sign.

- **Covert storage channel.** One process writes to a shared storage location, such as a file, a disk-space level, or a field in a packet header, and the other reads it.
- **Covert timing channel.** One process signals by changing the **timing** of an observable resource, for example holding the processor busy or delaying a response, and another reads the signal by measuring it.

Covert channels are hard to remove completely, and they matter most in high-security systems (see [[Security Model Fundamentals]], where noninterference is the model that addresses them). Malware also uses covert channels to hide communication, such as data hidden in DNS or ICMP traffic.

**Controls:** reduce shared resources, enforce isolation, add noise or delay to timing, limit the bandwidth of channels, and monitor and audit for unusual patterns.

## Attacks Based on Design or Coding Flaws

Flaws left from design or programming open the system to attack. Common ones:

- **Buffer overflow.** A program writes more data into a buffer than it can hold, overwriting adjacent memory, which can crash it or let an attacker run their own code.
- **Improper input validation.** The program trusts data it receives, which allows **injection** attacks (such as SQL or command injection) and malformed input to cause unexpected behavior.
- **Race condition and TOCTOU.** The outcome depends on timing. In **time-of-check to time-of-use**, the state changes between the moment a condition is checked and the moment it is relied on (see [[Processors]]).
- **Maintenance hooks and backdoors.** Special entry points that developers create to bypass normal security for debugging or support. If they are left in production they are an open door.
- **Hidden code.** Unauthorized functionality such as a **logic bomb** (code that triggers on a condition) that is inserted deliberately.
- **Insecure initialization and failure.** A system that starts or fails in an open or unprotected state, instead of failing secure (see [[Secure Design Principles]]).

**Controls:** secure coding standards and training, input validation and bounds checking, code review and testing (static and dynamic analysis, fuzzing), removing debug hooks before release, patching, and OS defenses such as non-executable memory and randomized memory layout.

## Rootkits

A **rootkit** is malware that gains privileged access and then **hides itself and other malware** by altering the operating system or lower layers, so that its processes, files, and network connections do not appear in normal tools. It also gives the attacker lasting access.

| Type | Where it lives |
|---|---|
| **User-mode** | Hooks applications and libraries, with the privileges of a user or administrator |
| **Kernel-mode** | Modifies the OS kernel or drivers (ring 0), so it can hide from anything running above it |
| **Bootkit** | Infects the boot loader, so it loads before the OS |
| **Firmware / hypervisor** | Lives in firmware or beneath the OS, and survives reinstalling the OS (see [[Firmware]]) |

The deeper the rootkit sits, the harder it is to detect, since the tools that would find it rely on the layer it controls.

**Controls:** secure and measured boot with a root of trust, code signing, integrity checking and offline or external scanning, memory forensics, least privilege to prevent installation, and, once found, **rebuilding from known good media**, not cleaning in place.

## Incremental Attacks

An **incremental attack** makes changes so small, or so slow, that they stay below the notice of the people and systems watching.

- **Data diddling.** Making small, unauthorized changes to data before or during entry or processing, such as altering records or amounts a little at a time.
- **Salami attack.** Skimming tiny amounts from many transactions, for example rounding fractions of a cent into an attacker's account. The amounts are trivial one by one and large in total.

**Controls:** separation of duties, reconciliation and audit of totals, integrity checking of data, logging and anomaly detection, and code review of financial and calculation logic.

## Key Points

- **Covert channels leak by storage or by timing**, and can be reduced but rarely removed entirely.
- **Most coding flaws are about trusting input or timing:** buffer overflow, bad input validation, TOCTOU, and leftover maintenance hooks.
- **Rootkits hide.** The lower they sit, the harder they are to find, and the answer is rebuilding.
- **Incremental attacks hide in the small.** Data diddling alters data, a salami attack skims amounts.
