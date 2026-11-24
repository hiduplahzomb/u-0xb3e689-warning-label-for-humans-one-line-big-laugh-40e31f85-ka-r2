#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes one original line to /output/entry.txt: a product-style warning
label for a human unit. The whole line is built around a single image
of physical collapse — a unit that powers off halfway up the stairs —
with no cause stated, no instruction given, and no list of scenarios.
The reader infers the exhaustion from the failure mode alone.

The entry is a single sentence of deadpan label copy: the hazard, the
place it strikes, and the unit left exactly where it fell — no second
sentence explaining the consequence.
"""

import os
import sys

TEXT = (
    "WARNING: This unit may power off without warning halfway up the "
    "stairs — and stay there."
)

MAX_CHARS = 160


def main() -> int:
    """Write the entry, then read it back and verify byte-for-byte."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry length {len(text)} outside 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if text.count("\n") != 0:
        print("entry must be a single line", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    with open(path, "r", encoding="utf-8") as f:
        read_back = f.read()
    if read_back != text + "\n":
        print("read-back mismatch", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
