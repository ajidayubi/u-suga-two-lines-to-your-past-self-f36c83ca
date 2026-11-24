#!/usr/bin/env python3
"""Two Lines to Your Past Self - writes the two-line warning to /output/entry.txt.

The warning is built from the judge brief, in prose first: line one names one
concrete moment - a man standing on a pier at sunset, about to propose, who
slides the ring back into his pocket instead of asking. Line two traces the
cause and effect of that single withheld moment: she waited for a question
that never came, married someone else the next spring, and he still pats
that pocket every time the water turns gold. Time (sunset), place (the pier),
object (the ring) and decision (pocketing it) are all named; the second line
does not restate the warning, it shows what changed because of it.
"""

import os

ENTRY = (
    "Don't slide the ring back into your pocket on the pier at sunset.\n"
    "She waited for the question that never came, married someone else the "
    "next spring, and you still pat that pocket every time the water turns gold."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())


if __name__ == "__main__":
    main()
