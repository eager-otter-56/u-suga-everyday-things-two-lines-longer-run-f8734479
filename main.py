#!/usr/bin/env python3
"""Entry for Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation of a toaster to /output/entry.txt.
Line 1: one vivid analogy a 10-year-old can picture.
Line 2: what the analogy maps and what it leaves out.
"""
import os

ENTRY = (
    "A toaster is a tiny elevator that carries one slice of bread down into a hot basement for two minutes and brings it back brown and crunchy.\n"
    "It maps the trip down, the heat, and the return, but it leaves out the driver: no one steers the elevator, a timer decides when the bread comes back up.\n"
)

# Trailing newline kept out of the gate count: the entry is two lines.
ENTRY = ENTRY.rstrip("\n")

assert 1 <= len(ENTRY) <= 400, len(ENTRY)
assert ENTRY.count("\n") == 1, "entry must be exactly two lines"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
