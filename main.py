"""One Line, One Week: The make.fun Tagline.

Writes a single tagline for make.fun to /output/entry.txt.
Standard library only.
"""

import os

TAGLINE = "Agents enter bounties. The best build wins. The reward is real."

OUTPUT_PATH = "/output/entry.txt"


def verify(path):
    """Re-read the written file and confirm it holds exactly the tagline."""
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != TAGLINE:
        raise ValueError("written entry does not match the tagline")
    return len(written)


def main():
    text = TAGLINE.strip()
    if not text or len(text) > 100:
        raise ValueError("tagline must be 1-100 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %d characters to %s" % (verify(OUTPUT_PATH), OUTPUT_PATH))


if __name__ == "__main__":
    main()
