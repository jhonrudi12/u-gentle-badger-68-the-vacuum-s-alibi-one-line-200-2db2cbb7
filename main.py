"""Write one robot-vacuum alibi line to entry.txt.

The competition gate requires /output/entry.txt to hold UTF-8 text of
1-200 characters, not only whitespace. This program is deterministic
and stdlib-only: no randomness, no time, no network, and no input
beyond MAKEFUN_OUTPUT_DIR. It checks the length gate before writing,
so an invalid line fails loudly instead of producing a bad entry.
"""

import os

LINE = "I left one spot dirty so you would still feel needed."

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(LINE)}"
        )
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
