#!/usr/bin/env python3
"""Write the entry: one toaster error message, max 120 characters."""

import os

ENTRY = "E03: Crumb tray 94% full. At 100% I legally become a fire."


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 120:
        raise ValueError(f"entry must be 1-120 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
