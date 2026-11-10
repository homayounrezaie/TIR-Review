#!/usr/bin/env python3
"""Calculate the inventory numbers and figure tables used in Rezaie & Hay (Remote Sensing, 2026).

Reads sensors/sensors_tir.csv and satellites/satellites_tir.csv, checks them against the
rules in DATA_DICTIONARY.md, prints the totals reported in the paper and writes the tables
behind Figure 12 and Figure 17.

    python scripts/calculate_figures.py                 # checks + summary
    python scripts/calculate_figures.py --out results/  # also write the figure tables as CSV

Exits with status 1 if any data rule is broken.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SENSORS_CSV = ROOT / "sensors" / "sensors_tir.csv"
SATELLITES_CSV = ROOT / "satellites" / "satellites_tir.csv"

AUDIT_DATE = date(2026, 8, 18)
FIRST_YEAR, LAST_YEAR = 1960, AUDIT_DATE.year

STATUSES = ["operational", "commissioning", "planned", "proposed", "retired", "failed", "unresolved"]
HISTORICAL = {"retired", "failed"}
NOT_IN_FIGURE12 = {"commissioning", "planned", "proposed", "failed", "unresolved"}
NOT_A_FIRST_LAUNCH = {"planned", "proposed", "failed", "unresolved"}
PURPOSES = {"surface imaging", "sounding", "radiometry", "other"}
VALUE_TYPES = {"specified", "measured", "provider-reported", "sharpened", ""}
COOLING = {"cryogenic", "passive_radiative", "uncooled", ""}
CALIBRATED = {"yes", "no", ""}


def year_of(value) -> int | None:
    """Year from an ISO date that may be YYYY, YYYY-MM or YYYY-MM-DD; None if empty."""
    value = str(value).strip()
    return int(value[:4]) if value else None


def load():
    sensors = pd.read_csv(SENSORS_CSV, dtype=str, keep_default_na=False)
    sats = pd.read_csv(SATELLITES_CSV, dtype=str, keep_default_na=False)
    sats["tir_sensors_list"] = sats["tir_sensors"].apply(json.loads)
    sensors["native_sampling_m_num"] = pd.to_numeric(sensors["native_sampling_m"], errors="coerce")
    return sensors, sats


def check_rules(sensors, sats) -> list[str]:
    errors = []
    for col, allowed, df, name in [
        ("status_2026_08_18", set(STATUSES), sats, "satellites"),
        ("primary_purpose", PURPOSES, sensors, "sensors"),
        ("value_type", VALUE_TYPES, sensors, "sensors"),
        ("cooled", COOLING, sensors, "sensors"),
        ("calibrated_data", CALIBRATED, sensors, "sensors"),
    ]:
        bad = sorted(set(df.loc[~df[col].isin(allowed), col]))
        if bad:
            errors.append(f"{name}.{col}: values outside the allowed list: {bad}")
    for df, key, name in [(sensors, "acronym", "sensors"), (sats, "name", "satellites")]:
        dup = sorted(set(df.loc[df[key].duplicated(keep=False), key]))
        if dup:
            errors.append(f"{name}: duplicate {key}: {dup}")
    known = set(sensors["acronym"])
    used = {s for lst in sats["tir_sensors_list"] for s in lst}
    if used - known:
        errors.append(f"satellites.tir_sensors names unknown designs: {sorted(used - known)}")
    if known - used:
        errors.append(f"designs with no platform deployment: {sorted(known - used)}")
    if (sats["status_source"] == "").any():
        errors.append("deployments without status_source: " + ", ".join(sats.loc[sats["status_source"] == "", "name"]))
    if (sensors["spec_source"] == "").any():
        errors.append("designs without spec_source: " + ", ".join(sensors.loc[sensors["spec_source"] == "", "acronym"]))
    for r in sats.itertuples():
        st, start, end = r.status_2026_08_18, year_of(r.operational_start), year_of(r.end_date)
        if st == "operational" and r.end_date and r.end_date <= AUDIT_DATE.isoformat():
            errors.append(f"{r.name}: operational but end_date {r.end_date} is before the audit date")
        if st == "retired" and not r.end_date:
            errors.append(f"{r.name}: retired without end_date")
        if st in {"operational", "retired"} and not (r.operational_start or r.launch_date):
            errors.append(f"{r.name}: {st} without operational_start or launch_date")
        if start and end and end < start:
            errors.append(f"{r.name}: end_date before operational_start")
    return errors


def operational_by_year(sats) -> pd.Series:
    """Figure 12: deployments operational on 31 December of each year (on the audit date for 2026).

    A deployment counts from the year of operational_start (launch_date when no separate start
    is recorded) up to, but not including, the year of end_date. Only partial dates are needed,
    because the count is by year. Commissioning, planned, proposed, failed and unresolved
    deployments are not counted in any year.
    """
    counts = pd.Series(0, index=range(FIRST_YEAR, LAST_YEAR + 1), name="operational_deployments")
    for r in sats.itertuples():
        if r.status_2026_08_18 in NOT_IN_FIGURE12:
            continue
        start = year_of(r.operational_start) or year_of(r.launch_date)
        end = year_of(r.end_date)
        for y in range(max(start, FIRST_YEAR), LAST_YEAR):
            if end is not None and y >= end:
                break
            counts[y] += 1
    counts[LAST_YEAR] = int((sats["status_2026_08_18"] == "operational").sum())
    return counts


def sampling_records(sensors, sats) -> pd.DataFrame:
    """Figure 17: successive records in finest nominal native sampling.

    Each design is placed at the launch date of its first deployment that delivered data
    (not planned, proposed, failed or unresolved). Designs with calibrated_data = no are
    skipped. A design sets a record when its native_sampling_m is finer than every earlier one.
    """
    first = {}
    for r in sats.itertuples():
        if r.status_2026_08_18 in NOT_A_FIRST_LAUNCH or not r.launch_date:
            continue
        for s in r.tir_sensors_list:
            key = (r.launch_date, r.name)
            if s not in first or key < first[s]:
                first[s] = key
    rows = []
    for s in sensors.itertuples():
        if s.calibrated_data == "no" or s.acronym not in first or pd.isna(s.native_sampling_m_num):
            continue
        launch, platform = first[s.acronym]
        rows.append((year_of(launch), launch, s.acronym, platform, s.native_sampling_m_num, s.value_type))
    df = pd.DataFrame(rows, columns=["year", "launch_date", "design", "platform", "native_sampling_m", "value_type"])
    best, out = float("inf"), []
    for r in df.sort_values(["launch_date", "native_sampling_m"]).itertuples(index=False):
        if r.native_sampling_m < best:
            best = r.native_sampling_m
            out.append(r._asdict())
    return pd.DataFrame(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, help="directory for the figure tables (CSV)")
    args = ap.parse_args()

    sensors, sats = load()
    errors = check_rules(sensors, sats)

    links = int(sats["tir_sensors_list"].apply(len).sum())
    multi = int((sats["tir_sensors_list"].apply(len) > 1).sum())
    status = sats["status_2026_08_18"].value_counts().reindex(STATUSES, fill_value=0)
    print("Totals")
    print(f"  instrument designs:          {len(sensors)}")
    print(f"  platform deployments:        {len(sats)}")
    print(f"  instrument-deployment links: {links} ({multi} deployments carry more than one design)")
    print("  status on 18 Aug 2026:       " + ", ".join(f"{k} {v}" for k, v in status.items())
          + f" (historical {int(status[list(HISTORICAL)].sum())})")
    no_start = int((sats["operational_start"] == "").sum())
    partial = int(sats[["launch_date", "operational_start", "end_date"]]
                  .apply(lambda c: c.str.len().isin([4, 7])).sum().sum())
    print(f"  deployments without operational_start (launch_date used): {no_start}")
    print(f"  partial dates (YYYY or YYYY-MM):                          {partial}")

    series = operational_by_year(sats)
    print("\nFigure 12: operational deployments per year")
    for decade in range(FIRST_YEAR, LAST_YEAR + 1, 10):
        years = [y for y in range(decade, decade + 10) if y in series.index]
        print(f"  {decade}s: " + " ".join(f"{series[y]:>3d}" for y in years))
    peak = series.max()
    print(f"  peak {peak} in {sorted(series[series == peak].index.tolist())}")

    rec = sampling_records(sensors, sats)
    print("\nFigure 17: successive records in finest nominal native sampling")
    for r in rec.itertuples():
        print(f"  {r.year}  {r.design:<24} {r.platform:<24} {r.native_sampling_m:>9g} m  {r.value_type}")

    if args.out:
        args.out.mkdir(parents=True, exist_ok=True)
        series.rename_axis("year").to_csv(args.out / "figure12_operational_by_year.csv")
        rec.to_csv(args.out / "figure17_sampling_records.csv", index=False)
        print(f"\nWrote figure tables to {args.out}/")

    if errors:
        print(f"\n{len(errors)} data rule(s) broken:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)
    print("\nAll data rules passed.")


if __name__ == "__main__":
    main()
