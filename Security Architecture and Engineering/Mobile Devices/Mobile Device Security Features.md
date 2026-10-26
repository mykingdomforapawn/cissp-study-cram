Mobile devices (phones and tablets, mainly **iOS** and **Android**) are small, always connected, easily lost, and hold both personal and corporate data. iOS is a closed ecosystem (one vendor, apps from one store), and Android is more open (many vendors, more freedom to install software, and updates that vary by manufacturer). Each feature below is a control, a setting, or a capability that an organization can use or manage. For device encryption mechanics see [[Portable Devices and TPM]].

## Management

- **Mobile device management (MDM)** is software that centrally **enrolls, configures, monitors, and controls** mobile devices, enforces policy, and can wipe them. Broader products (EMM, UEM) also manage apps, content, and other endpoints. Most of the features below are enforced through MDM.
- **Asset tracking** keeps an inventory of devices, their owners, status, and compliance, typically through the MDM.
- **Application control** restricts which apps may be installed or run, using allow lists or deny lists, and manages app permissions.
- **Content management** controls corporate documents on the device: secure access, encryption, and limits on copying and sharing, often inside a managed container.
- **Credential management** is the secure storage and handling of passwords, keys, and certificates on the device (such as a keychain or password manager), including MDM-delivered certificates. Credentials should not be stored in plain text in apps.
- **Deactivating unused features** means turning off Bluetooth, NFC, Wi-Fi, cameras, and other functions that are not needed, to reduce the attack surface.

## Protecting the Device and Its Data

- **Device authentication.** Verifying the user (and the device) with a PIN, password, biometrics, or certificates, ideally with MFA, both to unlock the device and to access the network.
- **Screen locks.** The screen locks automatically after inactivity and needs authentication to unlock.
- **Device lockout.** After a set number of failed unlock attempts, the device locks for a delay or erases itself, which defeats brute-force guessing.
- **Full device encryption.** All data on the device is encrypted at rest with a key tied to the passcode and hardware, so a lost or stolen device exposes nothing.
- **Remote wiping.** Erasing a device over the network when it is lost, stolen, or an employee leaves. A **full wipe** resets the entire device, and a **selective wipe** removes only corporate data. It only works while the device is online.
- **Storage segmentation.** Separating corporate and personal data (or apps) on the device, in a container or work profile, so that corporate controls such as encryption and selective wipe apply to the corporate side only.
- **Removable storage.** SD cards and USB storage can carry data out or malware in, and can be lost, so they are disabled or encrypted.

## Communications and Services

- **Communication protection.** Encrypting data in transit using TLS, a VPN (often per-app), and secure Wi-Fi, and avoiding untrusted public networks.
- **Text messaging.** SMS and MMS are **unencrypted**, can be spoofed and intercepted, and are a phishing route (**smishing**). Sensitive information and MFA codes are safer through encrypted messaging apps or authenticator apps.
- **Push notifications.** Messages sent by a server to the device without the app being open. They pass through the platform vendor's service, and previews on the lock screen can show sensitive content, so previews should be hidden. They can also be abused for phishing.
- **GPS and location services.** Let apps and the owner locate the device, which helps recovery and enables geofencing. They also create privacy risk and leak location through apps and **geotagged** photos.
- **Third-party application stores.** Stores other than the platform's official one. They apply little or no vetting, so they are a common route for malware, and are normally blocked on managed devices.

## Reducing the Loss

The real risk of a lost laptop or phone is the value of the data on it. **Strong passwords, encryption, and cable locks** are preventive controls that deter and delay but can be bypassed (encryption by a cold boot attack or a configuration error, a cable lock by cutting it, a password by cracking or by removing the drive). The only measure that actually *reduces* the exposure is **storing minimal sensitive data on the device** in the first place.

## Key Points

- **MDM is the control center**, and application control, content management, asset tracking, and remote wipe are mostly done through it.
- **Lockout and screen locks defend against physical access.** Encryption protects data if they fail.
- **Selective wipe plus storage segmentation** lets the company remove its data without touching personal data.
- **SMS is not a secure channel.**
- **Minimizing the data on the device reduces risk.** Encryption, passwords, and locks are preventive controls that can still be bypassed.
