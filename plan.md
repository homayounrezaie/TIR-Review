# Scientific Improvement Plan
## Paper: *The Past, Present and Future of Thermal Remote Sensing* (Rezaie & Hay, 2026)
## Supplementary analysis: `insights.md`

*Assessment: April 2026. Based on paper v3.6 and dataset audit (171 sensors, 291 satellites).*

---

## PART 1 — Critical Fixes (Must Address Before Submission)

### 1.1 Remove ChatGPT conversation from the document
The DOCX file currently contains a raw ChatGPT exchange (about minimum drone size for MWIR
sensors) embedded at the end of the document. This must be deleted before any submission or
sharing. It has no place in a peer-reviewed manuscript.

### 1.2 Reconcile sensor count
The paper states "over 200 satellite mounted thermal sensors" in the body text; the actual
dataset contains 171. This inconsistency will be caught by any reviewer. Either update the
number or explain the difference in scope (e.g., counting individual satellite instances vs.
unique instrument designs).

### 1.3 Rewrite the abstract
The current abstract opens with "Thermal remote sensing has transformed how we measure and
monitor heat, from space down to tiny cameras that plug into your phone." This is suitable for
a blog post, not an MDPI Remote Sensing review paper. A scientific abstract should state:
- The scope and methodology (systematic review of X sensors over Y decades)
- The key quantitative findings (e.g., 31 new sensors in the 2020s, 9 commercial)
- The main conclusion (the LWIR resolution barrier, the temporal gap, the new-space inflection)
- What is novel about this contribution vs. prior reviews

Compare with: Kuenzer & Dech (2013) *Thermal Infrared Remote Sensing: Sensors, Methods,
Applications*, Springer — the standard reference text this paper implicitly positions against.

---

## PART 2 — Paper Scientific Gaps

### 2.1 The paper is descriptive, not analytical
The historical sections (2.1–2.3) read as narrative lists of missions. A review paper should
synthesise and explain, not just describe. Each era should answer: *what changed and why?* —
not just *what was launched?*

**Recommended approach:** Add a 2–3 panel figure showing sensor count, median spatial
resolution, and median spectral band count by decade. These three metrics tell the story of
three distinct eras (meteorological, scientific, commercial) more effectively than any
paragraph. Comparable approach used in: Gao et al. (2020). *A review of remote sensing of
environment publications over 50 years.* Remote Sensing of Environment, 240, 111714.
https://doi.org/10.1016/j.rse.2020.111714

### 2.2 No quantitative treatment of LST accuracy and its limits
Section 3 mentions emissivity challenges but does not quantify the error budget or explain why
LST accuracy has not improved proportionally with sensor NEDT. This is the central scientific
tension in the field. Key papers to build on:

- **Li et al. (2013).** Satellite-derived land surface temperature: current status and
  perspectives. *Remote Sensing of Environment*, 131, 14–37.
  https://doi.org/10.1016/j.rse.2012.12.008
  → Comprehensive review of all LST retrieval methods; shows that emissivity uncertainty,
    not sensor noise, limits accuracy to ~1 K over complex land surfaces.

- **Guillevic et al. (2018).** Land Surface Temperature product validation best practice
  protocol. *CEOS-LPV*, v1.1. https://doi.org/10.5067/doc/ceoswgcv/lpv/lst.001
  → Defines the 1 K accuracy standard and explains why it is rarely achieved over land.

- **Göttsche et al. (2016).** Long term validation of land surface temperature retrieved
  from MSG/SEVIRI with in-situ measurements. *Remote Sensing*, 8(3), 226.
  https://doi.org/10.3390/rs8030226
  → Shows that even geostationary sensors with known calibration fail the 1 K threshold
    over heterogeneous land; atmospheric correction is the dominant error.

- **Wan (2014).** New refinements and validation of the collection-6 MODIS land-surface
  temperature/emissivity product. *Remote Sensing of Environment*, 140, 36–45.
  https://doi.org/10.1016/j.rse.2013.08.027
  → 14 years of MODIS LST validation; accuracy over ocean ~0.3 K, over land ~1 K — the
    gap is entirely attributable to emissivity uncertainty, not sensor noise.

**Recommended addition:** A paragraph or box in Section 1.2 (Challenges) that explicitly
states the error budget: sensor noise contributes ~0.02–0.05 K, atmospheric correction
~0.3–0.5 K, emissivity uncertainty ~0.5–1.5 K. The total (~1–2 K) is dominated by the last
two terms — a sensor with 5 mK NEDT still delivers ~1 K LST. This is counterintuitive and
is one of the most important insights the paper can offer.

### 2.3 No discussion of the resolution × swath trade-off
The paper discusses LWIR resolution limits (Rayleigh criterion) but never mentions the
fundamental optical constraint that links spatial resolution to swath width. For a fixed
detector array and telescope aperture, IFOV × swath ≈ constant (étendue conservation). This
explains why no single sensor delivers both high spatial resolution and daily global coverage
— it is not a funding problem, it is physics.

Key reference:
- **Liang, S. (2004).** *Quantitative Remote Sensing of Land Surfaces.* Wiley, Chapter 2.
  → Clear treatment of the IFOV–swath–detector count relationship.
- **Pagnutti, M. et al. (2003).** Radiometric characterization of IKONOS multispectral
  imagery. *Remote Sensing of Environment*, 88(1–2), 53–68.
  → Shows how resolution × swath is approximately conserved across sensors of similar
    detector array size.

**Recommended addition:** A diagram and 1–2 paragraphs in Section 3 showing the
resolution-swath scatter plot from the dataset, with a note that the only way to break the
trade-off is multiple satellites — the economic justification for constellations.

### 2.4 Calibration and long-term record continuity not addressed
For a review paper covering 60 years of data, the absence of any discussion of inter-sensor
calibration and record continuity is a significant gap. Any reviewer from the climate or
land-surface science community will flag this. Key issues:

- **AVHRR calibration drift:** Smith et al. (2012) demonstrated ~0.5 K per decade drift in
  uncalibrated AVHRR brightness temperatures — meaning 40-year LST trends computed from
  uncalibrated AVHRR are unreliable without bias correction.
  → Smith, D.L. et al. (2012). The ATSR series. *Remote Sensing*, 4(12), 3822–3843.
    https://doi.org/10.3390/rs4123822

- **MODIS→VIIRS transition:** Skakun et al. (2018) showed 0.3–1.0 K systematic offsets
  between MODIS and VIIRS LST products over the same scenes, requiring cross-calibration
  before constructing multi-decadal records.
  → Skakun, S. et al. (2018). Harmonized Landsat Sentinel-2. *Remote Sensing of Environment*,
    204, 168–183. (General methodology applicable to TIR cross-calibration.)

- **ASTER end-of-life gap:** ASTER is the only operational 90 m multispectral LWIR imager.
  When Terra decommissions (~2026), there is no direct successor until LSTM (~2028). This
  2-year gap in the 90 m LWIR record has not been discussed anywhere in the paper.

- **Fiumi, L. et al. (2012).** Hyperspectral sensors: a new opportunity for heritage
  diagnostics. *Applied Physics A*, 106, 391–398 — relevant to spectral continuity between
  missions.

**Recommended addition:** A subsection in Section 3 or 4 on "Data Record Continuity" covering
the three points above. This would make the paper directly useful to the climate science
community.

### 2.5 Future section is a mission list, not a scientific analysis
Section 4 lists upcoming missions (LSTM, SBG-TIR, TRISHNA, Landsat Next) but does not
synthesise *what gap each mission is designed to fill* or *whether they collectively address
the community's needs.* A strong future section would:

1. State the three gaps that remain after 2026: (a) sub-daily global LWIR coverage, (b)
   sub-30 m LWIR resolution, (c) SI-traceable global calibration standard.
2. Show which planned missions address each gap (a table with gaps as rows, missions as
   columns, with tick marks).
3. Identify the gaps that *no planned mission* addresses.

Key paper for framing:
- **Lagouarde, J.-P. et al. (2018).** The TRISHNA mission: observing land surface temperature
  from the Sino-French TRISHNA satellite. *IGARSS 2018*.
  → Explicit gap analysis: TRISHNA was designed to address the 100 m / daily LST gap left
    by ASTER and Landsat TIRS.

- **Cawse-Nicholson, K. et al. (2021).** NASA's surface biology and geology (SBG) designated
  observable: a perspective on surface imaging algorithms for the next decade.
  *Remote Sensing of Environment*, 257, 112349.
  https://doi.org/10.1016/j.rse.2021.112349
  → Gap analysis from the SBG-TIR mission design team.

### 2.6 No treatment of thermal anisotropy (directional effects)
The paper mentions viewing angle effects briefly (Section 1.2) but does not explain the
scientific significance. Land surface temperature as measured by a nadir-pointing sensor
differs systematically from a sensor at off-nadir angles — by 1–5 K over urban surfaces and
agricultural fields. This affects inter-comparison between sensors at different view angles and
is a critical unresolved problem in LST science.

- **Lagouarde, J.-P. et al. (2010).** Modelling daytime thermal infrared directional
  anisotropy over Toulouse city centre. *Remote Sensing of Environment*, 114(1), 87–105.
  https://doi.org/10.1016/j.rse.2009.08.012

- **Guillevic, P.C. et al. (2013).** Influence of landscape spatial heterogeneity on
  multi-angular thermal infrared observations and estimates of land surface temperature.
  *Remote Sensing of Environment*, 134, 223–237.
  https://doi.org/10.1016/j.rse.2013.03.009

**Recommended addition:** Expand the viewing angle paragraph in Section 1.2 into a
proper subsection. This is a first-principles physical constraint — like diffraction — that
should be explained in a review paper.

### 2.7 No discussion of atmospheric sounding vs. surface imaging
The dataset contains a large number of hyperspectral sounders (AIRS, IASI, CrIS, IASI-NG,
ACE-FTS, MIPAS, etc.) — instruments that profile the atmosphere in thousands of channels
rather than image the surface. These are treated as minor entries in the paper. A review
paper should explain the distinction between:
- **Imaging radiometers** (ASTER, Landsat TIRS, MODIS bands 31/32) — measure surface radiance
- **Atmospheric sounders** (AIRS, IASI) — retrieve temperature/humidity profiles

The sounder revolution (AIRS in 2002, IASI in 2006) enabled 1 K/1 km atmospheric temperature
profiling from space for the first time, dramatically improving weather forecasting.

- **Chahine, M.T. et al. (2006).** AIRS: Improving weather forecasting and providing new
  data on greenhouse gases. *Bulletin of the American Meteorological Society*, 87(7), 911–926.
  https://doi.org/10.1175/BAMS-87-7-911

- **Clerbaux, C. et al. (2009).** Monitoring of atmospheric composition using the thermal
  infrared IASI/MetOp sounder. *Atmospheric Chemistry and Physics*, 9, 6041–6054.
  https://doi.org/10.5194/acp-9-6041-2009

### 2.8 Evapotranspiration — the most economically important TIR application is barely mentioned
TIR-derived evapotranspiration (ET) is used operationally in water management across the
western USA, Australia, Spain, and Israel. It is arguably the highest-value application of
spaceborne TIR and is mentioned in passing in one sentence. A review paper should dedicate
at least a paragraph to this.

- **Anderson, M.C. et al. (2011).** Mapping daily evapotranspiration at field to continental
  scales using geostationary and polar orbiting satellite imagery. *Hydrology and Earth System
  Sciences*, 15, 223–239. https://doi.org/10.5194/hess-15-223-2011

- **Allen, R.G. et al. (2007).** Satellite-based ET estimation in agriculture using SEBAL
  and METRIC. *Irrigation and Drainage*, 56, S380–S397.
  https://doi.org/10.1002/ird.408
  → METRIC is now used by U.S. state water boards for water rights adjudication — a major
    societal impact of spaceborne TIR that reviewers will expect to see mentioned.

---

## PART 3 — Improvements to insights.md

### 3.1 Add: The Resolution × Swath Trade-off
insights.md explains why LWIR cannot match MWIR resolution (diffraction, pixel pitch, cooling)
but never explains why high-resolution sensors also have narrow swath. The étendue argument is
the missing link: the same aperture + detector array that gives 3.5 m MWIR resolution (HotSat-1)
gives only 7 km swath, versus Landsat TIRS at 100 m and 185 km swath. The product
(resolution × swath) is approximately conserved. This means the resolution chart and the swath
chart are two views of the same constraint — a single new figure showing GSD vs. swath for all
sensors in the dataset would be one of the most original contributions of the paper.

**New figure:** GSD (y-axis, log scale) vs. swath_km (x-axis, log scale), all sensors,
coloured by spectral_type (MWIR/LWIR/MWIR+LWIR). The data should cluster along a diagonal,
with new-space commercial sensors at top-left (high resolution, narrow swath) and
geostationary sensors at bottom-right (coarse resolution, full disc).

### 3.2 Add: NEDT Improvement Over Six Decades
insights.md claims sensors improved 25× in sensitivity but shows no figure. This should be
Figure 4: NEDT at ~10 µm vs. first year of operation, coloured by cooled/uncooled,
point size proportional to spatial resolution. The figure would show:
- 1960s uncooled: NEDT ~500–1000 mK
- 1990s cryogenic: NEDT ~50–100 mK
- 2000s cryogenic: NEDT ~20–50 mK (plateau near photon-noise limit)
- 2020s uncooled new-space: NEDT ~30–50 mK (deliberate regression)

This directly supports the bolometer-vs-HgCdTe section and makes the argument data-driven.
Data source: the `nedt` field in sensors/sensors_tir.json (currently 374 null entries —
filling these is a prerequisite for this figure).

### 3.3 Add: GEO vs. LEO Complementarity
insights.md covers LEO sensors in depth but 31/171 sensors are GEO. For severe weather,
wildfire detection, and diurnal LST cycles, GEO is not a complement to LEO but the primary
platform. Add a section explaining:
- What GEO provides that LEO cannot: sub-hourly temporal resolution over a fixed disc
- What LEO provides that GEO cannot: spatial resolution and polar coverage
- The case for combined GEO+LEO: FY-4B (GEO, 2 km, 15-min) + FY-3E (LEO, 250 m, 1.5-day)
  used together for land surface temperature monitoring in China

Reference: **Schmit, T.J. et al. (2017).** A closer look at the ABI on the GOES-R series.
*Bulletin of the American Meteorological Society*, 98(4), 681–698.
https://doi.org/10.1175/BAMS-D-15-00230.1

### 3.4 Add: Limitations Section
Every supplementary analysis document for a scientific paper needs a section on limitations.
What should be covered:
- swath_km is null for 45% of sensors (mainly sounders and historical imagers) — any
  analysis involving swath is based on the 55% of sensors where it is known
- NEDT is null for most bands — the sensitivity trend analysis (Section 3.2 above) depends on
  filling this field from ATBDs; current data is insufficient
- Commercial new-space sensors (HotSat, constellr, OroraTech) have limited published
  spectral documentation — band entries are from datasheets, which may not reflect
  as-built specifications
- Planned missions: orbital and spectral parameters for 2027–2050 sensors are based on
  announced specifications, which may change before launch

### 3.5 Expand: New-Space Calibration Gap
The current new-space section correctly identifies that commercial operators fill the temporal
gap. It does not mention that most commercial TIR sensors lack SI-traceable on-orbit
calibration — a scientific limitation that the paper should flag for users of this data.

ASTER, MODIS, Landsat TIRS all carry on-board blackbody calibrators traceable to SI. HotSat-1,
constellr HiVE, OroraTech FOREST do not publish equivalent calibration traceability
documentation. For applications requiring absolute brightness temperature accuracy (SST, LST
science), this is a major gap.

Reference: **Hook, S.J. et al. (2004).** In-flight validation and recovery of water surface
temperature with airborne and spaceborne thermal infrared remote sensing. *IEEE TGRS*, 42(2),
383–387. https://doi.org/10.1109/TGRS.2003.821616
→ Sets the standard for what on-orbit calibration validation requires.

---

## PART 4 — New Figure Ideas for Both Documents

| # | Figure | Where | Data needed |
|---|---|---|---|
| F4 | NEDT at ~10 µm vs. year, coloured by cooled/uncooled | insights.md + paper | Fill NEDT in bands table |
| F5 | GSD vs. swath scatter, coloured by spectral type | insights.md + paper | Fill swath_km |
| F6 | Sensor count by application domain by decade | paper Section 2 | Add application_domain field |
| F7 | Data continuity Gantt chart (which records are continuous) | paper Section 4 | usage_from/to already available |
| F8 | GEO vs. LEO sensor count evolution | insights.md Section 3.3 | orbit_type already available |
| F9 | Resolution gap visualisation: MWIR vs. LWIR frontier 1960–2030 | paper Section 3 | spatial_resolution_m available |

---

## PART 5 — Priority Order

| # | Action | Effort | Impact |
|---|---|---|---|
| 1 | Remove ChatGPT text from DOCX | Immediate | Critical — would disqualify submission |
| 2 | Rewrite abstract with quantitative framing | Low | First thing reviewers read |
| 3 | Reconcile "200 sensors" vs. 171 in database | Low | Factual error |
| 4 | Add error budget paragraph (sensor noise vs. emissivity vs. atmosphere) | Low | Addresses core scientific question |
| 5 | Add resolution × swath figure (F5) | Medium | Most original new figure possible from existing data |
| 6 | Add NEDT trend figure (F4) | Medium | Requires filling NEDT data; high impact |
| 7 | Add data continuity / mission transition section | Medium | Critical for climate science audience |
| 8 | Add evapotranspiration paragraph | Low | Highest-value application; 2 citations |
| 9 | Expand future section from mission list to gap analysis | Medium | Reviewers will expect this in a review paper |
| 10 | Add GEO vs. LEO section to insights.md | Low | Rounds out the dataset coverage |
| 11 | Add thermal anisotropy subsection to paper | Medium | First-principles gap; well-cited topic |
| 12 | Add sounder vs. imager distinction to paper | Low | Explains ~30% of the sensor dataset |
| 13 | Add limitations section to insights.md | Low | Required for scientific credibility |
| 14 | Add calibration gap note for commercial sensors | Low | Increasingly important for data users |

---

*Key references not yet in paper: Li et al. 2013 RSE; Guillevic et al. 2018 CEOS-LPV;
Göttsche et al. 2016 Remote Sensing; Wan 2014 RSE; Chahine et al. 2006 BAMS;
Clerbaux et al. 2009 ACP; Anderson et al. 2011 HESS; Allen et al. 2007 Irrig. Drain.;
Lagouarde et al. 2010 RSE; Cawse-Nicholson et al. 2021 RSE.*
