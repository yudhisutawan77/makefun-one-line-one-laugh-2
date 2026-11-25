"""One Line, One Laugh -- make.fun entry.

Writes a single funny line (<= 200 characters) to /output/entry.txt
and prints the identical text to stdout.
"""

import os
import sys


ENTRY = (
    "My doctor said I need more exercise, so now I run out of "
    "patience, money, and excuses \u2014 mostly in that order."
)


def entry_text():
    """Return the entry line, exactly as it must appear in the output."""
    return ENTRY


def check_entry(text):
    """Enforce the sealed gate: 1 to 200 UTF-8 characters, not blank."""
    if not text or text.isspace():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    text.encode("utf-8")
    return text


def write_entry(path):
    """Write the entry text to path, creating parent dirs as needed.

    If path is an existing directory, write entry.txt inside it, since
    some harnesses pass ENTRY_OUT as a directory rather than a file.
    """
    if os.path.isdir(path):
        path = os.path.join(path, "entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


def main():
    text = check_entry(entry_text())
    target = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    write_entry(target)
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
