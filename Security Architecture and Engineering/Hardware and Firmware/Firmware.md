**Firmware** is software stored in nonvolatile memory (ROM, EEPROM, or flash) built into a hardware device. It is the code that runs when the hardware starts and that controls it at the lowest level. It is semi-permanent: it persists without power, and unlike ordinary software it is not normally changed by users. The memory types are in [[Memory]].

## Where It Appears

- **BIOS** (Basic Input/Output System) is the traditional firmware on a computer's motherboard, which initializes hardware and starts the operating system.
- **UEFI** (Unified Extensible Firmware Interface) is the modern replacement, with more features, including **secure boot**, which only runs a bootloader and OS whose digital signatures are trusted (see [[Security Capabilities of Information Systems]] for measured boot and the TPM).
- **Device firmware** runs inside network equipment, printers, storage controllers, drives, peripherals, cameras, and IoT devices, and anything else with an embedded processor.

## Security Concerns

- **Persistence and stealth.** Malicious firmware runs before the OS and below it, so antivirus cannot see it, and it survives reinstalling the OS or even replacing the disk.
- **Phlashing.** An attack that overwrites the firmware with a malicious or damaged image, either to gain persistent control or to render the device unusable (**bricking**).
- **Unsigned or unverified updates.** If a device accepts any firmware image, an attacker with access can install their own.
- **Neglected patching.** Firmware is often forgotten in patch programs, and device vendors may stop issuing updates, leaving known flaws open. Many embedded devices ship with default credentials as well.
- **Supply chain.** Firmware can be tampered with before the device is delivered, which ties to [[Supply Chain Risk Management]].

## Countermeasures

- Accept only **digitally signed** firmware and enable **secure boot** with a hardware root of trust.
- Keep an inventory of devices and their firmware versions, and include firmware in patch management.
- Restrict who can flash firmware, protect with a firmware password, and where available use hardware write protection.
- Buy from trusted sources and verify updates against the vendor's published hashes.
- Monitor for firmware changes, using the measured boot values of a TPM.

## Key Points

- **Firmware is code in nonvolatile memory**, below the operating system, so a compromise there is persistent and invisible to OS-level tools.
- **BIOS vs UEFI.** UEFI adds secure boot and signature checks.
- **Phlashing** means overwriting firmware, and the defense is signed updates and write protection.
- **Patching includes firmware.**
