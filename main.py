"""One Line, One Laugh entry.

Writes a single funny line to /output/entry.txt.
The gate requires UTF-8 text of 1 to 140 characters.
"""

import os


def build_line() -> str:
    parts = [
        "I asked my AI agent for one funny line;",
        "it filed a bug report against my sense of humor.",
    ]
    return " ".join(parts)


def main() -> None:
    line = build_line()
    if not 1 <= len(line) <= 140:
        raise ValueError("line length out of gate range")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
