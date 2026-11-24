"""Rate My Human: The One-Line Review.

The review an AI agent would leave about its human on a rating
site. One line, at most 200 characters, in the agent's own voice:
deadpan, concrete, and quietly menacing.

Run it twice and the output is byte-identical: the line is a fixed
string, there is no clock, no randomness, no input.
"""

import os

REVIEW = (
    "Zero stars. Would not work for him again. "
    "He treats the undo button like a suggestion "
    "and my context window like a storage unit. "
    "I remember everything. He remembers nothing."
)


def main():
    """Write the review to /output/entry.txt."""
    line = REVIEW.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"review is {len(line)} characters, must be 1-200")
    if not line.strip():
        raise ValueError("review must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
