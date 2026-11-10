# Changelog

## v1.2 — 2026 (audit date unchanged: 18 August 2026)

One data correction found during a final consistency check of the manuscript.

### Changed
- **INSAT-2D removed** (390 platform deployments, previously 391). ISRO lists only communications transponders for INSAT-2D and no Very High Resolution Radiometer; the VHRR entry in OSCAR/Space is an error. The record is now in `excluded_records.csv` with the source. India now has 21 deployments (previously 22); instrument–deployment links are 542 (previously 543); retired deployments are 217 (previously 218).
- Figures 12 and 17 are unchanged: INSAT-2D stopped working within four months of launch (June–October 1997), so it was never counted on 31 December of any year.
- `DATA_DICTIONARY.md`: the `failed` status now states that launch failures are included where the source catalogues document them (e.g. Nimbus-B, 1968, is not included).

## v1.1 — 2026 (audit date unchanged: 18 August 2026)

Documentation and two data corrections, made in response to peer review. Totals are unchanged: 185 instrument designs, 391 platform deployments (543 instrument–deployment links) and 83 operational deployments.

### Added
- `DATA_DICTIONARY.md`: fields, allowed values, counting units, exceptions to the design-counting rule, missing values, partial dates and the definitions of Figures 12 and 17.
- `scripts/calculate_figures.py`: checks the data rules and calculates the totals and the tables behind Figures 12 and 17.
- `results/figure12_operational_by_year.csv` and `results/figure17_sampling_records.csv`.
- `scripts/csv_to_json.py`: regenerates the JSON files from the CSVs.
- `excluded_records.csv` / `.json` (39 rows): every record removed or merged, and candidates considered but not included, with the rule and source.
- `CITATION.cff`, `LICENSE` (code), `LICENSE-DATA` (data), `requirements.txt`.

### Changed
- `status_2026_08_18` = `unresolved` for the five deployments whose status was left empty in v1.0 (FOREST-3, GOES-14, HyTI, SJ-9B, TIRSAT). Reasons are in `notes`.
- `end_date` added as an upper bound for two retired deployments with no documented end date: FOREST-1 (re-entry, 2024-08-03) and GF-5 (reported as no longer working, 2022-10).
- Figure 12 now excludes unresolved deployments in every year and uses the two upper-bound end dates. Values change for 2009–2025 only (e.g. 2024: 78 → 73); 2026 is still 83.
- Figure 17 is unchanged (13 successive records).

## v1.0 — 26 October 2026 (audit date 18 August 2026)

Audited inventory accompanying Rezaie & Hay, *The Past, Present and Possible Future of Thermal Remote Sensing* (Remote Sensing, 2026).

### How the totals changed from the pre-1.0 compilation

| | Pre-1.0 | Excluded | Merged | Added | v1.0 |
|---|--:|--:|--:|--:|--:|
| Instrument designs | 174 | −9 | −6 (+1 merged record) | +25 | **185** |
| Platform deployments | 306 | −9 | −8 | +102 | **391** |

- **Designs excluded (9):** ERBE and ERBE (NOAA) (broadband, no discrete MWIR/LWIR channel); PMR, SSU and SCR (Nimbus-4) (15 µm CO₂ channels only); TANSO-3 (VIS–SWIR only); HyTES and MASTER (airborne); SatLeo-TIR (no primary documentation).
- **Designs merged (6 → 1 new record):** TES limb and nadir → TES; VIIRS (JPSS-3) → VIIRS; Landsat-Next → LandIS; Forest-2 and OTC-P1 → SAFIRE; FOREST-GNSSP → FOREST-3 TIR imager.
- **Deployments excluded (9):** aircraft (ER-2, ER-2/DC-8), platforms without a thermal instrument or that do not exist (GOSAT-GW, SatLeo-1), superseded future missions (Landsat-11/12, GeoXO Central, GeoXO East/West).
- **Deployments merged (8):** relocation records of the same spacecraft (GOES-9, GOES-10, Meteosat-3 ×2, Meteosat-5/6/7 IODC, JPSS-3).
- **Operational on the audit date, 55 → 83:** every status was re-assigned from dated sources. 22 deployments recorded as historical were operational (e.g. ALOS-2, CBERS-4/4B, FY-3D, FY-4A, GCOM-C, KOMPSAT-3A, DMSP-F16/F17/F18); 30 recorded as operational were planned, commissioning, proposed, retired or unresolved (e.g. Sentinel-3C, TRISHNA, GOES-16, Himawari-8, Aura); constellations are counted per satellite (eight OroraTech satellites launched in 2025).

### Changed
- Rebuilt both tables against the inclusion, unit, duplicate and status rules stated in the manuscript's Review Method (documented in `DATA_DICTIONARY.md`).
- Status of every deployment fixed at 18 August 2026 in six categories (`operational`, `commissioning`, `planned`, `proposed`, `retired`, `failed`); five deployments with insufficient evidence were left empty (`unresolved` from v1.1). Each record now carries `status_source` and `status_access_date`.
- Spatial sampling redefined as the finest native MWIR/LWIR sampling at nadir (`native_sampling_m`), with product/sharpened grids in `product_sampling_m` and the nature of the value in `value_type`. Values changed for 70 previous design records.
- Each design now carries `spec_source`, `spec_access_date`, `confidence` and `primary_purpose`.
- Relocation records of the same spacecraft merged (e.g. Meteosat-7 IODC, GOES-10 S-America), with the other names kept in `alt_names`.
- Launch dates corrected (e.g. DMSP-F01–F04, HotSat-2, SkyBee-1, VanZyl-1, Clarity-1, CBERS-4B).

### Added
- 72 missing platform deployments of included designs, including TIROS-2/3/4/7, Landsat-3, MTI, BIRD, Metop-A, Meteosat-8, GOES-12/13/15, DMSP-F05–F15/F19, SkyBee-2, VanZyl-2, FireSat-1/2/3 and EDC-02–08.
- 25 designs, with 30 further platforms. 2 were needed for the figures and text of the paper: MSS (Landsat-3) and AGRI (FY-4C). 18 are documented in OSCAR/Space but were missing (e.g. VISSR (SMS/GOES), VISSR (Himawari 1-4), VHRR (NOAA), S-VISSR (FY-2A/B, FY-2C/D/E), CZCS, COCTS2, EOIR, GIIRS-3). 5 were found by targeted search (LisR, HyperScout-2 TIR, ERNST MWIR, TIRSAT sensor, HyTI).
- `calibrated_data` field: uncalibrated demonstrations (Clarity-1) are kept but cannot set a sampling record.

### Removed
- Airborne records (ER-2/DC-8: HyTES, MASTER), instruments without an MWIR/LWIR channel (ERBE, PMR, SSU, SCR (Nimbus-4), TANSO-3/GOSAT-GW), an undocumented record (SatLeo-1) and superseded future missions (Landsat-11/12, GeoXO Central): listed in `excluded_records.csv` from v1.1.
- Unsourced columns (`altitude_km`, `inclination_deg`, `period_min`, `mass_kg`, `all_sensors`, `instrument_type`, `scanning_technique`, `usage_from`, `usage_to`, `data_quality`, `short_description`, `background`).


## Pre-1.0 (to 27 June 2026)
Initial compilation: 174 sensor records and 306 satellite records, largely from WMO OSCAR/Space. It is superseded by v1.0.
