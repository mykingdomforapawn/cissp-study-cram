#!/usr/bin/env python3
"""Turn the card Markdown under cards/ into a file Anki can import.

Usage:  python3 cards/generate.py

Reads every cards/<domain>/<topic>.md, parses the `## Card N` blocks, and
writes one tab-separated import file per topic to cards/build/, plus a
combined all-cards.txt. Import a single topic file to update just that topic.
See cards/CLAUDE.md for the card format.
"""

import pathlib
import re
import sys

CARDS_DIR = pathlib.Path(__file__).parent
BUILD_DIR = CARDS_DIR / "build"

# Deck path every card is filed under, before the domain and topic.
DECK_ROOT = "Certifications::CISSP"

FIELDS = ("Domain", "Question", "Options", "Source")
# Column order in the output file. Must match the note type's field order.
COLUMNS = ("Question", "Options", "Domain", "Source")

HEADER = [
    "#separator:tab",
    "#html:true",
    "#notetype:CISSP Scenario",
    "#deck column:5",
    "#tags column:6",
]


def parse_file(path):
    """Yield one dict of field name -> raw text per `## Card` block."""
    text = path.read_text(encoding="utf-8")
    # Drop YAML frontmatter and everything before the first card.
    blocks = re.split(r"^## Card\b.*$", text, flags=re.MULTILINE)[1:]

    for block in blocks:
        card = {}
        label = None
        for line in block.splitlines():
            m = re.fullmatch(r"\*\*(\w+)\*\*", line.strip())
            if m:
                label = m.group(1)
                card[label] = []
            elif label and line.strip():
                card[label].append(line.rstrip())
        yield {k: "\n".join(v).strip() for k, v in card.items()}


def parse_options(raw, where):
    """Split the Options field into lines and validate it."""
    lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
    correct = [ln for ln in lines if ln.startswith("*")]

    if len(lines) != 4:
        warn(f"{where}: {len(lines)} options, expected 4")
    if len(correct) != 1:
        warn(f"{where}: {len(correct)} options marked correct, expected exactly 1")
    for ln in lines:
        body = ln[1:] if ln.startswith("*") else ln
        if not re.search(r"\s[—–-]\s", body):
            warn(f"{where}: option has no rationale after a dash: {body[:60]}...")

    return "".join(f"<div>{ln}</div>" for ln in lines)


def deck_for(domain, where):
    """'1 — Security and Risk Management / Risk Management' -> deck path."""
    m = re.fullmatch(r"(\d+)\s*[—–-]\s*(.+?)\s*/\s*(.+)", domain)
    if not m:
        warn(f"{where}: cannot derive deck from Domain: {domain!r}")
        return DECK_ROOT
    number, domain_name, topic = m.groups()
    return f"{DECK_ROOT}::{number} {domain_name}::{topic}"


def tags_for(domain, source):
    """A tag per card: the domain number plus a slug of the source note."""
    tags = ["cissp"]
    m = re.match(r"(\d+)", domain)
    if m:
        tags.append(f"domain{m.group(1)}")
    for link in re.findall(r"\[\[([^\]|]+)", source):
        slug = re.sub(r"[^a-z0-9]+", "-", link.lower()).strip("-")
        tags.append(slug)
    return " ".join(tags)


warnings = []


def warn(message):
    warnings.append(message)


def write_file(path, rows):
    """Write one import file: the headers, then a line per card."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        for line in HEADER:
            fh.write(line + "\n")
        for row in rows:
            fh.write("\t".join(row) + "\n")


def main():
    by_source = {}

    for path in sorted(CARDS_DIR.rglob("*.md")):
        if path.name == "CLAUDE.md" or "anki-template" in path.parts:
            continue

        for index, card in enumerate(parse_file(path), start=1):
            where = f"{path.relative_to(CARDS_DIR)} card {index}"

            missing = [f for f in FIELDS if not card.get(f)]
            if missing:
                warn(f"{where}: missing field(s) {', '.join(missing)} — skipped")
                continue

            card["Options"] = parse_options(card["Options"], where)
            row = [card[c] for c in COLUMNS]
            row.append(deck_for(card["Domain"], where))
            row.append(tags_for(card["Domain"], card["Source"]))

            if any("\t" in value for value in row):
                warn(f"{where}: contains a tab character — skipped")
                continue

            by_source.setdefault(path, []).append(row)

    # Clear stale output so a renamed or deleted topic file leaves nothing behind.
    for stale in BUILD_DIR.rglob("*.txt"):
        stale.unlink()

    combined = []
    for source, rows in sorted(by_source.items()):
        relative = source.relative_to(CARDS_DIR).with_suffix(".txt")
        write_file(BUILD_DIR / relative, rows)
        combined.extend(rows)
        print(f"{len(rows):4d}  build/{relative}")

    write_file(BUILD_DIR / "all-cards.txt", combined)
    print(f"{len(combined):4d}  build/all-cards.txt (everything)")

    for message in warnings:
        print(f"  warning: {message}", file=sys.stderr)
    return 1 if warnings else 0


if __name__ == "__main__":
    sys.exit(main())
