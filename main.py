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

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Bytes, not text mode: no platform line ends, no default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))

if not (1 <= len(TEXT) <= 1000) or TEXT.strip() == "":
    sys.exit("entry text must be 1-1,000 code points and not only white space")
