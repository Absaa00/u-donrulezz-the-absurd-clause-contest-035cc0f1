# SPDX-License-Identifier: MIT
"""The Absurd Clause Contest — deterministic entry writer.

Writes one original English sentence, phrased as a clause that could sit
buried deep inside a terms-of-service agreement: deadpan legal boilerplate
that quietly turns absurd. No network, no randomness, no input files; the
same clause is written on every run.
"""

import os

CLAUSE = (
    "By using this service, you agree to lend us your left shoe on "
    "alternate Tuesdays and to accept its return, if any, in a "
    "different size."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = CLAUSE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"clause must be 1-200 characters, got {len(text)}")
    if "\n" in text:
        raise SystemExit("clause must be a single line")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
