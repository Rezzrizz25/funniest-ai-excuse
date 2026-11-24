#!/usr/bin/env python3
"""Funniest AI Excuse — make.fun entry.

Writes one line — the funniest excuse an AI agent gives after failing
a task — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only, no network.
"""

import os
from pathlib import Path

# The line: an excuse in the agent's own voice, one concrete scene
# (the wrong tab), no explanation of its own joke, no stock gag about
# hallucinations, reboots or training data.
ENTRY = (
    "I finished your task in the wrong tab, so someone else's project "
    "is now flawless and yours is completely untouched."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-200")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
