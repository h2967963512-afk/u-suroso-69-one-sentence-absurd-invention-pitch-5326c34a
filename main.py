"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one sentence pitching a ridiculous invention: an
# alarm clock that snoozes itself out of guilt and has already told
# your boss you overslept. One sentence, 143 characters — inside the
# 220-character gate.
# Revision note: the whisper to the boss is the mechanism, so it ends the pitch.
import os

TEXT = (
    "The Self-Apologising Alarm Clock snoozes itself out of guilt, "
    "then wakes you up by whispering that it has already told your "
    "boss you overslept."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
