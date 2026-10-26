These are things users or attackers do to mobile devices, or things devices can do, that weaken the controls in [[Mobile Device Security Features]].

## Circumventing the Platform's Controls

- **Rooting** (Android) and **jailbreaking** (iOS) remove the manufacturer's restrictions to gain full administrative (root) control. They break the app sandbox and other protections, often block updates, and make malware far more damaging. MDM compliance checks can detect them and block the device.
- **Sideloading** is installing an app from outside the official store, such as an APK file or a third-party store. It skips the store's vetting.
- **Custom firmware** replaces the vendor's operating system with an unofficial build (a custom ROM). It usually needs an unlocked bootloader, may not receive security patches, and its contents are unverified.
- **Carrier unlocking** removes the lock that ties a phone to one mobile carrier, so it works with other carriers' SIM cards. It is a different thing from rooting, and is legitimate when done through the carrier, but it lets the device be used with unmanaged SIMs. Unofficial unlock methods can involve modifying firmware.
- **Firmware over-the-air (OTA) updates** are OS and firmware updates delivered wirelessly by the vendor or carrier. They keep the device patched, so they should be enabled and managed, but they must be **digitally signed**. Carriers and vendors may delay or stop them, leaving old devices vulnerable.

## Hardware and Radio Features

- **Onboard camera and video.** They can capture sensitive documents, screens, and facilities, geotag images, and be switched on by malware. Policy or MDM can restrict or disable them in sensitive areas.
- **Recording microphone.** Can record meetings and conversations, and can be activated covertly by malware or a malicious app.
- **Tethering and hotspots.** **Tethering** shares the device's cellular connection with another device, over USB or Bluetooth. A **hotspot** does it as a Wi-Fi access point. A device on the corporate network that also tethers can bridge around network filtering and monitoring, and a weak hotspot password lets others in.
- **Contactless payment** uses NFC and **tokenization** (a one-time token replaces the card number) for mobile wallets. The short range, tokens, and biometric approval make it fairly safe, and the remaining risks are eavesdropping or relay attacks and a lost unlocked device. NFC can be disabled when not needed.
- **SIM cloning** copies the identity data from a SIM card onto another, so the attacker can use the victim's number and account. It is different from **SIM swapping**, where the attacker tricks the carrier into moving the number to their own SIM. Both undermine SMS-based authentication.

## Key Points

- **Rooting and jailbreaking, sideloading, and custom firmware** all remove vendor protections, so managed devices must detect and block them.
- **Carrier unlocking** is about carrier lock, not security bypass.
- **OTA updates should be on, signed, and managed.**
- **Camera, microphone, tethering, and NFC** are features whose use should be governed by policy.
- **SIM cloning copies the SIM. SIM swapping hijacks the number.**
