#!/usr/bin/env python3
"""Style checks on the card Markdown that generate.py does not enforce.

Usage:  python3 cards/lint.py [path ...]

Two checks, both about what the learner sees on the *front* of a card:

  length   The correct option must not be the giveaway. Flags a card whose
           correct option text (before the rationale dash) is the longest of
           the four by more than LENGTH_SLACK characters.

  abbrev   An abbreviation must be expanded the first time it appears on the
           front, unless it is ordinary professional vocabulary (NEVER_EXPAND).

Exits non-zero if anything is flagged. See cards/CLAUDE.md.
"""

import collections
import pathlib
import re
import sys

CARDS_DIR = pathlib.Path(__file__).parent

# How much longer than the longest distractor the correct option may be.
LENGTH_SLACK = 12

# Ordinary professional vocabulary: expanding these teaches nothing.
NEVER_EXPAND = {
    "API", "SaaS", "PaaS", "IaaS", "VPN", "OS", "IT", "HR", "CEO", "CFO",
    "CISO", "CIO", "URL", "HTTP", "HTTPS", "IP", "IPv4", "IPv6", "TCP", "UDP",
    "DNS", "LAN", "WAN", "VLAN", "PC", "USB", "SQL", "PDF", "HVAC", "ID",
    "FAQ", "GPS", "SMS", "AI", "ML", "TLS", "IoT", "GHz", "MHz", "Wi-Fi",
}

# Emphasised words in a stem, not abbreviations. Any all-caps run that is a
# plain English word belongs here rather than being flagged for expansion.
QUALIFIERS = {
    "BEST", "MOST", "FIRST", "PRIMARY", "PRIMARILY", "NEXT", "LEAST", "NOT",
    "HIGHEST", "LOWEST", "GREATEST", "ALL", "ONLY", "BOTH", "NEVER", "EACH",
    "SECOND", "THIRD", "MORE", "LESS", "CORRECT", "AGAINST", "MAIN", "OR",
    "AND", "EXPLAINS", "DESIGNED", "COMPLETE", "ADEQUATE", "PURPOSE-BUILT",
    "BEFORE", "AFTER", "ALWAYS", "WORST", "LIKELY", "MUST", "SHOULD",
    "RE",
}

# Names, not abbreviations: nothing to expand.
PROPER_NAMES = {
    "LaPadula", "ElGamal", "ActiveX", "JavaScript", "JSON", "HTML", "XML",
    "DomainKeys", "SKIPJACK", "RACE", "EdDSA", "SoC", "TEMPEST", "RJ-45",
    "FM-200", "CO2", "US", "EU", "FBI", "NSA", "NIST", "II", "PVC", "NT", "OpenID", "OAuth",
}

ABBREV = re.compile(r"\b([A-Z][A-Za-z0-9]*[A-Z][A-Za-z0-9+]*(?:-[A-Za-z0-9]+)?)\b")
CARD_RE = re.compile(
    r"^## (Card \d+)\s*$(.*?)(?=^## Card |\Z)", re.MULTILINE | re.DOTALL
)
FIELD_RE = r"\*\*{}\*\*\s*\n(.*?)(?=\n\*\*|\Z)"


def cards(path):
    text = path.read_text(encoding="utf-8")
    for m in CARD_RE.finditer(text):
        body = m.group(2)
        q = re.search(FIELD_RE.format("Question"), body, re.DOTALL)
        o = re.search(FIELD_RE.format("Options"), body, re.DOTALL)
        if not (q and o):
            continue
        options = [ln.strip() for ln in o.group(1).strip().splitlines() if ln.strip()]
        yield m.group(1), q.group(1).strip(), options


def split(option):
    """-> (is_correct, option text as shown on the front)"""
    correct = option.startswith("*")
    body = option[1:] if correct else option
    return correct, re.split(r"\s[—–-]\s", body, maxsplit=1)[0].strip()


def check_length(where, options, out):
    parsed = [split(o) for o in options]
    if len(parsed) != 4 or sum(c for c, _ in parsed) != 1:
        return  # generate.py reports these
    key = next(t for c, t in parsed if c)
    others = max(len(t) for c, t in parsed if not c)
    if len(key) > others + LENGTH_SLACK:
        out.append(
            f"{where}: correct option is {len(key) - others} chars longer than "
            f"any distractor ({len(key)} vs {others})"
        )


def check_abbrev(where, question, options, out):
    front = question + "\n" + "\n".join(t for _, t in (split(o) for o in options))
    # Spans of parenthesised text: an abbreviation inside one is part of an
    # expansion already given ("CCMP (Counter Mode CBC-MAC Protocol)").
    spans = [(m.start(), m.end()) for m in re.finditer(r"\([^()]*\)", front)]
    seen = set()
    for m in ABBREV.finditer(front):
        inside = any(a < m.start() and m.end() < b for a, b in spans)
        token = m.group(1)
        root = token[:-1] if token.endswith("s") and token[:-1].isupper() else token
        # "VoIP-related", "IPv6-only": judge the base, not the compound.
        head_token = root.split("-")[0]
        # "EAL4" -> "EAL", but never "IPv6" -> "IPv": only strip the digits if
        # the lettered stem is a known abbreviation.
        stem = re.sub(r"\d+$", "", head_token)
        base = head_token
        if head_token not in NEVER_EXPAND and head_token not in PROPER_NAMES:
            if stem in NEVER_EXPAND or stem in PROPER_NAMES or stem in seen:
                base = stem
        if base in NEVER_EXPAND or base in PROPER_NAMES or base in seen:
            seen.add(root)
            continue
        if root in QUALIFIERS or root in NEVER_EXPAND or root in PROPER_NAMES or root in seen:
            continue
        if inside and front[m.start() - 1] != "(":
            seen.add(root); seen.add(base)
            continue
        seen.add(root)
        seen.add(base)
        tail = front[m.end():m.end() + 2]
        head = front[:m.start()]
        # Either order counts: "EAL (Evaluation Assurance Level)" and
        # "Evaluation Assurance Level (EAL)".
        if tail == " (" or tail.startswith("("):
            continue
        if head.endswith("(") and tail.startswith(")"):
            continue
        if head.rstrip().endswith(")"):
            continue
        out.append(f"{where}: abbreviation {token!r} is not expanded on first use")


def main(argv):
    paths = (
        [pathlib.Path(a) for a in argv]
        if argv
        else sorted(p for p in CARDS_DIR.glob("*/*.md") if p.parent.name != "build")
    )
    out = []
    counts = collections.Counter()
    for path in paths:
        for name, question, options in cards(path):
            where = f"{path}: {name}"
            before = len(out)
            check_length(where, options, out)
            counts["length"] += len(out) - before
            before = len(out)
            check_abbrev(where, question, options, out)
            counts["abbrev"] += len(out) - before
    for line in out:
        print(line)
    if out:
        print(
            f"\n{len(out)} issues "
            f"({counts['length']} length, {counts['abbrev']} abbrev)",
            file=sys.stderr,
        )
        return 1
    print("lint: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
