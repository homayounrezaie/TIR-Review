# Thermal Infrared Satellite Sensors Database

A curated, open dataset of every space-borne sensor that observes Earth in the mid-wave infrared (MWIR, 3–6 µm) and long-wave infrared (LWIR, 6–15 µm). Built from WMO OSCAR, ESA eoPortal, agency mission pages, and peer-reviewed ATBDs.

This dataset accompanies the review paper:

> Rezaie, A., & Hay, G. J. (2025). The past, present and future of thermal remote sensing. *MDPI Sensors*, 25(x), xxxx. https://doi.org/10.3390/sXXXXXXX

---

## Dataset at a glance

| Metric | Value |
|---|---|
| TIR sensors | **167** |
| Satellites carrying them | **288** |
| Space agencies represented | **36** |
| Temporal span | **1964 – 2050** |
| Sensors with full band tables | **167 / 167 (100%)** |
| Operational sensors | 47 |
| Planned / future sensors | 14 |
| Historical (retired) sensors | 80 |
| Sensors with spatial resolution | 162 / 167 (97%) |
| Complete records | 52 / 167 (31%) |

### By spectral type

| Type | Count | Description |
|---|---|---|
| MWIR + LWIR | 103 | Covers both 3–6 µm and 6–15 µm |
| LWIR only | 58 | Primarily 8–15 µm window / sounding |
| MWIR only | 6 | Primarily 3–6 µm (e.g. fire detection) |

### By scanning technique

| Technique | Count |
|---|---|
| Whiskbroom | 61 |
| Pushbroom | 31 |
| Fourier Transform Spectrometer (FTS) | 3 |
| Spin-scan (GEO) | 5 |
| Conical | 8 |
| Staring / framing | 2 |
| Limb / limb occultation | ~14 |

### By detector cooling

| Cooling | Count |
|---|---|
| Cryogenic | 38 |
| Passive radiative | 23 |
| Uncooled | 33 |
| Unknown | 73 |

### Top agencies

| Agency | Sensors |
|---|---|
| NASA | 36 |
| Roscosmos | 20 |
| NOAA | 16 |
| CMA | 15 |
| JAXA | 12 |
| UKSA | 8 |
| ESA | 8 |
| JMA | 6 |
| ISRO | 6 |
| CNES | 4 |

---

## Files

| File | Rows | Description |
|---|---|---|
| `sensors_tir.json` | 167 | One record per TIR sensor. Primary view — includes full `thermal_bands` sub-array. |
| `sensors_tir.csv` | 167 | Flat CSV of the same data; `thermal_bands` serialised as JSON string. |
| `satellites_tir.json` | 288 | One record per satellite; includes orbital parameters and sensor lists. |
| `satellites_tir.csv` | 288 | Flat CSV version of the satellite view. |
| `dropped_sensors.json` | 38 | Sensors removed during filtering and the reason (solar monitors, microwave, etc.). |
| `added_sensors.json` | 5 | Sensors added beyond OSCAR that were absent from the WMO database. |
| `enrichment_report.md` | — | Field coverage statistics and known data gaps. |
| `build_tir_complete.py` | — | Reproducible build script — regenerates all outputs from source data. |

---

## Sensor schema (`sensors_tir.json`)

Each element of the top-level array is a sensor record:

```jsonc
{
  // ── Identity ─────────────────────────────────────────────
  "acronym":          "MODIS",          // Short identifier used as primary key
  "full_name":        "Moderate Resolution Imaging Spectroradiometer",
  "agency":           "NASA",           // Responsible agency acronym
  "oscar_link":       "https://space.oscar.wmo.int/instruments/view/modis",

  // ── Instrument characteristics ──────────────────────────
  "instrument_type":  "Multi-purpose imaging Vis/IR radiometer",
  "spectral_type":    "MWIR+LWIR",      // "MWIR", "LWIR", or "MWIR+LWIR"
  "scanning_technique": "whiskbroom",
  "cooled":           "cryogenic",      // "cryogenic" | "passive_radiative" | "uncooled" | "unknown"

  // ── Geometry ─────────────────────────────────────────────
  "spatial_resolution_m": 1000,         // Native IFOV at nadir, metres
  "swath_km":         2330,             // Cross-track swath, km (null for sounders/limb)
  "orbit_type":       "SSO",            // "SSO" | "GEO" | "LEO_non-SSO" | "HEO" | "ISS"

  // ── Spectral bands (TIR only) ────────────────────────────
  "no_of_bands_total":    36,           // Total bands across all wavelengths
  "no_of_thermal_bands":  16,           // Bands with centre ≥ 3 µm
  "thermal_bands": [                    // See thermal_bands sub-schema below
    { ... }
  ],

  // ── Operational timeline ──────────────────────────────────
  "usage_from":   1999,                 // First year in operation (launch year)
  "usage_to":     null,                 // Last year (null = still operational)
  "status":       "operational",        // "operational" | "historical" | "planned" | "unknown"

  // ── Platform links ────────────────────────────────────────
  "satellites":   ["Terra", "Aqua"],    // Satellite names this sensor has flown on
  "short_description": "...",           // One-sentence summary

  // ── Data quality ─────────────────────────────────────────
  "data_quality": "complete",           // "complete" | "incomplete" | "needs_review"
  "notes":        null,                 // Free-text flag for anomalies
  "additional_sources": ["https://..."] // Sources beyond OSCAR
}
```

### `thermal_bands` sub-schema

Each element of `thermal_bands` describes one spectral channel:

```jsonc
{
  "band_id":      "B31",         // Short identifier (band number, acronym, or purpose label)
  "center_um":    11.03,         // Centre wavelength, µm
  "bandwidth_um": 0.50,          // Full bandwidth (FWHM or passband width), µm
  "range_um":     [10.78, 11.28],// [lower, upper] wavelength boundaries, µm
  "region":       "LWIR",        // "MWIR" (3–6 µm) or "LWIR" (6–15 µm)
  "purpose":      "Cloud top temperature / SST",  // Primary application
  "nedt":         0.05           // Noise-equivalent temperature difference, K (null if unknown)
}
```

**Notes:**
- Hyperspectral sensors (AIRS, CrIS, IASI, IASI-NG, IIS) store 2–3 representative spectral intervals rather than thousands of individual channels.
- Sensors flagged `data_quality: "needs_review"` have provisional band entries derived from secondary sources; values should be verified against the primary ATBD.

---

## Satellite schema (`satellites_tir.json`)

```jsonc
{
  // ── Identity ─────────────────────────────────────────────
  "name":           "Terra",
  "alt_names":      ["EOS-AM-1"],
  "operator":       "NASA",
  "country":        "USA",

  // ── Orbital parameters ────────────────────────────────────
  "orbit_type":     "SSO",
  "altitude_km":    705,
  "inclination_deg": 98.2,
  "period_min":     99.0,
  "mass_kg":        5190,

  // ── Timeline ─────────────────────────────────────────────
  "launch_date":    "1999-12-18",      // ISO-8601 date string
  "decommission_date": null,
  "status":         "operational",

  // ── Payload ──────────────────────────────────────────────
  "tir_sensors":    ["MODIS", "ASTER", "CERES"],  // Sensors in this dataset
  "all_sensors":    ["MODIS", "ASTER", "CERES", "MOPITT", "MISR"],  // Full payload

  // ── Provenance ───────────────────────────────────────────
  "sources":        ["https://..."],
  "notes":          null
}
```

---

## Scope — what is included and excluded

### Included

- **Thermal imagers** — whiskbroom, pushbroom, staring arrays with bands in 3–15 µm
- **VIS/IR multi-spectral sensors** — at least one thermal band confirmed (e.g. AVHRR, MODIS, Landsat TM/ETM+/TIRS, AHI, SEVIRI)
- **IR sounders** — nadir-pointing hyperspectral (AIRS, CrIS, IASI, IASI-NG) and cross-nadir (HIRS family, ATOVS)
- **Limb sounders with TIR bands** — MIPAS, ACE-FTS, HALOE, LIMS, SAMS
- **Commercial/new-space TIR** — SatVu HOTSAT, OroraTech FOREST, constellr HiVE, Albedo Clarity (where public specs confirmed TIR capability)
- **Future/planned sensors** — TRISHNA, SBG-TIR, LSTM, Landsat Next (LandIS), MTG-I/S (IRS, FCI), MetOp-SG, JPSS-3/4, FY-3G/H, GOSAT-GW

### Excluded (38 dropped sensors)

| Category | Count | Examples |
|---|---|---|
| Solar irradiance monitors | 20 | ACRIM I/II/III, TIM, VIRGO, PREMOS |
| Passive microwave radiometers | 17 | AMSR, AMSR-E, AMSR2, GMI, CIMR, SMMR |
| Active microwave (SAR, scatterometer) | 1 | AMI |
| Pure VIS/NIR/SWIR | 1 | CZCS |

Full details in [`dropped_sensors.json`](dropped_sensors.json).

---

## Data sources and enrichment priority

Records were built by merging data from the following sources in descending priority:

1. **[WMO OSCAR/Space](https://space.oscar.wmo.int/)** — spectral ranges, IFOV, swath, orbit, agency
2. **Instrument ATBDs and user guides** — authoritative band tables for hyperspectral sounders (AIRS, CrIS, IASI) and radiation budget sensors
3. **[ESA eoPortal](https://www.eoportal.org/)** — mission overviews, updated specifications
4. **[CEOS EO Handbook](https://database.eohandbook.com/)** — cross-check for scanning technique, orbit, status
5. **[NASA Earthdata](https://www.earthdata.nasa.gov/)** — NASA-specific instruments and satellites
6. **Agency mission pages** (NOAA, ESA, JAXA, JMA, CMA, CNES, ISRO, CSA, UKSA, EUMETSAT, Roscosmos)
7. **[Gunter's Space Page](https://space.skyrocket.de/)** — satellite-level launch dates, mass, orbit parameters
8. **Manufacturer/commercial datasheets** — new-space sensors (SatVu, OroraTech, constellr, Albedo, Hydrosat)

---

## Data quality

Every record carries a `data_quality` tag:

| Tag | Meaning | Count |
|---|---|---|
| `complete` | All five tier-1 fields populated and cross-validated | 52 |
| `incomplete` | One or more tier-1 fields still `null` after checking all sources | 115 |
| `needs_review` | Provisional values from secondary sources; awaiting verification | ~5 |

**Tier-1 fields** (required for `complete`): `thermal_bands`, `spatial_resolution_m`, `swath_km`, `scanning_technique`, `orbit_type`.

The most commonly missing field is `swath_km` (populated for 92/167 = 55%): limb sounders have no meaningful swath, and many historical sensors have no published value. All other tier-1 fields reach ≥ 97% coverage.

---

## Quick start

### Load and filter sensors

```python
import json

with open("sensors_tir.json") as f:
    sensors = json.load(f)

# All operational LWIR sensors with sub-100 m ground resolution
high_res = [
    s for s in sensors
    if s["status"] == "operational"
    and "LWIR" in (s.get("spectral_type") or "")
    and isinstance(s.get("spatial_resolution_m"), (int, float))
    and s["spatial_resolution_m"] < 100
]
print([s["acronym"] for s in high_res])
```

### Explore with pandas

```python
import pandas as pd

df = pd.read_csv("sensors_tir.csv")

# Sensors by agency
print(df.groupby("agency")["acronym"].count().sort_values(ascending=False).head(10))

# Resolution histogram by spectral type
df.groupby("spectral_type")["spatial_resolution_m"].describe()

# Count of sensors by decade of first launch
df["decade"] = (df["usage_from"] // 10 * 10).astype("Int64")
print(df.groupby("decade")["acronym"].count())
```

### Query thermal bands

```python
import json

with open("sensors_tir.json") as f:
    sensors = json.load(f)

# Sensors with a window channel near 11 µm
def has_window_band(s, lo=10.5, hi=11.5):
    for b in s.get("thermal_bands") or []:
        c = b.get("center_um") or 0
        if lo <= c <= hi:
            return True
    return False

window_sensors = [s["acronym"] for s in sensors if has_window_band(s)]
print(f"{len(window_sensors)} sensors have a channel near 11 µm")
```

### Look up a satellite

```python
import json

with open("satellites_tir.json") as f:
    sats = json.load(f)

# Find all GEO satellites
geo = [s for s in sats if s.get("orbit_type") == "GEO"]
for s in geo:
    print(s["name"], "—", s.get("tir_sensors"))
```

### Timeline of planned sensors

```python
import json, datetime

with open("sensors_tir.json") as f:
    sensors = json.load(f)

planned = sorted(
    [s for s in sensors if s["status"] == "planned"],
    key=lambda x: x.get("usage_from") or 9999
)
for s in planned:
    print(f"{s.get('usage_from', '?')}  {s['acronym']:20s}  {s.get('agency','?')}")
```

---

## Methodology

### Filtering rules

Starting from 205 OSCAR-scraped records plus commercial sensors not in OSCAR:

1. **Drop** any sensor whose primary function is solar irradiance measurement (ACRIM family, TIM, VIRGO, etc.) — these measure the Sun, not Earth's thermal emission.
2. **Drop** passive microwave radiometers (AMSR family, GMI, CIMR, SMMR, etc.) — they operate at GHz frequencies (cm wavelengths), not 3–15 µm.
3. **Drop** active microwave instruments (SAR, scatterometer) and pure VIS/NIR/SWIR imagers with no confirmed thermal band.
4. **Keep** any sensor with at least one spectral band whose centre wavelength or range overlaps 3–15 µm.
5. **Keep and flag** ambiguous sensors with `data_quality: "needs_review"` rather than dropping them.

### Band classification

| Wavelength range | Region label |
|---|---|
| 3.0 – 6.0 µm | `MWIR` |
| 6.0 – 15.0 µm | `LWIR` |
| Spans both | `MWIR+LWIR` |

### Orbit classification

| Value | Meaning |
|---|---|
| `SSO` | Sun-synchronous orbit |
| `GEO` | Geostationary (35 786 km) |
| `LEO_non-SSO` | Low Earth orbit, non-sun-synchronous (e.g. ISS nadir, UARS, TIMED) |
| `HEO` | Highly elliptical orbit |
| `ISS` | International Space Station |
| `Airborne` | Aircraft platform (not satellite) |

### Cooling classification

| Value | Meaning |
|---|---|
| `cryogenic` | Active mechanical cooler or expendable cryogen |
| `passive_radiative` | Passive radiative cooler only |
| `uncooled` | Uncooled microbolometer or pyroelectric detector |
| `unknown` | Not specified in available sources |

---

## Known limitations

- **swath_km missing for ~45%** of sensors: limb sounders have no swath; many historical instruments have no published value in OSCAR or eoPortal.
- **`cooled` is unknown for 44%** of sensors (mostly older OSCAR records where the original database entry doesn't specify detector technology).
- **Hyperspectral band entries are representative**, not exhaustive: AIRS (2378 channels), CrIS (1305), IASI (8461), and IASI-NG are stored as 2–3 representative spectral intervals; individual channel tables are available in the respective ATBDs.
- **Commercial new-space sensors** (OroraTech, constellr, Albedo, Hydrosat, SatVu) have limited public spectral documentation; band entries marked `needs_review` are derived from product datasheets and may change with published results.
- **Satellite orbital parameters** for 246/288 satellites come from hardcoded values in the build script; only 42 satellites currently have `orbit_type` populated in the satellite-centered view.
- **`usage_from` for planned sensors** uses the currently planned launch year, which may slip.

---

## Reproducibility

All output files can be regenerated from the raw OSCAR base data:

```bash
# Requirements: Python ≥ 3.10, beautifulsoup4
pip install beautifulsoup4

python3 build_tir_complete.py
```

The script:
1. Loads `sensors_base.json` (195 OSCAR records) and `thermal_sensors.json` (pre-enriched from prior session)
2. Applies filtering rules → produces `dropped_sensors.json`
3. Merges `MANUAL_TIR_SUPPLEMENT` (band data for ~70 sensors that OSCAR doesn't tabulate)
4. Attempts live OSCAR page fetches with 15-minute disk cache in `cache/`
5. Appends 5 commercial sensors from `ADDITIONAL_SENSORS`
6. Outputs all JSON and CSV files, `README.md`, and `enrichment_report.md`

Cached HTML pages are stored in `cache/space.oscar.wmo.int/` and will be reused on subsequent runs.

---

## How to cite

If you use this dataset in a publication, please cite the accompanying review paper:

**APA:**
> Rezaie, A., & Hay, G. J. (2025). The past, present and future of thermal remote sensing. *MDPI Sensors*, *25*(x), xxxx. https://doi.org/10.3390/sXXXXXXX

**BibTeX:**
```bibtex
@article{rezaie2025thermal,
  author    = {Rezaie, A. and Hay, G. J.},
  title     = {The Past, Present and Future of Thermal Remote Sensing},
  journal   = {MDPI Sensors},
  year      = {2025},
  volume    = {25},
  publisher = {MDPI},
  doi       = {10.3390/sXXXXXXX},
  url       = {https://doi.org/10.3390/sXXXXXXX},
}
```

---

## License

Data compiled from public sources. Released under **CC BY 4.0**. Original sources (WMO OSCAR, ESA eoPortal, NASA Earthdata, agency mission pages) retain their own licenses; please cite them when using specific values.

---

## Contributing

Open an issue or pull request if you spot an error or a missing sensor. For corrections, please include a source URL. For new sensors, confirm at least one band in 3–15 µm from a primary source.
