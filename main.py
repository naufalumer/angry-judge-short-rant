"""Angry Judge: The Short Rant Contest (make.fun).

A short, funny rant about an everyday annoyance: the lift
close-door button that has never once closed a door. The rant is
288 characters, inside the 1-400 gate. The program
drops that rant into $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing
newline, so the file's byte count is the rant's character count.
Standard library only.
"""

import os
from pathlib import Path

ENTRY = (
    "I have pressed the close-door button in my lift 4,000 times. "
    "It has never once closed a door. It is a toy they installed "
    "to keep adults quiet, like the steering wheel on a supermarket "
    "trolley, and every morning I still press it, because hope is "
    "the only thing in this building that works."
)

MAX_CHARS = 400


def check_entry(text: str) -> None:
    """Refuse to ship anything the sealed gate would call invalid."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    check_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with target.open("w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
