# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one fixed text to /output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set.
# UTF-8, no trailing newline, deterministic, no network.

import os
import sys

TEXT = """\
The plates are washed and stacked, the blue one on top.
The pan is back on its hook.
The bread is wrapped in a tea towel.
The rest of the soup is in a jar, the lid turned until it stopped.
The table is wiped, the crumbs saved in a saucer for the morning sparrows.
The chairs are pushed in.
The dog has had her walk. She is asleep by the radiator, one ear turned inside out.
The letters are answered. The one that can wait is face down on the shelf, waiting.
The clock in the hall keeps time on its own.
Upstairs, someone has already turned out the lamp.
Outside, the snow has covered the car, the woodpile, the path to the gate, and stopped.

Under the floor, the last of the washing-up water is still on its way down through the pipes, slower now, and slower, until there is nowhere lower for it to go."""

MAX_CODE_POINTS = 1000


def output_path():
    """Return the entry file path: $MAKEFUN_OUTPUT_DIR/entry.txt if set, else /output/entry.txt."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def text_is_valid(text):
    """True if text is 1 to MAX_CODE_POINTS code points and not only white space."""
    return 1 <= len(text) <= MAX_CODE_POINTS and not text.isspace()


def main():
    # Bytes, not text mode: no platform line ends, no default encoding.
    with open(output_path(), "wb") as f:
        f.write(TEXT.encode("utf-8"))
    if not text_is_valid(TEXT):
        print("entry text must be 1-1,000 code points and not only white space", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
