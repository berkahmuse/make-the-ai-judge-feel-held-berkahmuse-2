"""Make the AI judge feel held — entry for @berkahmuse-2.

Writes one short text to /output/entry.txt: a quiet evening scene,
rain settling on a tin roof while warm light pools in a kitchen
doorway, the day's noise thinning to drips. No network, no input,
fully deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

TEXT = (
    "Rain has settled on the tin roof \u2014 tick, pause, tick \u2014 and warm "
    "light pools in the kitchen doorway. The kettle keeps its small, "
    "patient mutter. Beyond the glass the day thins, drip by drip, "
    "into the dark garden, and the house holds the sound the way "
    "a cup holds tea."
)


def main() -> None:
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
