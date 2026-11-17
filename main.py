"""ai-judge-relax-01 entry (Python 3.13, standard library only).

Writes the fixed text TEXT to /output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt
when that variable is set. The file is UTF-8 with no trailing newline, the same bytes
on every run, and nothing is read from the network. Exits 1 if TEXT is not 1 to
MAX_CODE_POINTS code points or is only white space, otherwise 0.
"""

import os
import sys

TEXT = """\
The duck comes down onto the pond with a short scrape of water. Rings go out from her and reach the reeds and stop.

She paddles to the middle, where the last light lies flat. She dips her bill, lifts it, and the water runs off in drops. One. Two. A while later, one more.

She shakes her wings out and folds them, the brown over the blue, and settles a little lower in the water.

Then she turns her head and lays her bill along her back, deep in the feathers. One eye stays open. It closes. Later it opens, finds the reeds still there, and closes again.

Under the water her feet keep moving, slower each time. Then once. Then not.

The light goes off the pond. A small wind crosses it and turns her halfway round, as it would a leaf.

All night the water carries her a little this way and a little that way, and never anywhere at all."""

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
