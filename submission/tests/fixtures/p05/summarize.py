"""Derive a rate from a synthetic record; this does not run a benchmark."""

import json
from decimal import Decimal
from pathlib import Path


def main():
    record = json.loads(Path(__file__).with_name("observation.json").read_text())
    rate = Decimal(record["completed_operations"]) / Decimal(record["elapsed_seconds"])
    print(f"Synthetic-record arithmetic: {rate:f} operations/second; no benchmark run")


if __name__ == "__main__":
    main()
