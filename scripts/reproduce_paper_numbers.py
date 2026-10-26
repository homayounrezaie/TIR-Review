#!/usr/bin/env python3
"""Reproduce the inventory numbers reported in Rezaie & Hay (Remote Sensing, 2026).

Reads sensors/sensors_tir.csv and satellites/satellites_tir.csv, validates them against
DATA_DICTIONARY.md, recomputes every number the paper takes from the inventory, and
exits with status 1 if any of them differs from the value printed in the paper.

    python scripts/reproduce_paper_numbers.py            # check + print summary
    python scripts/reproduce_paper_numbers.py --strict   # also fail on Figure 12 year-by-year differences
    python scripts/reproduce_paper_numbers.py --out results/   # also write figure tables as CSV
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

STATUSES = {"operational", "commissioning", "planned", "proposed", "retired", "failed"}
HISTORICAL = {"retired", "failed"}
PURPOSES = {"surface imaging", "sounding", "radiometry", "other"}
VALUE_TYPES = {"specified", "measured", "provider-reported", "sharpened"}
COOLING = {"cryogenic", "passive_radiative", "uncooled", ""}

# ---- Numbers printed in the manuscript -------------------------------------------------
PAPER = {
    "n_designs": 174,                 # Abstract, Overview, Highlights
    "n_deployments": 306,             # Abstract, Overview, Highlights
    "n_operational_audit": 55,        # Abstract, Section 3, Figure 12
    "operational_2024": 56,           # Figure 12 ("Inventory peak: 56")
    "fig17_first": ("MRIR", "TIROS-2", 1960, 55000.0),
    "fig17_last": ("HotSat-2", 2026, 3.5, "provider-reported"),
    # Successive records shown in Figure 17 (label, first launch year, value in m where the
    # text states it; None where the value is only read off the log-scale plot).
    "fig17_records": [
        ("MRIR", 1960, 55000.0), ("HRIR", 1964, 8500.0), ("Scanning radiometer", 1970, None),
        ("SCMR", 1973, None), ("MSS Band 8", 1978, 240.0), ("TM", 1982, 120.0),
        ("ETM+", 1999, 60.0), ("MTI", 2000, None), ("KOMPSAT-3A IIP", 2015, None),
        ("HotSat-1", 2023, 3.5),
    ],
}
# Figure 12 values read off the published plot (integer grid). Used for an informative
# year-by-year comparison only; the authoritative series is the one this script computes.
FIG12_DIGITISED = {
    1960: 1, 1961: 1, 1962: 1, 1963: 0, 1964: 2, 1965: 2, 1966: 2, 1967: 2, 1968: 2, 1969: 5,
    1970: 10, 1971: 9, 1972: 9, 1973: 11, 1974: 12, 1975: 17, 1976: 20, 1977: 20, 1978: 23,
    1979: 26, 1980: 24, 1981: 19, 1982: 20, 1983: 20, 1984: 14, 1985: 14, 1986: 16, 1987: 17,
    1988: 17, 1989: 17, 1990: 17, 1991: 21, 1992: 21, 1993: 22, 1994: 23, 1995: 23, 1996: 24,
    1997: 21, 1998: 23, 1999: 24, 2000: 26, 2001: 24, 2002: 28, 2003: 32, 2004: 34, 2005: 37,
    2006: 35, 2007: 35, 2008: 35, 2009: 35, 2010: 36, 2011: 37, 2012: 40, 2013: 40, 2014: 42,
    2015: 44, 2016: 43, 2017: 47, 2018: 51, 2019: 50, 2020: 51, 2021: 53, 2022: 54, 2023: 53,
    2024: 56, 2025: 55, 2026: 55,
}


class Report:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def check(self, label, got, want):
        ok = got == want
        print(f"  [{'OK ' if ok else 'FAIL'}] {label}: data={got!r} paper={want!r}")
        if not ok:
            self.errors.append(f"{label}: data={got!r}, paper={want!r}")
        return ok


def year_of(value) -> int | None:
    """Year from an ISO date that may be YYYY, YYYY-MM or YYYY-MM-DD."""
    if value is None or (isinstance(value, float) and pd.isna(value)) or str(value).strip() == "":
        return None
    return int(str(value)[:4])


def load():
    sensors = pd.read_csv(SENSORS_CSV, dtype=str, keep_default_na=False)
    sats = pd.read_csv(SATELLITES_CSV, dtype=str, keep_default_na=False)
    sats["tir_sensors_list"] = sats["tir_sensors"].apply(json.loads)
    sensors["native_sampling_m_num"] = pd.to_numeric(sensors["native_sampling_m"], errors="coerce")
    return sensors, sats


def validate(sensors, sats, rep: Report):
    print("Schema and rule checks")
    for col, allowed, df, name in [
        ("status_2026_08_18", STATUSES, sats, "satellites"),
        ("primary_purpose", PURPOSES, sensors, "sensors"),
        ("cooled", COOLING, sensors, "sensors"),
    ]:
        bad = df[~df[col].isin(allowed)]
        if len(bad):
            rep.errors.append(f"{name}.{col}: {len(bad)} values outside {sorted(allowed)}: "
                              f"{bad[col].unique().tolist()[:10]}")
    vt = sensors[(sensors["value_type"] != "") & ~sensors["value_type"].isin(VALUE_TYPES)]
    if len(vt):
        rep.errors.append(f"sensors.value_type: invalid values {vt['value_type'].unique().tolist()}")
    for df, key, name in [(sensors, "acronym", "sensors"), (sats, "name", "satellites")]:
        dup = df[df[key].duplicated(keep=False)][key].tolist()
        if dup:
            rep.errors.append(f"{name}: duplicate {key}: {sorted(set(dup))}")
    known = set(sensors["acronym"])
    unknown = sorted({s for lst in sats["tir_sensors_list"] for s in lst} - known)
    if unknown:
        rep.errors.append(f"satellites.tir_sensors references unknown designs: {unknown}")
    unused = sorted(known - {s for lst in sats["tir_sensors_list"] for s in lst})
    if unused:
        rep.errors.append(f"designs with no platform deployment: {unused}")
    nosrc = sats[sats["status_source"] == ""]["name"].tolist()
    if nosrc:
        rep.errors.append(f"{len(nosrc)} deployments without status_source: {nosrc[:15]}")
    nospec = sensors[sensors["spec_source"] == ""]["acronym"].tolist()
    if nospec:
        rep.warnings.append(f"{len(nospec)} designs without spec_source: {nospec}")
    # status must agree with dates at the audit date
    for r in sats.itertuples():
        start, end = year_of(r.operational_start), year_of(r.end_date)
        if r.status_2026_08_18 == "operational" and r.end_date and r.end_date <= AUDIT_DATE.isoformat():
            rep.errors.append(f"{r.name}: operational but end_date {r.end_date} is not after the audit date")
        if r.status_2026_08_18 == "retired" and not r.end_date:
            rep.errors.append(f"{r.name}: retired without end_date")
        if r.status_2026_08_18 in {"operational", "retired"} and start is None and not r.launch_date:
            rep.errors.append(f"{r.name}: {r.status_2026_08_18} without operational_start or launch_date")
        if start and end and end < start:
            rep.errors.append(f"{r.name}: end_date before operational_start")
    for e in rep.errors:
        print(f"  [FAIL] {e}")
    for w in rep.warnings:
        print(f"  [warn] {w}")
    if not rep.errors:
        print("  [OK ] all schema and rule checks passed")


def operational_by_year(sats) -> pd.Series:
    """Deployments operational on 31 December of each year (on the audit date for 2026).

    A deployment counts from the year of operational_start (launch_date if no separate
    operational start is recorded) up to, but not including, the year of end_date.
    Failed, planned and proposed deployments never count; commissioning ones count only
    from the year they were declared operational.
    """
    counts = {}
    for y in range(FIRST_YEAR, LAST_YEAR + 1):
        counts[y] = 0
    for r in sats.itertuples():
        if r.status_2026_08_18 in {"failed", "planned", "proposed", "commissioning"}:
            continue
        start = year_of(r.operational_start) or year_of(r.launch_date)
        end = year_of(r.end_date)
        for y in range(max(start, FIRST_YEAR), LAST_YEAR):
            if end is not None and y >= end:
                break
            counts[y] += 1
    counts[LAST_YEAR] = int((sats["status_2026_08_18"] == "operational").sum())
    return pd.Series(counts, name="operational_deployments")


def sampling_records(sensors, sats) -> pd.DataFrame:
    """Successive records in finest nominal native sampling, by first launch year of each design."""
    first = {}
    for r in sats.itertuples():
        if r.status_2026_08_18 in {"planned", "proposed", "failed", ""} or not r.launch_date:
            continue
        for s in r.tir_sensors_list:
            key = (r.launch_date, r.name)
            if s not in first or key < first[s]:
                first[s] = key
    rows = []
    for s in sensors.itertuples():
        if s.acronym in first and pd.notna(s.native_sampling_m_num):
            ld, plat = first[s.acronym]
            rows.append((year_of(ld), ld, s.acronym, plat, s.native_sampling_m_num, s.value_type))
    df = pd.DataFrame(rows, columns=["year", "launch_date", "design", "platform", "native_sampling_m", "value_type"])
    df = df.sort_values(["launch_date", "native_sampling_m"])
    best, out = float("inf"), []
    for r in df.itertuples():
        if r.native_sampling_m < best:
            best = r.native_sampling_m
            out.append(r._asdict())
    return pd.DataFrame(out).drop(columns="Index")


def latest_at_record(sensors, sats, value) -> tuple | None:
    """Most recently launched non-future deployment whose design samples at `value` m."""
    designs = set(sensors.loc[sensors["native_sampling_m_num"] == value, "acronym"])
    c = sats[sats["tir_sensors_list"].apply(lambda l: bool(designs & set(l)))
             & ~sats["status_2026_08_18"].isin(["planned", "proposed", "failed", ""])]
    if c.empty:
        return None
    r = c.sort_values("launch_date").iloc[-1]
    return r["name"], year_of(r["launch_date"])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="fail on any Figure 12 year that differs from the digitised plot")
    ap.add_argument("--out", type=Path, help="directory for figure tables (CSV)")
    args = ap.parse_args()

    sensors, sats = load()
    rep = Report()
    validate(sensors, sats, rep)

    print("\nTotals")
    rep.check("instrument designs", len(sensors), PAPER["n_designs"])
    rep.check("platform deployments", len(sats), PAPER["n_deployments"])
    status = sats["status_2026_08_18"].value_counts().reindex(sorted(STATUSES), fill_value=0)
    print("  status on 2026-08-18: " + ", ".join(f"{k}={v}" for k, v in status.items())
          + f" (historical={int(status[list(HISTORICAL)].sum())})")
    rep.check("operational on 2026-08-18", int(status["operational"]), PAPER["n_operational_audit"])

    print("\nFigure 12 (operational deployments per year)")
    series = operational_by_year(sats)
    rep.check("operational in 2024", int(series[2024]), PAPER["operational_2024"])
    rep.check("peak year(s)", sorted(series[series == series.max()].index.tolist()), [2024])
    diffs = {y: (int(series[y]), v) for y, v in FIG12_DIGITISED.items() if int(series[y]) != v}
    if diffs:
        msg = f"{len(diffs)} years differ from the digitised Figure 12: " + ", ".join(
            f"{y}: data={a} plot={b}" for y, (a, b) in diffs.items())
        (rep.errors if args.strict else rep.warnings).append(msg)
        print(f"  [{'FAIL' if args.strict else 'warn'}] {msg}")
    else:
        print("  [OK ] every year matches the digitised Figure 12")

    print("\nFigure 17 (successive records in finest nominal native sampling)")
    rec = sampling_records(sensors, sats)
    for r in rec.itertuples():
        print(f"  {r.year}  {r.design:<22} {r.platform:<24} {r.native_sampling_m:>9g} m  {r.value_type}")
    first = rec.iloc[0]
    rep.check("first record", (first.design, first.platform, int(first.year), float(first.native_sampling_m)),
              PAPER["fig17_first"])
    last = rec.iloc[-1]
    latest = latest_at_record(sensors, sats, last.native_sampling_m)
    rep.check("finest value, latest platform at that value, value type",
              (latest[0] if latest else None, latest[1] if latest else None,
               float(last.native_sampling_m), last.value_type), PAPER["fig17_last"])
    rep.check("record years", rec["year"].astype(int).tolist(), [y for _, y, _ in PAPER["fig17_records"]])
    stated = {y: v for _, y, v in PAPER["fig17_records"] if v is not None}
    got = {int(r.year): float(r.native_sampling_m) for r in rec.itertuples() if int(r.year) in stated}
    rep.check("record values stated in the text", got, stated)

    if args.out:
        args.out.mkdir(parents=True, exist_ok=True)
        series.rename_axis("year").to_csv(args.out / "figure12_operational_by_year.csv")
        rec.to_csv(args.out / "figure17_sampling_records.csv", index=False)
        print(f"\nWrote figure tables to {args.out}")

    print()
    if rep.errors:
        print(f"FAILED: {len(rep.errors)} check(s) disagree with the paper or the data rules:", file=sys.stderr)
        for e in rep.errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)
    print("All paper numbers reproduced.")


if __name__ == "__main__":
    main()
