# Validation report — dataset v1.0 audit

**Audit date (status reference):** 18 August 2026 **Sources accessed:** 26 October 2026
**Inputs:** previous repository data (`master`, 27 June 2026), manuscript *The Past, Present and Possible Future of Thermal Remote Sensing* (revision v7), WMO OSCAR/Space (full satellite and instrument catalogue, 1,062 satellites and 1,250 instruments, downloaded 26 Oct 2026), agency/operator documentation and peer-reviewed sources cited per record.

Run `python scripts/reproduce_paper_numbers.py` to regenerate every number below.

---

## 1. Are the paper's totals reproduced? **No.**

Applying the inclusion, unit, duplicate and status rules stated in the paper's Review Method to the audited records gives:

| Quantity | Paper | This audit | Reproduced |
|---|---:|---:|:---:|
| Instrument designs | 174 | **162** | no |
| Platform deployments | 306 | **361** | no |
| Operational on 18 Aug 2026 | 55 | **80** | no |
| Operational in 2024 (Figure 12) | 56 (peak) | **74** | no |
| Peak year of Figure 12 | 2024 | **2026** | no |
| First record in Figure 17 | MRIR / TIROS-2 / 1960 / 55 km | MRIR / TIROS-2 / 1960 / 55 km | **yes** |
| Finest record in Figure 17 | HotSat-2, 2026, 3.5 m (provider-reported) | **Clarity-1, 2025, 2.0 m (provider-reported)**; HotSat-2 repeats 3.5 m | no |

Status on 18 Aug 2026: operational 80, commissioning 19, planned 46, proposed 7, retired 200, failed 7 (historical 207), unresolved 2.

Following the instruction "if the totals do not match, stop and report", **no pull request, merge or release has been made.** The data were not adjusted to reach the published numbers. The sections below identify the records responsible.

---

## 2. Why the design count differs (174 → 162)

| Change | Records |
|---|---|
| **Excluded (9)**, see `excluded_records.csv` | ERBE, ERBE (NOAA) (broadband radiometers, no discrete MWIR/LWIR channel); PMR, SSU, SCR (Nimbus-4) (15 µm CO₂ channels only); TANSO-3 (VIS/NIR/SWIR only); HyTES, MASTER (airborne); SatLeo-TIR (no primary documentation) |
| **Merged duplicates (6)** | TES-limb + TES-nadir → TES; VIIRS (JPSS-3) → VIIRS; Landsat-Next → LandIS; Forest-2 + OTC-P1 → SAFIRE (one OroraTech design); FOREST-GNSSP → FOREST-3 TIR imager ("GNSSP" is the Greek National Small Satellite Programme, not an instrument) |
| **Added (2)** | MSS (Landsat-3): Figure 17 uses its thermal Band 8, which the previous repository did not contain. AGRI (FY-4C): its thermal channel set differs from the FY-4A/B AGRI (OSCAR records it separately), so the paper's new-design rule applies. |
| **Renamed (alt names kept)** | e.g. IMAGER-1/2 (GEOS) → IMAGER (GOES-8/11), IMAGER (GOES-12/15); TIR → TIS (SDGSAT-1); HYDROSAT → LIRI; IR spectrometer → CLARREO IR spectrometer; SBG-TIR → EAGLE-TIR radiometer; EarthDaily → EDC TIR; Clarity → Clarity LWIR; SuperSharp → HIBISCUS |

## 3. Why the deployment count differs (306 → 361)

| Change | Records |
|---|---|
| **Excluded (9)** | ER-2 / DC-8 and ER-2 aircraft (not satellites); GOSAT-GW (no TIR instrument); SatLeo-1 (no such satellite; hosted payload launched after the audit date, news sources only); Landsat-11, Landsat-12 (Landsat Next re-architected as one observatory, Landsat 10); GeoXO Central (dropped in the April 2026 plan); GeoXO East/West (replaced by the OSCAR GeoXO 1–4 records) |
| **Merged duplicates (8)** | GOES-9 (GMS backup), GOES-10 (S-America), Meteosat-3 (ADC), Meteosat-3 (X-ADC), Meteosat-5/6/7 (IODC) (relocations of the same spacecraft); JPSS-3 (NOAA-22) (duplicate of JPSS-3) |
| **Added (72)**: deployments of included designs that were missing | **TIROS-2, -3, -4, -7** (MRIR; TIROS-2 is cited throughout the paper); Landsat-3 (MSS Band 8); MTI; BIRD (HSRS); Metop-A; Meteosat-8; GOES-12, -13 (EWS-G1), -15 (EWS-G2); DMSP-F05 to F15 and F19 (OLS); Meteor-M N1, N2, N2-1, N2-7, N2-8; Okean-O1-1 to -7, Okean-O-1, SICH-1; Resurs-O1-1 to -4, Meteor-P5 (MSU-SK family); CBERS-1, CBERS-3; HY-1A, HY-1B; FY-2F; FY-4F; SAC-D (NIRST); Megha-Tropiques (ScaRaB); EOS-03/GISAT-1 (failed); Arctica-M N5–N8; GeoXO 1–4; **SkyBee-2, VanZyl-2**; FireSat-1/2/3; EDC-02 to EDC-08 (one record per EarthDaily satellite) |

Totals: 306 − 9 − 8 + 72 = **361**.

## 4. Why the operational count differs (55 → 80)

The 80 deployments operational on 18 Aug 2026:

ALOS-2, Aqua, Arctica-M N1, Arctica-M N2, CBERS-4, CBERS-4B, DMSP-F16, DMSP-F17, DMSP-F18, EarthCARE, Electro-L N2, Electro-L N3, Electro-L N4, FireSat Protoflight, FOREST-2, FOREST-4P to FOREST-11P (8), FY-2G, FY-2H, FY-3D, FY-3E, FY-3F, FY-3G, FY-3H, FY-4A, FY-4B, GCOM-C, GEO-KOMPSAT-2A, GF-13, GF-13-02, GF-4, GF-5-01A, GF-5-02, GOES-15 (EWS-G2), GOES-18, GOES-19, GOSAT, GOSAT-2, HJ-2A, HJ-2B, HotSat-2, HY-1C, HY-1D, Himawari-9, INSAT-3DR, INSAT-3DS, ISS ECOSTRESS, KANOPUS-V-IK-1, KOMPSAT-3A, Landsat-8, Landsat-9, Meteor-M N2-3, Meteor-M N2-4, Meteosat-9 (IODC), Meteosat-10, Meteosat-11, Meteosat-12, Metop-B, Metop-C, NOAA-20, NOAA-21, PREFIRE-1, PREFIRE-2, SCISAT-1, SDGSAT-1, Sentinel-3A, Sentinel-3B, SkyBee-1, SkyBee-2, SNPP, Terra, TIMED, VanZyl-1, VanZyl-2.

The previous repository marked 88 records operational, of which **22 were wrongly marked historical** (e.g. ALOS-2, CBERS-4/4B, FY-3D, FY-4A, GCOM-C, GOSAT, KOMPSAT-3A, DMSP-F16/F17/F18, SCISAT-1, TIMED) and **30 were wrongly marked operational**, being planned, commissioning, proposed or retired on the audit date (e.g. Sentinel-3C, TRISHNA, HotSat-3, MTG-S1, Metop-SG-A1, FY-4C, Electro-L N5, GOES-16, Himawari-8, Aura, Clarity-1, FOREST-1, FOREST-16 to -19). I could not reconstruct a rule that yields 55.

Judgement calls that move the operational count (each recorded in `notes`):

- **In-orbit stand-by/storage counted as not operational** (GOES-16, GOES-17, Himawari-8): recorded as `retired` from the end of operational service, because the six-category scheme has no stand-by value. GOES-14 is unresolved (see §8).
- **Multi-instrument platforms** count as operational while any included instrument delivers data. Terra (ASTER off since Sept 2022), Metop-B (HIRS/4 off since 2023), SNPP (CrIS off since Dec 2025) and FY-4B (AGRI failed 30 Jul 2026) stay operational. Aura (HIRDLS and TES both ended) is retired.
- **OroraTech OTC-P1** contributes 8 operational deployments (one per satellite, per the paper's unit rule).
- **DMSP-F16**: OSCAR says "Inactive", but NOAA/NCEI list F16 OLS data to "Present", with the DMSP mission extended to September 2026. Recorded as operational (medium confidence).
- **Stale OSCAR records** (last updated before 2024) back five operational records: GF-13, GF-13-02, GF-5-01A, GF-5-02 and INSAT-3DR. No contrary evidence was found.

## 5. Figure 12 (annual operational deployments)

Computed series (deployments operational on 31 December of each year; 2026 = audit date):

| Decade | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1960s | 1 | 1 | 0 | 1 | 1 | 1 | 2 | 1 | 1 | 2 |
| 1970s | 5 | 4 | 2 | 4 | 7 | 10 | 10 | 12 | 12 | 10 |
| 1980s | 10 | 11 | 10 | 12 | 15 | 15 | 17 | 19 | 23 | 21 |
| 1990s | 23 | 27 | 27 | 24 | 26 | 31 | 28 | 26 | 30 | 33 |
| 2000s | 33 | 31 | 37 | 38 | 37 | 38 | 38 | 36 | 35 | 38 |
| 2010s | 43 | 43 | 46 | 48 | 49 | 47 | 47 | 49 | 56 | 62 |
| 2020s | 63 | 66 | 63 | 69 | 74 | 74 | 80 | | | |

63 of 67 years differ from the published curve. The 1960s–1970s are lower because the published curve appears to count Meteor-1/-2 and similar short-lived satellites differently, and the paper does not state its counting convention. Post-1984 values are higher because of the added deployments (§3) and corrected statuses (§4). **The paper should state its convention** (e.g. "operational on 31 December" or "operational at any time during the year"); the data dictionary documents the one used here.

## 6. Figure 17 (successive records in native sampling)

Applying the paper's rule (finest MWIR/LWIR native sampling at nadir; first launched deployment that delivered data):

| Year | Design | Platform | Value | Paper |
|---|---|---|---:|---|
| 1960 | MRIR | TIROS-2 | 55 km | ✔ |
| 1964 | HRIR | Nimbus-1 | 8.5 km | ✔ |
| 1970 | SR | ITOS-1 | **7.2 km** | Paper plots ~3.6 km, which is the SR *visible* channel; OSCAR gives 7.2 km for IR |
| 1970 | THIR | Nimbus-4 | **7.0 km** | not in paper |
| 1972 | SCMR | Nimbus-5 | 660 m | Paper plots **1973**; Nimbus-5 launched Dec 1972 |
| 1976 | OLS | DMSP-F01 (Block 5D-1) | **560 m** (fine mode, thermal channel) | not in paper; the old repository misdated DMSP-F01–F04 to 1970–72 |
| 1978 | MSS Band 8 | Landsat-3 | 240 m | ✔ |
| 1982 | TM | Landsat-4 | 120 m | ✔ |
| 1999 | ETM+ | Landsat-7 | 60 m | ✔ |
| 2000 | MTI | MTI | 20 m | ✔ |
| 2015 | IIP | KOMPSAT-3A | 5.5 m | ✔ |
| 2023 | HotSat Imager | HotSat-1 | 3.5 m (provider) | ✔ |
| 2025 | Clarity LWIR | Clarity-1 | **2.0 m (provider specification)** | **not in paper** |

**Clarity-1** (Albedo Space, launched 15 Mar 2025 UTC) carries an uncooled LWIR imager specified at 2.0 m GSD (at 275 km, nadir). Albedo reports that it returned thermal imagery, though uncalibrated, before contact was lost about nine months after launch. If counted, it replaces HotSat-2 as the finest record and changes the Highlights and Abstract ("55 km … to 3.5 m"). The authors must decide whether it qualifies (e.g. by excluding uncalibrated or unvalidated demonstrations), or record it as `failed`. It is recorded here as `retired`, with the judgement noted.

A further candidate, NOAA-2's VHRR (0.9 km, Oct 1972, see §9), would also enter the sequence if added.

## 7. Records whose values changed, and why

All value changes follow from the paper's own rules or from sources, and are documented in each record's `notes`. Main classes:

- **Spatial sampling: values changed for 70 of the 174 previous design records.** The previous `spatial_resolution_m` often held the visible/reflective-band value, or a product value, instead of the MWIR/LWIR native value required by the paper. Examples: TM 30 → 120 m; ETM+ 30 → 60 m; ETM 30 → 120 m; MODIS 250 → 1000 m; SLSTR 500 → 1000 m; AHI 500 → 2000 m; GHI 250 → 2000 m; SR 3600 → 7200 m; VHRR (ATS) 5500 → 11000 m; STR 1250 → 6250 m; VAS 900 → 6900 m; VISSR (GMS-5) 1250 → 5000 m; VTIR 900 → 2700 m; MI 1000 → 4000 m; IRMSS 80 → 160 m; MTI 500 → 20 m; VIMS 2000 → 40 m; PREFIRE 3400 → 11800 m; EarthDaily 5 → 120 m; LSTM 50 → 37 m native (50 m product); TRISHNA 50 → 57 m native (60 m product). Limb/occultation sounders (ACE-FTS, AIUS, CLAES, HALOE, HIRDLS, ILAS-I/II, ISAMS, LIMS, LRIR, MIPAS, SABER, SAMS) now have no nadir value, because they have no nadir sampling.
- **Status: every deployment re-assigned** from dated sources. Transitions: 132 unknown → retired; 22 historical → operational; 12 operational → planned; 9 operational → commissioning; 5 operational → retired; 2 operational → proposed; 4 unknown → proposed; 1 unknown → failed; 1 unknown → operational; 1 planned → proposed; 2 operational → unresolved.
- **Launch dates corrected** where the old record was a placeholder (`YYYY-01-01`) or wrong. Examples: DMSP-F01–F04 (1970–72 → 1976–79), HotSat-2 (2025-01-01 → 2026-03-30), SkyBee-1 (2023 → 2025-01-14), VanZyl-1 (2022 → 2024-08-16), Clarity-1 (2024 → 2025-03-15), CBERS-4B (2021 → 2019-12-20), ATS-6 (OSCAR's 30 Apr 1974 → NSSDCA's 30 May 1974).
- **Specific errors listed in the task**: TIROS-2 added; HotSat-3 → `proposed`; TRISHNA → `planned`; VanZyl-2 added.
- **Fields removed**: `altitude_km`, `inclination_deg`, `period_min`, `mass_kg`, `all_sensors`, `instrument_type`, `scanning_technique`, `usage_from/to`, `data_quality`. Most values had no source, and the brief's schema does not include them. Swath, revisit and cooling are filled only where the specification source states them (many are therefore empty).

## 8. Records without sources, or with unresolved values

- **Every** design has a `spec_source` and **every** deployment has a `status_source` (no record without a source). 298 of 361 deployment statuses rest on WMO OSCAR/Space alone. Historical dates taken from OSCAR were not independently checked, except where noted (one OSCAR error found: ATS-6 launch date).
- **Status unresolved (2)**: FOREST-3 (no source on data delivery at the audit date); GOES-14 (transferred to USSF in late 2025; no source on activity on 18 Aug 2026).
- **End date unresolved (2)**: FOREST-1 (mission goals met 2022; re-entry 2024-08-03; end of operations not documented); GF-5 (stopped working before 20 Oct 2022; exact date not found).
- **No native sampling (17)**: the 12 limb/occultation sounders listed in §7 (by definition); FOREST-1 TIR imager and FOREST-3 TIR imager (not published); GXS (planned; not published); MSU-MR-MP (planned; channels not resolved).
- **Low-confidence specifications (13)**: e.g. GF-4/13 imager, HRSAT-1, IRMSS-2 (HJ), ISR, EAGLE-TIR radiometer, Clarity LWIR, EDC TIR, HIBISCUS. See the `confidence` column.
- **Source conflicts recorded in notes**: BIROS end of operations (Dec 2020 vs re-entry Jan 2026); MTI end date (eoPortal 2015, unsupported); TET-1 (DLR: active until 2022 re-entry vs eoPortal 2019); TRISHNA launch (CNES 2027 vs OSCAR ≥2028); LSTM launch (SentiWiki 2028 vs OSCAR ≥2029); Landsat-4 TM end (ESA gives both 1987 and 1993); EarthDaily TIR band count (5 vs 4 + wildfire band).

## 9. Coverage: designs documented in OSCAR but not in the inventory

The paper states that the inventory "covers all publicly documented instruments that could be identified in English-language sources". A sweep of all 1,250 OSCAR instrument pages found the following designs that meet the inclusion rule on their OSCAR description. **None was added**: adding them changes the totals further and needs the authors' decision.

| Design | MWIR/LWIR evidence (OSCAR) | Platforms (OSCAR status, launch) |
|---|---|---|
| VHRR (NOAA) | 10.5–12.5 µm, 0.9 km | NOAA-2, -3, -4, -5 (1972–76) |
| VISSR | 10.5–12.6 µm, 6.9 km | SMS-1, SMS-2, GOES-1, -2, -3 (1974–78) |
| VISSR (Himawari 1–4) | 10.5–12.5 µm, 5 km | GMS-1 to -4 (1977–89) |
| S-VISSR (FY-2A/B) | 10.5–12.5 µm, 5.76 km | FY-2A, FY-2B (1997–2000) |
| S-VISSR (FY-2C/D/E) | MWIR + 2 LWIR, 5 km | FY-2C, -2D, -2E (2004–08) |
| CZCS | 10.5–12.5 µm, 825 m | Nimbus-7 (1978) |
| MSU-V | 10.6–12.0 µm, 250 m | Okean-O-1 (1999) |
| SME (IR) | 10.6 µm channel | SME (1981) |
| IRS (SJ-9) | 8–12 µm, 73 m | SJ-9B (2012; OSCAR "Unclear") |
| MIRIS/MEOC | 3–5 µm, 50 m | STSat-3 (2013; "Unclear") |
| COCTS2 | 3.74, 11, 12 µm, <500 m | HY-3A/HY-1E (operational, 2023); HY-1F, HY-3B (planned) |
| EOIR | 3–12 µm (no band details) | EOS-08 (operational, 2024) |
| GIIRS-3 | MWIR/TIR sounder, 8 km | FY-4C (commissioning), FY-4D, FY-4F (planned) |
| GKMI | MWIR/LWIR, 1 km | GEO-KOMPSAT-5 (planned) |
| IMAGER (INSAT-4) | IR 2 km | INSAT-4 (planned) |
| PLATiNO TIR | 8.6–11.5 µm, 40 × 60 m | PLATiNO-2 (planned) |
| FEI | ~10.5 µm, 0.6 km | FORUM (planned) |
| SACFF | VIS/IR, 250 m | G20 (planned) |
| TICFIRE | 7.5–50 µm | AOS-Sky (considered) |
| CO sensor | 4.6 µm | ASCENDS (concept) |

Also identified outside OSCAR and not added: OroraTech SAFIRE Gen4 hosted payloads on four Kepler satellites (launched Jan 2026; host names and status unknown); the constellr HiVE demonstrator on the ISS (2022), which appears in Figure 16.

## 10. Other disagreements between the data and the manuscript

1. **Abstract, Highlights, Overview, Section 3**: 174 / 306 / 55, Figure 12 and the "55 km to 3.5 m" range: see §1–6.
2. **Figure 16**: FOREST-1 is shown with "mid-wave plus 2 long-wave infrared channels · 200 m". The sources found give two thermal channels (MWIR and LWIR) and no published GSD. HSRS (BIRD) 372 m agrees with OSCAR/eoPortal; the FireBIRD (TET-1/BIROS) HSRS samples at 178 m.
3. **Section 2.1 / Figure 13**: MRIR channel set. OSCAR's MRIR record lists 0.2–4.0, 5–30, 6.4–6.9, 10–11 and 14–16 µm, not the TIROS-2 set given in the paper (from NASA GES DISC). Because channel sets varied by mission, the paper's own new-design rule implies MRIR should be split by configuration. One design is kept here, with a note.
4. **Section 2.2**: "Band 8 … failed shortly after launch" (NASA/USGS mission pages) vs USGS Open-File Report 83-123: "became inoperative in early 1979, [after] over 370 thermal IR images".
5. **Table 3**: EAGLE-TIR sampling "Not stated". The CEOS EO Handbook gives 60 m at nadir (undated entry), and the 2023 SBG-TIR design gives ≤ 60 m. HotSat-3 "Not fixed": SatVu planned it for 2026 and launched it on 1 Oct 2026, after the audit date, so `proposed` on the audit date is consistent.
6. **Review method**: the statuses were re-audited against OSCAR/Space plus agency/operator sources. The ITC database and the CEOS EO Handbook were consulted only where cited in individual records.
7. **Data Availability Statement**: says the inventory is "archived". GitHub is not an archive. A Zenodo DOI for the v1.0 release (via the GitHub–Zenodo integration) would make the statement true.

## 11. Repository files not used by the paper

`figures/fig1–3*.png` were generated from the pre-audit data for an earlier notes file and do not appear in the manuscript. They are unchanged and do not reflect v1.0.
