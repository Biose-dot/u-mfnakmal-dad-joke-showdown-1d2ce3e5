#!/usr/bin/env python3
"""Dad Joke Showdown — make.fun entry.

Writes one dad joke (a single joke, at most 200 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os

ENTRY = (
    "I asked Dad why he always keeps a pencil behind his ear, and he "
    "said in case he needs to draw the line somewhere."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
