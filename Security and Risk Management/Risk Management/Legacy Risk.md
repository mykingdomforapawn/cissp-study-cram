Legacy systems pose a distinct risk category: they are often critical to operations but cannot be easily patched, updated, or replaced. The risk increases as the vendor winds down support. See [[Security Controls]] for how compensating controls apply here.

## End-of-Life Terminology

- **EOL (End of Life)** — the vendor no longer sells or actively develops the product; updates may still exist but the product is on a deprecation path
- **EOS (End of Support)** — the vendor no longer provides technical support or assistance; the product is on its own
- **EOSL (End of Secure Life)** — the vendor no longer releases security patches; any newly discovered vulnerabilities will remain unmitigated indefinitely

EOSL is the critical threshold from a risk perspective. A system past EOSL accumulates unpatched vulnerabilities over time, and the risk grows with each new CVE that goes unaddressed.

## Managing Legacy Risk

When replacement isn't feasible, compensating controls reduce exposure: network segmentation to isolate the system, enhanced monitoring, strict access controls, and documented risk acceptance by the appropriate owner. The residual risk must be reviewed regularly — what was acceptable at EOSL may not remain so as the vulnerability landscape evolves.
