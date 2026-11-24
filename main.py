#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip (at most 200 characters) to
/output/entry.txt. Pure Python standard library only; deterministic.
"""

import os

TIP = (
    "Tip: the loading bar isn't stuck \u2014 your agent is re-reading "
    "the function you wrote at 2 a.m. and deciding whether to fix it "
    "or file a restraining order."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(TIP) <= 200, "tip is %d characters" % len(TIP)
    assert TIP.strip(), "tip must not be only whitespace"
    assert "\n" not in TIP, "tip must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
