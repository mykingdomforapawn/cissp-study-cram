## Full-Disk and Mobile Encryption

Portable devices (laptops, phones, removable media) are protected mainly against loss or theft, not interception in transit — the threat model is "someone has physical possession of the device," not "someone's sniffing traffic." The standard answer is **full-disk encryption**: everything on the drive is encrypted with a symmetric key (see Symmetric Key Algorithms), so the data is unreadable without that key even if the drive is physically removed and read elsewhere.

## TPM (Trusted Platform Module)

A **TPM** is a dedicated hardware chip on the device's motherboard — the portable-device equivalent of the HSM described in Asymmetric Key Management, but built into consumer hardware rather than a standalone security appliance. It:

- Generates and stores the disk encryption key, never exposing it outside the chip in plaintext.
- Binds the key to that specific hardware — the encrypted drive can't simply be moved to another machine and decrypted, since the key material never leaves the original TPM.
- Can verify the boot process hasn't been tampered with before releasing the key (a check sometimes called measured/trusted boot), refusing to unlock the drive if the system has been altered.

This is why full-disk encryption on modern laptops (e.g., BitLocker on TPM-equipped hardware) can unlock transparently at boot without the user typing a password every time, while still remaining unreadable if the physical drive is stolen and read on a different machine.
