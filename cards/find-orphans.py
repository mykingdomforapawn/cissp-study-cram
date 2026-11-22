#!/usr/bin/env python3
"""Find Anki notes whose Question no longer matches any card in the Markdown.

Usage:  python3 cards/find-orphans.py <deck-export.txt>

Anki matches notes on the first field, Question. Editing an option updates the
note in place on re-import; editing the question text creates a *new* note and
leaves the old one behind as a duplicate. This script finds those leftovers.

To produce the export: in Anki, File -> Export, "Notes in Plain Text (.txt)",
the CISSP deck, "Include HTML and media references" ticked.

For each orphan it prints a Browse search matching the OLD wording, so the
stale note can be found and deleted. Nothing is changed by this script.
"""

import html
import pathlib
import re
import sys

CARDS_DIR = pathlib.Path(__file__).parent


def normalize(text):
    """Compare on words alone: markup, entities and spacing are noise here."""
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    return " ".join(text.split()).lower()


def markdown_questions():
    questions = {}
    for path in sorted(CARDS_DIR.glob("*/*.md")):
        if path.parent.name == "build":
            continue
        text = path.read_text(encoding="utf-8")
        for m in re.finditer(
            r"^## (Card \d+)\s*$(.*?)(?=^## Card |\Z)", text, re.MULTILINE | re.DOTALL
        ):
            q = re.search(
                r"\*\*Question\*\*\s*\n(.*?)(?=\n\*\*|\Z)", m.group(2), re.DOTALL
            )
            if q:
                questions[normalize(q.group(1))] = f"{path}: {m.group(1)}"
    return questions


def exported_questions(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        yield line.split("\t")[0]


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    export = pathlib.Path(argv[0])
    if not export.is_file():
        print(f"no such export file: {export}", file=sys.stderr)
        return 2

    known = markdown_questions()
    orphans = [q for q in exported_questions(export) if normalize(q) not in known]

    print(f"{len(known)} cards in Markdown, {len(orphans)} notes in Anki with no match\n")
    for q in orphans:
        plain = html.unescape(re.sub(r"<[^>]+>", "", q))
        # A distinctive middle slice: start and end wording is often shared.
        words = plain.split()
        probe = " ".join(words[:12]) if len(words) > 12 else plain
        print(f"  {plain[:110]}")
        print(f'    Browse:  "Question:{probe}*"\n')
    if orphans:
        print("Delete these notes in Anki, then re-import the topic files.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
