# Changelog

## v1.0 — unreleased (audit date 18 August 2026)

Dataset version prepared to accompany Rezaie & Hay, *The Past, Present and Possible Future of Thermal Remote Sensing* (Remote Sensing, 2026).

**Status: not released.** The audited totals (162 designs, 361 deployments, 80 operational) do not reproduce the numbers printed in the manuscript (174, 306, 55). See `VALIDATION_REPORT.md`. The release tag will be created only after the authors reconcile the manuscript and the data.

### Changed
- Rebuilt both tables against the inclusion, unit, duplicate and status rules stated in the manuscript's Review Method (documented in `DATA_DICTIONARY.md`).
- Status of every deployment fixed at 18 August 2026 in six categories (`operational`, `commissioning`, `planned`, `proposed`, `retired`, `failed`); the `unknown` and `historical` values are gone. Each record now carries `status_source` and `status_access_date`.
- Spatial sampling redefined as the finest native MWIR/LWIR sampling at nadir (`native_sampling_m`), with product/sharpened grids in `product_sampling_m` and the nature of the value in `value_type`. Values changed for 70 previous design records.
- Each design now carries `spec_source`, `spec_access_date`, `confidence` and `primary_purpose`.
- Relocation records of the same spacecraft merged (e.g. Meteosat-7 IODC, GOES-10 S-America), with the other names kept in `alt_names`.
- Launch dates corrected (e.g. DMSP-F01–F04, HotSat-2, SkyBee-1, VanZyl-1, Clarity-1, CBERS-4B).
- JSON files are now generated from the CSVs (`scripts/csv_to_json.py`).

### Added
- 72 missing platform deployments of included designs, including TIROS-2/3/4/7, Landsat-3, MTI, BIRD, Metop-A, Meteosat-8, GOES-12/13/15, DMSP-F05–F15/F19, SkyBee-2, VanZyl-2, FireSat-1/2/3 and EDC-02–08.
- Designs MSS (Landsat-3) and AGRI (FY-4C).
- `excluded_records.csv` (33 rows): every record removed or merged, with the rule and source.
- `DATA_DICTIONARY.md`, `VALIDATION_REPORT.md`, `CITATION.cff`, `LICENSE` (CC BY 4.0 data, MIT code), `LICENSE-DATA`.
- `scripts/reproduce_paper_numbers.py`: recomputes every inventory number in the manuscript and exits non-zero on any difference.

### Removed
- Airborne records (ER-2/DC-8: HyTES, MASTER), instruments without an MWIR/LWIR channel (ERBE, PMR, SSU, SCR (Nimbus-4), TANSO-3/GOSAT-GW), an undocumented record (SatLeo-1) and superseded future missions (Landsat-11/12, GeoXO Central): all listed in `excluded_records.csv`.
- Unsourced columns (`altitude_km`, `inclination_deg`, `period_min`, `mass_kg`, `all_sensors`, `instrument_type`, `scanning_technique`, `usage_from`, `usage_to`, `data_quality`, `short_description`, `background`).

## Pre-1.0 (to 27 June 2026)
Initial compilation: 174 sensor records and 306 satellite records, largely from WMO OSCAR/Space. It is superseded by v1.0.
