# Improvement Plan — TIR Sensor Database & Paper

*Assessment date: April 2026. Based on audit of 171 sensors, 291 satellites, and current insights.md.*

---

## 1. Dataset Quality Gaps (High Priority)

### 1.1 swath_km — 77 / 171 null (45%)
Swath is missing for nearly half the sensors. This prevents any analysis of spatial coverage,
the resolution × swath trade-off, or data continuity timelines. Actions:
- Fill swath for all operational and historical imagers from ESA eoPortal / WMO OSCAR / ATBDs
- For limb sounders and hyperspectral sounders, set a dedicated `swath_type: "limb"` flag rather
  than leaving null — a null swath for a limb sounder means something different from a null on
  an imager
- Priority sensors: AVHRR series (all NOAA-6 to NOAA-19), MODIS, ASTER, Landsat, FY-3 series,
  Meteor-M series

### 1.2 NEDT — 374 null band entries
NEDT is the single most important sensitivity metric for TIR sensors. It is null for most bands.
Without this, the paper cannot support any quantitative claim about sensitivity trends over decades.
- Fill NEDT for at least all operational and major historical sensors from instrument ATBDs
- For sensors where absolute NEDT is not published, record the instrument-specified noise floor
  (e.g., "< 0.3 K at 300 K") and normalise to K
- Add a `nedt_source` sub-field to each band ("ATBD", "datasheet", "estimate") to be transparent
  about data quality

### 1.3 data_quality = "incomplete" — 115 / 171 sensors (67%)
Most records are flagged incomplete because swath_km is null. Resolving section 1.1 will
automatically promote many of these to "complete". Target: ≥ 60% complete records.

### 1.4 status = "unknown" — 26 sensors
26 sensors have unknown operational status. For a scientific paper, every sensor needs a
confirmed status. These are mostly early Meteor-1/2 and Soviet-era sensors. Assign status from
decommission dates already in the satellites file.

### 1.5 scanning_technique — non-normalised strings
The field currently stores raw OSCAR text (e.g., "Mechanical, 3-axis stabilised satellite,
E-W continuous, S-N stepping") rather than a controlled vocabulary. This makes any comparative
analysis impossible. Normalise to a clean enum:
`whiskbroom | pushbroom | conical | staring | spin-scan | FTS | limb | other`
and move the raw OSCAR description to a `scanning_technique_raw` notes field.

### 1.6 orbit_type — non-normalised strings
Same problem: 15 different orbit_type string values exist instead of the 6 intended categories.
Normalise to: `SSO | GEO | LEO_non-SSO | HEO | ISS | Airborne`

---

## 2. Missing Schema Fields (Medium Priority)

These fields are needed to support the paper's scientific arguments but do not yet exist.

| Field | Type | Rationale |
|---|---|---|
| `detector_material` | string enum | HgCdTe / InSb / QWIP / bolometer / thermopile / other — required to support the detector technology arc narrative |
| `aperture_m` | float | Primary optic diameter — directly supports the Rayleigh diffraction argument; currently only discussed in text, not in data |
| `revisit_days` | float | Single-satellite revisit period at equator — needed for temporal resolution analysis |
| `application_domain` | list[string] | weather / LST / SST / fire / atmosphere / ocean / cryosphere — enables domain-specific trend analysis |
| `no_bands_mwir` | int | Count of MWIR bands — currently derivable but not stored; needed for quick filtering |
| `no_bands_lwir` | int | Count of LWIR bands |
| `data_access` | string enum | open / commercial / restricted / unknown — increasingly relevant given new-space data models |

---

## 3. Missing Scientific Analysis (High Priority for Paper)

### 3.1 The Resolution × Swath Trade-off
This is the most fundamental optical constraint in remote sensing and is never mentioned in
insights.md. The relation IFOV × swath ≈ constant (for a fixed detector array size and telescope
aperture) means that improving resolution always costs swath — and vice versa. MODIS (250–1000 m,
2330 km swath) and ECOSTRESS (38 m, 384 km) sit at opposite ends of the same physical curve.
This explains why no single sensor simultaneously provides high spatial resolution AND daily global
coverage — it is not a funding problem, it is étendue conservation. Adding this section would
make the paper's argument about commercial constellations filling the "temporal + spatial" gap
much stronger: the only way to break the trade-off is multiple satellites, not a better single sensor.

### 3.2 NEDT Trend Over 60 Years
The paper claims sensors improved 25× in sensitivity since AVHRR but does not show this as a
figure. A scatter plot of NEDT (at ~10 µm) vs. first operation year, coloured by cooled/uncooled,
would be one of the most compelling figures in the paper. It would visually demonstrate:
- The step-change between uncooled (1960s) and cryogenic (1990s)
- The plateau in cryogenic NEDT improvement after ~2005 (already near the photon-noise limit)
- The deliberate regression in uncooled new-space sensors (lower NEDT accepted for lower cost)

### 3.3 GEO vs. LEO Complementarity
The paper focuses almost entirely on LEO sensors. But 31 of 171 sensors are GEO — and for many
applications (severe weather, wildfire, diurnal LST cycle) GEO is not a backup to LEO but the
primary platform. A section on what GEO provides that LEO cannot (continuous temporal sampling of
a fixed disc, sub-hourly storm tracking) would round out the paper's coverage of the sensor
landscape.

### 3.4 The Hyperspectral Sounder Revolution
AIRS (2378 channels, 2002), IASI (8461 channels, 2006), CrIS (1305 channels, 2011), and IASI-NG
represent a completely different instrument family from imaging radiometers — yet they make up a
large fraction of the dataset. Their scientific contribution (atmospheric temperature and humidity
profiling to 1 K / 1 km vertical resolution) is not discussed anywhere. A single section on how
sounders differ from imagers, and why both are needed, would make the paper's dataset more
coherent.

### 3.5 Data Continuity and Mission Transition Gaps
Science-quality LST and SST records require sensor overlap for inter-calibration. Key gaps and
transitions are not discussed:
- AVHRR series: continuous from 1978 to present, but instrument-to-instrument calibration drift
  of ~0.5 K per decade affects 40-year LST trends
- MODIS Terra (2000) → VIIRS SNPP (2012): the dominant land LST record transitioned mid-series;
  there are known calibration offsets between the two
- ASTER (2000) → no direct successor currently funded: the 90 m multispectral LWIR record will
  end when Terra decommissions, with no equivalent planned before LSTM (2028)
- Landsat TM/ETM+ → TIRS: TIR band went from 6 channels to 2 channels and from 30 m to 100 m
  native resolution — a spatial regression that is underappreciated
These gaps have direct scientific consequences for long-term climate records.

### 3.6 Commercial vs. Government: A Structural Shift Analysis
The paper notes 9 commercial sensors after 2020 but does not quantify the structural shift.
A rigorous comparison should include:
- Resolution targets: commercial average 3–30 m vs. government average 30–1000 m
- Revisit targets: commercial average 1–6 hours vs. government average 8–16 days (LEO)
- Data policy: commercial (subscription/API) vs. government (open Landsat/MODIS model)
- Calibration standards: commercial sensors largely lack SI-traceable on-orbit calibration
  targets — this is a scientific limitation that is not yet flagged in the paper

---

## 4. Missing Figures for insights.md (Medium Priority)

| Figure | Description | Scientific value |
|---|---|---|
| Fig 4 | NEDT vs. year of first operation, coloured by cooled/uncooled | Shows sensitivity evolution; supports claims in Section 2 |
| Fig 5 | Resolution vs. swath scatter plot, coloured by orbit type | Shows fundamental trade-off; motivates constellation argument |
| Fig 6 | GEO vs. LEO sensor count by decade | Shows growing GEO role |
| Fig 7 | Sensor count by application domain over time | Shows shift from meteorology to land/fire/commercial |
| Fig 8 | Data continuity timeline | Shows which records are continuous vs. gapped |

---

## 5. Writing & Structure Gaps in insights.md

### 5.1 No abstract or framing statement
insights.md starts directly with analysis. For a supplementary paper document it needs an
opening paragraph stating what the dataset is, how it was built, and what this document adds
to the main paper.

### 5.2 Missing uncertainty section
Every scientific dataset paper needs a section on limitations and uncertainty:
- What fraction of sensor data comes from primary sources (ATBDs) vs. secondary (OSCAR)?
- How were conflicts between sources resolved?
- What is the estimated error rate in the dataset?
- Which conclusions are robust to data gaps and which depend on the incomplete records?

### 5.3 Citation coverage uneven
Sections 1 and 3–4 are well cited. The two new sections (bolometer physics, LST accuracy) would
benefit from 2–3 more primary references each — particularly:
- Planck-law error propagation for the emissivity uncertainty argument
- A specific MODIS→VIIRS calibration comparison study for the LST accuracy ceiling claim
- A cryogenic bolometer D* measurement paper to support the D* gap numbers

### 5.4 No methods section for the dataset
The README describes sources but not the methodology: how were conflicts resolved? How were
planned-mission parameters estimated? How was spectral_type assigned for sensors spanning both
MWIR and LWIR? A short methods section adds reproducibility and is required for most journals.

---

## 6. Repository / Reproducibility Improvements

- Add `build_figures.py`: a single script that reads sensors_tir.json and reproduces all figures
  in figures/ — currently the figures exist as PNGs but the code that generated them is not in
  the repo, making the analysis non-reproducible
- Add `validate.py`: automated schema validation (field types, enum values, range checks) so
  contributors can verify their additions without reading the full README
- Add `CHANGELOG.md`: version history of the dataset with dates and record counts — important
  for datasets cited in scientific papers, so downstream users know which version they used
- Consider a DOI via Zenodo: depositing the dataset on Zenodo gives a citable DOI independent
  of the paper DOI, which is standard practice for companion datasets

---

## Priority Order

| Priority | Item | Effort | Impact |
|---|---|---|---|
| 1 | Fill swath_km for imagers | Medium | Fixes 67% incomplete records, enables trade-off analysis |
| 2 | Fill NEDT for major sensors | High | Enables Fig 4 and quantitative sensitivity claims |
| 3 | Normalise scanning_technique and orbit_type | Low | Fixes data usability for any filtering/analysis |
| 4 | Add resolution × swath trade-off section | Low | Strongest missing scientific argument |
| 5 | Add NEDT trend figure (Fig 4) | Medium | Most visually compelling missing figure |
| 6 | Add data continuity section | Medium | Directly relevant to LST science users |
| 7 | Add aperture_m field | Medium | Quantifies the Rayleigh argument from data not just text |
| 8 | Add methods + limitations section to insights.md | Low | Required for journal submission |
| 9 | Add build_figures.py to repo | Low | Reproducibility — increasingly required by journals |
| 10 | Deposit dataset on Zenodo for DOI | Low | Standard for companion datasets |

---

*This plan covers scientific depth, data completeness, and reproducibility — the three axes on
which reviewers of a companion-dataset paper typically focus.*
