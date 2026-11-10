#!/usr/bin/env python3
"""Regenerate the JSON copies of the inventory from the CSV files (the CSVs are authoritative).

    python scripts/csv_to_json.py          # write JSON
    python scripts/csv_to_json.py --check  # exit 1 if any JSON file is out of date
"""
import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = [ROOT / "sensors" / "sensors_tir.csv", ROOT / "satellites" / "satellites_tir.csv",
          ROOT / "excluded_records.csv"]
LIST_FIELDS = {"alt_names", "tir_sensors", "thermal_bands_um"}
NUMBER_FIELDS = {"n_thermal_bands", "native_sampling_m", "product_sampling_m", "swath_km", "revisit_days"}


def convert(value, field):
    if value == "":
        return [] if field in LIST_FIELDS else None
    if field in LIST_FIELDS:
        return json.loads(value)
    if field in NUMBER_FIELDS:
        number = float(value)
        return int(number) if number.is_integer() else number
    return value


def render(path: Path) -> str:
    with path.open(newline="", encoding="utf-8") as f:
        rows = [{k: convert(v, k) for k, v in row.items()} for row in csv.DictReader(f)]
    return json.dumps(rows, indent=2, ensure_ascii=False) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    stale = []
    for path in TABLES:
        if not path.exists():
            continue
        target = path.with_suffix(".json")
        text = render(path)
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != text:
                stale.append(target.relative_to(ROOT))
        else:
            target.write_text(text, encoding="utf-8")
            print(f"wrote {target.relative_to(ROOT)}")
    if stale:
        print("JSON out of date with CSV: " + ", ".join(map(str, stale)), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
