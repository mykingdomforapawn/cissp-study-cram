How an organization provides and governs mobile devices is a business decision with security consequences. The main question is who owns the device, and the policy has to cover the rest.

## Deployment Models

| Model | Meaning | Who owns the device | Personal use | Control |
|---|---|---|---|---|
| **BYOD** (bring your own device) | Employees use their own personal devices for work | Employee | Unrestricted, it is theirs | Lowest. Needs segmentation and consent |
| **CYOD** (choose your own device) | Employee picks from a list of approved models | Usually the company (or approved by it) | Limited | Moderate. Fewer models make management easier |
| **COPE** (corporate-owned, personally enabled) | Company buys and owns the device, and allows some personal use | Company | Allowed within policy | High |
| **COMS** (corporate-owned mobile strategy, also called **COBO**, corporate-owned business-only) | Company provides the device strictly for business | Company | Not allowed | Highest |

BYOD, CYOD, and COPE all let personal and business data mix and leave responsibility for the device's security, updates, and repair less clear. Only COMS makes it unambiguous, since the company owns the device, it is business-only, and the company is responsible for it, at the cost of users carrying a second phone. BYOD is cheap and popular with staff but is hardest to secure. COMS gives the most control and the least flexibility. Ownership decides how much the company may monitor, restrict, or wipe.

## Deployment Policy Details

- **Data ownership.** Corporate data on a device remains corporate property and is kept separate (see storage segmentation in [[Mobile Device Security Features]]). Personal data stays the user's. The agreement should say what happens to each at termination or wipe.
- **Support ownership.** Who supports the device: the company help desk, the user, or the carrier. BYOD usually gets limited support.
- **Patch and update management.** How OS and app updates are applied, the minimum allowed OS version, and blocking devices that fall behind.
- **Secure product management.** Choosing which device models and vendors are approved, based on their security features and patch support record.
- **Forensics.** Whether and how the company can collect evidence from a device for investigations or legal discovery. Personally owned devices complicate this, so the policy must secure the user's consent and handle legal holds.
- **Architecture and infrastructure.** The network and systems that mobile use needs: MDM, VPN, network access control, authentication, wireless capacity, and segmentation of mobile devices from sensitive networks.
- **Legal concerns.** Privacy and employment laws, employee consent to monitoring and remote wipe, liability for lost personal data, regulation of the data on devices, and cross-border issues.
- **Acceptable use policy (AUP).** What users may do with the device, its apps, and its data, with consequences for violations, and signed acknowledgment (see [[Employment Agreements and Policies]]). It is where rules on camera, microphone, tethering, and sideloading are set out (see [[Mobile Device Risks]]).

## Key Points

- **Ownership defines control.** BYOD, CYOD, COPE, and COMS run from least to most corporate control.
- **BYOD needs segmentation and consent**, because company data and personal data share one device.
- **The policy must settle data ownership, support, patching, forensics, and legal rights in advance**, and the AUP makes it binding.
