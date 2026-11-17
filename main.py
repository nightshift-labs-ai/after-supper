"""ai-judge-relax-01 entry (Python 3.13, standard library only).

Writes the fixed text TEXT to /output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt
when that variable is set. The file is UTF-8 with no trailing newline, the same bytes
on every run, and nothing is read from the network. Exits 1 if TEXT is not 1 to
MAX_CODE_POINTS code points or is only white space, otherwise 0.
"""

import os
import sys

TEXT = """\
The porch boards give back the day's heat slowly, the way they took it in.

Past the steps, in the long grass, the crickets keep count. At dusk they are quick, one bright thread of sound with no gaps in it. As the air cools, they slow. A cricket can only sing as fast as the night is warm.

Mae sits in the cane chair with her shoes off and her heels on the rail. Her father taught her the sum: the chirps in fourteen seconds, plus forty, is the warmth of the air. She counts without meaning to. Thirty. Later, twenty-four. Later, seventeen.

The gaps open. A chirp, a long breath of nothing, a chirp.

The moth on the screen door has stopped trying for the kitchen light.

By the time the boards are as cool as the air, Mae is asleep in the chair. One cricket by the bottom step is still at it, slower than her heartbeat now, letting the last of the day out of the grass one note at a time."""

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
