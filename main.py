"""Write the original contest piece Under the Cloth."""

import os
from pathlib import Path


ENTRY = (
    "The bread is still warm beneath the linen cloth.\n\n"
    "She sits across from me, sleeves rolled to her elbows. A little flour "
    "remains in the crease of her thumb. She lifts one corner of the cloth, "
    "and the smell of the crust comes across the table.\n\n"
    "She lowers the corner again. Her palm follows the round of the loaf, "
    "drawing the linen down along its sides. A loose fold settles on the "
    "wooden board.\n\n"
    "Her hand stays there, and I rest mine beside it. The warmth comes "
    "through the cloth."
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
