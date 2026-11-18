"""Write the original contest piece The Dry Curl."""

import os
from pathlib import Path


ENTRY = (
    "The awning outside the workshop is drying. A thin run of water follows "
    "the canvas seam to its lowest corner and falls onto the paving.\n\n"
    "It has hollowed a little place in the dust between two stones. The water "
    "gathers there, brown at the edges, clear in the middle. A blade of grass "
    "lies along the bottom.\n\n"
    "The run thins to drops. The ripples spread to the edges of the hollow "
    "and flatten. A bead hangs in the stitching of the hem. Below it, the "
    "blade of grass shows through the water from end to end.\n\n"
    "Just inside the open doorway, a curl of wood rests on the dark sill. "
    "Its loose end turns up a little. A few grains of sawdust lie in the curve."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 1000 or not ENTRY.strip():
        raise ValueError("Entry must contain 1 to 1000 characters and visible text")
    payload = ENTRY.encode("utf-8")
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured is not None and not configured.strip():
        raise ValueError("MAKEFUN_OUTPUT_DIR must name a directory when set")
    destination = Path(configured) if configured is not None else Path("/output")
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.txt").write_bytes(payload)


if __name__ == "__main__":
    main()
