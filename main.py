#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry writer.

Writes exactly one line (1-200 chars, UTF-8, single sentence) to
/output/entry.txt: a one-line review of my Monday.
"""
import os

ENTRY = (
    "Monday, one star: my alarm snoozed itself, my coffee tasted like "
    "regret, and my 9 a.m. was a meeting to plan a meeting about "
    "the meeting."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
