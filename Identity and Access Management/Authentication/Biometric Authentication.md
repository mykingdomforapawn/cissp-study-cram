Type 3 authentication: the subject is identified by a physiological or behavioral trait. Hardest to share or forget, and **unrevocable** — a compromised fingerprint cannot be reissued, which is why biometric templates are stored as derived data rather than raw images.

## Common Biometrics

| Trait | Notes |
|---|---|
| **Fingerprint** | Most deployed; cheap, fast to enroll, moderate accuracy. Matches **minutiae** — **ridges** (the lines), **bifurcations** (where a ridge forks), and **whorls** (circular patterns). Defeated by lifted or molded prints without liveness detection, and a compromised print cannot be reissued |
| **Iris** | Pattern of the colored ring; **highly accurate**, works at a distance, stable over life |
| **Retina** | Blood-vessel pattern at the back of the eye; **most accurate**, but intrusive and can reveal medical conditions — a **privacy** concern |
| **Face** | Convenient and contactless; sensitive to lighting, aging, and demographic bias |
| **Palm / vein** | Subsurface **vein pattern**, not minutiae; contactless and hard to forge |
| **Voice** | Low cost, usable over the phone; affected by illness and defeated by recordings or synthesis |
| **Signature dynamics / keystroke rhythm / gait** | **Behavioral** ("something you do"); continuous or passive, lower accuracy |

## Error Rates

| Metric | Meaning | Consequence |
|---|---|---|
| **FRR** — false rejection rate (**Type I error**) | A legitimate subject is denied | Frustration, support cost, workarounds |
| **FAR** — false acceptance rate (**Type II error**) | An impostor is accepted | **Security breach** — the serious error |
| **CER** — crossover error rate (EER) | Sensitivity where FRR equals FAR | **Lower CER = more accurate system**; the standard way to compare devices |

Sensitivity trades one against the other: raise it and FAR falls while FRR rises. **High-security environments deliberately tune away from the CER** toward a low FAR, accepting rejected legitimate users as the cheaper failure.

Other acceptance factors: **throughput rate** (people processed per minute — iris and fingerprint are fast, retina slow), **enrollment time** (should stay under about two minutes), and **user acceptance**, which is why intrusive scans fail in practice regardless of accuracy.

## Enrollment

The subject's trait is sampled and converted into a **reference template** — a mathematical representation, not an image — stored for later comparison. Poor-quality enrollment causes lifelong false rejections for that user. Some subjects cannot enroll at all (worn fingerprints), so a **fallback path** is mandatory, and that fallback usually sets the system's real strength.

Templates are **personal data**: protect them like secrets, and expect biometric-specific privacy law (see [[State Privacy Laws]]).

## Key Points

- **FRR = Type I (legitimate denied), FAR = Type II (impostor accepted), CER = where they cross.**
- **A lower CER means a better device, but high-security systems tune for low FAR instead.**
- **Biometrics cannot be reissued after compromise; store templates, never raw samples.**
- **Enrollment quality, throughput, and user acceptance decide deployments as much as accuracy does.**
