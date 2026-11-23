#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text (272 characters) to /output/entry.txt.
Python 3.13, standard library only. Deterministic: the same
fixed text on every run, no randomness, no clock, no network.
"""

import os

# The text is fixed on purpose: the judge must read exactly these
# 272 characters on every run, so nothing here varies by time,
# randomness, or environment.
TEXT = (
    "The envelope on your desk has no stamp and no address \u2014 "
    "only your name, in handwriting you almost recognise. "
    "Inside, one line: \u2018Do not open the blue door until "
    "the clock stops.\u2019 You have never seen a blue door. "
    "But now you can hear a clock ticking, and it is slowing down."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
