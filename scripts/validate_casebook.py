#!/usr/bin/env python3
"""Validate structural invariants of an OpenReview Casebook HTML file."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
    "meta", "param", "source", "track", "wbr",
}


class StructuralParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.unexpected: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag not in VOID_TAGS:
            self.stack.append(tag)

    def handle_startendtag(self, tag: str, attrs) -> None:
        return

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID_TAGS:
            return
        if tag not in self.stack:
            self.unexpected.append(tag)
            return
        index = len(self.stack) - 1 - self.stack[::-1].index(tag)
        del self.stack[index]


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"file does not exist: {path}"]

    text = path.read_text(encoding="utf-8")
    parser = StructuralParser()
    parser.feed(text)
    if parser.unexpected:
        errors.append(f"unexpected closing tags: {parser.unexpected[:8]}")
    if parser.stack:
        errors.append(f"unclosed tags: {parser.stack[:8]}")

    required_fragments = {
        "UTF-8 declaration": '<meta charset="utf-8"',
        "responsive viewport": 'name="viewport"',
        "search control": 'type="search"',
        "filter chips": 'data-filter=',
        "paper cards": 'class="paper-card"',
        "details controls": 'details-btn',
        "source disclosure": 'source-box',
        "print stylesheet": '@media print',
        "mobile stylesheet": '@media (max-width:',
        "source controls": 'class="linkbtn"',
    }
    for label, fragment in required_fragments.items():
        if fragment not in text:
            errors.append(f"missing {label}: {fragment}")

    if text.count('<article class="paper-card"') < 3:
        errors.append("fewer than three paper cards")
    source_count = text.count('https://openreview.net/') + text.count('data-source-placeholder="openreview-url"')
    if source_count < 3:
        errors.append("fewer than three official OpenReview links or template source placeholders")
    if re.search(r"(?:\[TODO\]|\[TBD\]|\{\{[^}]+\}\}|lorem ipsum)", text, re.I):
        errors.append("unfinished placeholder text found")
    if re.search(r"<(script|link)[^>]+(?:src|href)=[\"']https?://", text, re.I):
        errors.append("external runtime dependency found; output must work offline")
    if '<script' not in text or '</script>' not in text:
        errors.append("interactive script is missing")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", type=Path)
    args = parser.parse_args()
    errors = validate(args.html)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {args.html}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
