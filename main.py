"""One Letter for Your Day — a single letter describing the day.

The letter is Z: zero sleep, zany, zapped, zonked. A day that ran the
writer down to nothing and kept going anyway. Z is the alphabet's last
letter for a person with nothing left, and the comic-strip symbol for
sleep itself — the day is legible from the letter alone.
"""

import os

LETTER = "Z"

# The gate requires exactly one character, A to Z, and nothing else.
assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "letter must be one A-Z character"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
