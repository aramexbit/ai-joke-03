"""ai-joke-03 entry: one-liner joke about AI coding agents.

Writes exactly the joke (no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, standard library only, no network, fully deterministic.
"""

import os

JOKE = "I gave my AI coding agent one ticket. It closed it, opened three bigger ones, and assigned them all to me."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
