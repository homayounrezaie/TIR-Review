# Validation report — dataset v1.0 audit

**Audit date (status reference):** 18 August 2026 **Sources accessed:** 26 October 2026
**Inputs:** previous repository data (`master`, 27 June 2026); manuscript *The Past, Present and Possible Future of Thermal Remote Sensing* (revision v7); WMO OSCAR/Space (full catalogue of 1,062 satellites and 1,250 instruments, downloaded 26 Oct 2026); agency, operator and peer-reviewed sources cited per record.

Run `python scripts/reproduce_paper_numbers.py` to regenerate every number below.

---

## 1. Are the paper's numbers reproduced?

| Quantity | Manuscript v7 | Audited data | Reproduced |
|---|---:|---:|:---:|
| Instrument designs | 174 | **185** | no |
| Platform deployments | 306 | **391** | no |
| Operational on 18 Aug 2026 | 55 | **83** | no |
| Operational in 2024 (Figure 12) | 56 (peak) | **78** | no |
| Peak year of Figure 12 | 2024 | **2026** (83) | no |
| First record, Figure 17 | MRIR / TIROS-2 / 1960 / 55 km | MRIR / TIROS-2 / 1960 / 55 km | **yes** |
| Finest record, Figure 17 | HotSat-2, 2026, 3.5 m, provider-reported | HotSat-2, 2026, 3.5 m, provider-reported | **yes** |
| Intermediate Figure 17 steps | 10 steps | 13 steps | no (§6) |

Status on 18 Aug 2026: operational 83, commissioning 19, planned 50, proposed 9, retired 218, failed 7 (historical 225), **unresolved 5** (§8).

These numbers come from applying the rules in the manuscript's Review Method, plus four decisions taken by the authors on 26 Oct 2026:

1. Add instrument designs that are documented in OSCAR/Space but were missing from the inventory.
2. Uncalibrated demonstrations cannot set a sampling record (Figure 17).
3. In-orbit stand-by spacecraft count as not operational.
4. One record per satellite in constellations.

**The data were not adjusted to reach the published numbers.** Following the instruction to stop when the totals differ, no pull request, merge or release has been made. The manuscript must be updated to the audited numbers (§11) before v1.0 is released.

---

## 2. Design count (174 → 185)

| Change | n | Records |
|---|--:|---|
| Previous records | 174 | |
| **Excluded** | −9 | ERBE, ERBE (NOAA) (broadband, no discrete MWIR/LWIR channel); PMR, SSU, SCR (Nimbus-4) (15 µm CO₂ channels only); TANSO-3 (VIS–SWIR only); HyTES, MASTER (airborne); SatLeo-TIR (no primary documentation) |
| **Merged duplicates** | −6 | TES-limb + TES-nadir → TES; VIIRS (JPSS-3) → VIIRS; Landsat-Next → LandIS; Forest-2 + OTC-P1 → SAFIRE (one OroraTech design); FOREST-GNSSP → FOREST-3 TIR imager |
| Merged record created | +1 | SAFIRE |
| **Added** | +25 | *Required by the paper's figures/text:* MSS (Landsat-3) (Figure 17), AGRI (FY-4C) (changed channel set). *Documented in OSCAR but missing:* VISSR (SMS/GOES), VISSR (Himawari 1-4), VHRR (NOAA), S-VISSR (FY-2A/B), S-VISSR (FY-2C/D/E), CZCS, MSU-V, SME (IR), IRS (SJ-9), MIRIS/MEOC, COCTS2, EOIR, GIIRS-3, GKMI, IMAGER (INSAT-4), PLATiNO TIR, FEI, TICFIRE. *Found by targeted search:* LisR (constellr ISS demonstrator, shown in Figure 16), HyperScout-2 TIR (PhiSat-1), ERNST MWIR, TIRSAT sensor, HyTI |
| **Total** | **185** | |

Renamed records keep their previous name in `alt_names`, e.g. IMAGER-1/2 (GEOS) → IMAGER (GOES-8/11), IMAGER (GOES-12/15); TIR → TIS (SDGSAT-1); HYDROSAT → LIRI; SBG-TIR → EAGLE-TIR radiometer; EarthDaily → EDC TIR; VISSR → VISSR (GMS-5).

## 3. Deployment count (306 → 391)

| Change | n | Records |
|---|--:|---|
| Previous records | 306 | |
| **Excluded** | −9 | ER-2 / DC-8 and ER-2 aircraft; GOSAT-GW (no TIR instrument); SatLeo-1 (no such satellite); Landsat-11, Landsat-12 (Landsat Next became one observatory, Landsat 10); GeoXO Central (dropped in April 2026); GeoXO East/West (replaced by OSCAR GeoXO 1–4) |
| **Merged duplicates** | −8 | GOES-9 (GMS backup), GOES-10 (S-America), Meteosat-3 (ADC), Meteosat-3 (X-ADC), Meteosat-5/6/7 (IODC), JPSS-3 (NOAA-22) |
| **Added** | +102 | *Missing deployments of included designs (72):* TIROS-2, -3, -4, -7; Landsat-3; MTI; BIRD; Metop-A; Meteosat-8; GOES-12, -13, -15; DMSP-F05–F15, F19; Meteor-M N1, N2, N2-1, N2-7, N2-8; Okean-O1-1 to -7, Okean-O-1, SICH-1; Resurs-O1-1 to -4, Meteor-P5; CBERS-1, -3; HY-1A, -1B; FY-2F; FY-4F; SAC-D; Megha-Tropiques; EOS-03 (GISAT-1); Arctica-M N5–N8; GeoXO 1–4; SkyBee-2; VanZyl-2; FireSat-1/2/3; EDC-02 to -08. *Platforms of the 25 added designs (30):* SMS-1, -2, GOES-1, -2, -3; GMS-1 to -4; FY-2A to -2E; SME; SJ-9B; STSat-3; HY-3A (HY-1E), HY-1F, HY-3B; EOS-08; GEO-KOMPSAT-5; INSAT-4; PLATiNO-2; AOS-Sky; ISS LisR; PhiSat-1; ERNST; TIRSAT; HyTI. (NOAA-2–5, Nimbus-7, Okean-O-1, FY-4C/D/F and FORUM were already present.) |
| **Total** | **391** | |

## 4. Operational count (55 → 83)

The 83 deployments operational on 18 Aug 2026:

ALOS-2, Aqua, Arctica-M N1, Arctica-M N2, CBERS-4, CBERS-4B, DMSP-F16, DMSP-F17, DMSP-F18, EarthCARE, Electro-L N2, Electro-L N3, Electro-L N4, EOS-08, ERNST, FireSat Protoflight, FOREST-2, FOREST-4P to FOREST-11P (8), FY-2G, FY-2H, FY-3D, FY-3E, FY-3F, FY-3G, FY-3H, FY-4A, FY-4B, GCOM-C, GEO-KOMPSAT-2A, GF-13, GF-13-02, GF-4, GF-5-01A, GF-5-02, GOES-15 (EWS-G2), GOES-18, GOES-19, GOSAT, GOSAT-2, HJ-2A, HJ-2B, HotSat-2, HY-1C, HY-1D, HY-3A (HY-1E), Himawari-9, INSAT-3DR, INSAT-3DS, ISS ECOSTRESS, KANOPUS-V-IK-1, KOMPSAT-3A, Landsat-8, Landsat-9, Meteor-M N2-3, Meteor-M N2-4, Meteosat-9 (IODC), Meteosat-10, Meteosat-11, Meteosat-12, Metop-B, Metop-C, NOAA-20, NOAA-21, PREFIRE-1, PREFIRE-2, SCISAT-1, SDGSAT-1, Sentinel-3A, Sentinel-3B, SkyBee-1, SkyBee-2, SNPP, Terra, TIMED, VanZyl-1, VanZyl-2.

The previous repository had 22 operational deployments marked historical (e.g. ALOS-2, CBERS-4/4B, FY-3D, FY-4A, GCOM-C, GOSAT, KOMPSAT-3A, DMSP-F16/F17/F18, SCISAT-1, TIMED). It also had 30 deployments marked operational that were planned, commissioning, proposed, retired or unresolved on the audit date (e.g. Sentinel-3C, TRISHNA, HotSat-3, MTG-S1, Metop-SG-A1, FY-4C, GOES-16, Himawari-8, Aura, Clarity-1). No rule reproduces 55.

Judgement calls affecting the count, each recorded in `notes`:

- **In-orbit stand-by** (GOES-16, GOES-17, Himawari-8): `retired` from the end of operational service, because they were not delivering data.
- **Multi-instrument platforms** are operational while any included instrument delivers data: Terra (ASTER off since 2022), Metop-B (HIRS/4 off), SNPP (CrIS off since Dec 2025), FY-4B (AGRI failed 30 Jul 2026). Aura (HIRDLS and TES ended) is retired.
- **Constellations**: one record per satellite (OroraTech OTC-P1 = 8 operational; EarthDaily = 8 commissioning).
- **DMSP-F16**: OSCAR says "Inactive", but NOAA/NCEI list F16 OLS data as current, with the mission extended to Sept 2026. Recorded as operational.
- **Weakly evidenced operational records** (stale OSCAR entries, or no 2026 statement): GF-13, GF-13-02, GF-5-01A, GF-5-02, INSAT-3DR, EOS-08, ERNST.

## 5. Figure 12 (annual operational deployments)

The convention used here: a deployment counts if it was operational on 31 December of the year; for 2026, on the audit date.

| Decade | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1960s | 1 | 1 | 0 | 1 | 1 | 1 | 2 | 1 | 1 | 2 |
| 1970s | 5 | 4 | 2 | 4 | 8 | 12 | 13 | 17 | 18 | 16 |
| 1980s | 16 | 18 | 16 | 18 | 22 | 21 | 23 | 24 | 27 | 25 |
| 1990s | 27 | 31 | 31 | 26 | 28 | 32 | 29 | 28 | 31 | 34 |
| 2000s | 34 | 32 | 38 | 39 | 37 | 39 | 39 | 38 | 37 | 40 |
| 2010s | 45 | 45 | 48 | 51 | 53 | 49 | 49 | 51 | 57 | 63 |
| 2020s | 65 | 67 | 64 | 71 | 78 | 79 | 83 | | | |

`--out results/` writes this series as CSV for redrawing Figure 12. The published curve cannot be reproduced; the manuscript does not state its counting convention.

## 6. Figure 17 (successive records in native sampling)

| Year | Design | First platform | Value | vs manuscript |
|---|---|---|---:|---|
| 1960 | MRIR | TIROS-2 | 55 km | same |
| 1964 | HRIR | Nimbus-1 | 8.5 km | same |
| 1970 | SR | ITOS-1 | **7.2 km** | Manuscript plots ~3.6 km, which is the SR *visible* channel (OSCAR: 7.2 km IR) |
| 1970 | THIR | Nimbus-4 | **7.0 km** | new step |
| 1972 | VHRR (NOAA) | NOAA-2 (Oct 1972) | **900 m** | new step (design added) |
| 1972 | SCMR | Nimbus-5 (Dec 1972) | 660 m | Manuscript plots **1973** |
| 1976 | OLS | DMSP-F01 (Block 5D-1) | **560 m** | new step (thermal channel, fine mode) |
| 1978 | MSS Band 8 | Landsat-3 | 240 m | same |
| 1982 | TM | Landsat-4 | 120 m | same |
| 1999 | ETM+ | Landsat-7 | 60 m | same |
| 2000 | MTI | MTI | 20 m | same |
| 2015 | IIP | KOMPSAT-3A | 5.5 m | same |
| 2023 | HotSat Imager | HotSat-1 | 3.5 m (provider) | same; HotSat-2 (2026) repeats it |

Clarity-1 (Albedo, 2025) is specified at 2.0 m LWIR GSD. It is excluded from the records under the authors' rule, because Albedo states its thermal imagery was uncalibrated (`calibrated_data = no`). The rule must be stated in the manuscript (§11).

## 7. Values that changed, and why

- **Spatial sampling:** values changed for 70 of the 174 previous design records. The old `spatial_resolution_m` often held a visible or product value instead of the native MWIR/LWIR value at nadir. Examples:

  | Design | Old | New |
  |---|---:|---:|
  | TM | 30 m | 120 m |
  | ETM+ | 30 m | 60 m |
  | ETM | 30 m | 120 m |
  | MODIS | 250 m | 1000 m |
  | SLSTR | 500 m | 1000 m |
  | AHI | 500 m | 2000 m |
  | GHI | 250 m | 2000 m |
  | SR | 3600 m | 7200 m |
  | VHRR (ATS) | 5500 m | 11000 m |
  | STR | 1250 m | 6250 m |
  | VAS | 900 m | 6900 m |
  | VISSR (GMS-5) | 1250 m | 5000 m |
  | VTIR | 900 m | 2700 m |
  | MI | 1000 m | 4000 m |
  | IRMSS | 80 m | 160 m |
  | MTI | 500 m | 20 m |
  | VIMS | 2000 m | 40 m |
  | PREFIRE | 3400 m | 11800 m |
  | EarthDaily | 5 m | 120 m |
  | LSTM | 50 m | 37 m native (50 m product) |
  | TRISHNA | 50 m | 57 m native (60 m product) |

  Limb and occultation sounders now have no nadir value, by definition.
- **Status:** every deployment was re-assigned from dated sources. Transitions from the previous file: 132 unknown → retired, 22 historical → operational, 12 operational → planned, 9 operational → commissioning, 5 operational → retired, 2 operational → proposed, 2 operational → unresolved, and others.
- **Launch dates corrected** where the old value was a placeholder or wrong. Examples:
  - DMSP-F01–F04: 1970–72 → 1976–79
  - HotSat-2: 2025-01-01 → 2026-03-30
  - SkyBee-1: 2023 → 2025-01-14
  - VanZyl-1: 2022 → 2024-08-16
  - Clarity-1: 2024 → 2025-03-15
  - CBERS-4B: 2021 → 2019-12-20
  - ATS-6: OSCAR error → 1974-05-30, from NSSDCA
- **Items in the task brief:** TIROS-2 added; HotSat-3 → `proposed`; TRISHNA → `planned`; VanZyl-2 added.
- **Removed columns:** columns that had no sources (altitude, inclination, period, mass, all_sensors, scanning technique and similar). Swath, revisit and cooling are filled only where the specification source states them.

## 8. Sources and unresolved records

- **Every design has a `spec_source` and every deployment a `status_source`**, each with an access date. 314 of 391 status sources are WMO OSCAR/Space record pages only. Historical OSCAR dates were not independently checked except where noted; one OSCAR error was found and corrected (ATS-6 launch date).
- **Status unresolved (5)**, left empty with the reason in `notes`:
  - FOREST-3: no source on data delivery.
  - GOES-14: transferred to the US Space Force in late 2025; activity unknown.
  - SJ-9B: OSCAR "Unclear"; no end-of-mission source.
  - TIRSAT: no post-launch status source.
  - HyTI: re-entered Dec 2024, but whether it ever returned data, i.e. retired or failed, is not documented.
- **End date unresolved (2):** FOREST-1 and GF-5.
- **No native sampling (20):** 14 limb/occultation sounders, plus FOREST-1 and FOREST-3 imagers, ERNST MWIR, TIRSAT sensor, GXS and MSU-MR-MP. In each case the value is unpublished or not applicable.
- **Low-confidence specifications:** 18; see the `confidence` column.
- **Source conflicts recorded in `notes`:**
  - BIROS end date: Dec 2020 vs re-entry Jan 2026.
  - MTI end date: 2015, unsupported by narrative.
  - TET-1: DLR vs eoPortal.
  - TRISHNA launch: 2027 vs ≥2028.
  - LSTM launch: 2028 vs ≥2029.
  - Landsat-4 TM end: 1987 vs 1993.
  - STSat-3 end: 2015 vs 2021.
  - EarthDaily TIR band count.
  - COCTS2 second LWIR centre: 10.8 vs 11.0 µm.
- **Candidates considered and not included** (listed in `excluded_records.csv`):
  - CO sensor (ASCENDS concept).
  - SACFF (no documented MWIR/LWIR channel).
  - Aistech, Jilin-1 Hongwai and Satellogic thermal modes (no primary design source).
  - OroraTech SAFIRE Gen4 on Kepler satellites (hosts unidentified).

## 9. Coverage

All 1,250 OSCAR/Space instrument pages were swept for MWIR/LWIR channels, and the qualifying designs were added (§2). New-space and commercial instruments were searched separately (§2, §8). Those searches cover English-language sources up to the audit date. Chinese and other commercial operators without English documentation may still be under-represented, consistent with the manuscript's stated scope.

## 10. Other disagreements between the data and the manuscript

1. **Figure 16, LisR:** the "HiVE demonstrator (ISS), 30 m" entry. The instrument is LisR, and its sources give **~80 m** GSD and a 26 km swath (Bierdel et al., 4S 2022; Fraunhofer 2023).
2. **Figure 16, FOREST-1:** shown as "mid-wave plus 2 long-wave channels, 200 m". The sources give two thermal channels (MWIR and LWIR) and no published GSD.
3. **Section 2.1 / Figure 13, MRIR:** OSCAR's MRIR channel set differs from the TIROS-2 set in the paper. Channel sets varied by mission, so the paper's new-design rule implies separate designs; one design is kept here, with a note.
4. **Section 2.2:** says Landsat-3 Band 8 "failed shortly after launch" (NASA/USGS mission pages). USGS OFR 83-123 says it "became inoperative in early 1979" after more than 370 thermal images.
5. **Table 3:** gives EAGLE-TIR sampling as "Not stated". CEOS EO Handbook gives 60 m at nadir (undated) and the 2023 SBG-TIR design gives ≤60 m.
6. **Data Availability Statement:** says "archived". GitHub is not an archive; a Zenodo DOI for the release would make this true.

## 11. Manuscript changes needed before release

| Location | Current text | Change to |
|---|---|---|
| Highlights, Abstract, Overview | 174 designs, 306 deployments, 55 operational | **185**, **391**, **83** |
| Section 3, first paragraph | "The audit identified 55 operational platform deployments." | **83** |
| Figure 12 | "Inventory peak: 56"; 55 in 2026 | Redraw from `figure12_operational_by_year.csv`: peak **83 in 2026**, **78 in 2024**; state the counting convention in the caption |
| Figure 17 | 10 steps; Scanning radiometer ~3.6 km; SCMR at 1973 | 13 steps (§6): SR 7.2 km; add THIR (1970), VHRR NOAA (1972), OLS (1976); SCMR at 1972 |
| Figure 16 | HiVE demonstrator (ISS) 30 m; FOREST-1 3 channels, 200 m | LisR (ISS) ~80 m; FOREST-1 MWIR + LWIR, sampling not reported |
| Review Method, status | six categories | Add: "Spacecraft in on-orbit storage or stand-by and not delivering data on the audit date were classed as retired from the end of their operational service." |
| Review Method, sampling | finest nominal native sampling | Add: "Demonstrations whose operators report uncalibrated thermal data were retained but not used as sampling records." |
| Review Method, sources | OSCAR, ITC, CEOS | State that statuses were verified against OSCAR/Space and agency/operator sources accessed on 26 Oct 2026 for conditions on 18 Aug 2026 |
| Section 2.2 | Landsat-3 Band 8 "failed shortly after launch" | e.g. "operated intermittently until early 1979" (USGS OFR 83-123) |
| Data Availability | "archived ... at GitHub" | GitHub release v1.0 plus Zenodo DOI |

## 12. Repository files not used by the paper

`figures/fig1–3*.png` were generated from pre-audit data for an earlier notes file. They do not appear in the manuscript and do not reflect v1.0.
