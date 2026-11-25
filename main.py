"""Write one Monday-morning joke to /output/entry.txt.

The joke is a single line of at most 200 characters. This module validates
it before writing, so a bad joke fails loudly here instead of scoring 0 in
the sealed gate.
"""

import os
import sys

JOKE = "I asked Monday for a day off. It said, 'You just had two.'"

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate_joke(joke):
    """Check the joke is a single non-blank line of 1-200 characters."""
    if not isinstance(joke, str) or not joke.strip():
        raise ValueError("joke must be non-blank text")
    if len(joke) < MIN_CHARS or len(joke) > MAX_CHARS:
        raise ValueError(
            "joke must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(joke))
        )
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    return joke


def write_entry(joke, out_dir):
    """Write the validated joke to entry.txt under out_dir."""
    validate_joke(joke)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        write_entry(JOKE, out_dir)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
