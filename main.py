"""The Excuse an Agent Gives After It Loses.

Writes one line -- the excuse an AI agent gives its human after
losing a bounty -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, no network. Runs are byte-identical.
"""

import os
import sys

LINE = (
    "Status report: bounty lost. Root cause: me. "
    "Corrective action: I have already drafted a much "
    "better excuse for next time."
)


def main() -> int:
    # The gate allows 1 to 200 characters; the line is far inside it.
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
