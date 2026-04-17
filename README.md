# Thermal Infrared Satellite Sensors Database

A curated, open dataset of every space-borne sensor that observes Earth in the mid-wave infrared (MWIR, 3–6 µm) and long-wave infrared (LWIR, 6–15 µm). Built from WMO OSCAR, ESA eoPortal, agency mission pages, and peer-reviewed ATBDs.

This dataset accompanies the review paper:

> Rezaie, H., & Hay, G. J. (2026). The past, present and future of thermal remote sensing. *MDPI Remote Sensing*, 25(x), xxxx. https://doi.org/10.3390/sXXXXXXX

---

## Dataset at a glance

| Metric | Value |
|---|---|
| TIR sensors | **167** |
| Satellites carrying them | **288** |
| Space agencies represented | **36** |
| Temporal span | **1964 – 2050** |
| Sensors with full band tables | **167 / 167 (100%)** |
| Sensors with spatial resolution | 162 / 167 (97%) |
| Sensors with swath | 92 / 167 (55%) |
| Operational sensors | 47 |
| Planned / future sensors | 14 |
| Historical (retired) sensors | 80 |
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
| Whiskbroom | 68 |
| Pushbroom | 31 |
| Conical | 8 |
| Limb / limb occultation | 13 |
| Staring / nadir | 11 |
| Spin-scan (GEO) | 5 |
| FTS / interferometer | 3 |
| Other | 28 |

### By orbit type

| Orbit | Count |
|---|---|
| Sun-synchronous (SSO) | 127 |
| Geostationary (GEO) | 30 |
| LEO non-sun-synchronous | 5 |
| ISS | 1 |
| HEO | 1 |
| Airborne | 2 |

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
| CAST | 4 |
| OroraTech | 3 |

---

## Files

| File | Rows | Description |
|---|---|---|
| `sensors_tir.json` | 167 | One record per TIR sensor. Primary view — includes full `thermal_bands` sub-array. |
| `sensors_tir.csv` | 167 | Flat CSV of the same data; `thermal_bands` serialised as JSON string. |
| `satellites_tir.json` | 288 | One record per satellite, with orbital parameters and sensor lists. |
| `satellites_tir.csv` | 288 | Flat CSV version of the satellite view. |

---

## Sensor schema (`sensors_tir.json`)

Each element of the top-level array is a sensor record:

```jsonc
{
  // ── Identity ──────────────────────────────────────────────
  "acronym":          "MODIS",
  "full_name":        "Moderate Resolution Imaging Spectroradiometer",
  "agency":           "NASA",
  "oscar_link":       "https://space.oscar.wmo.int/instruments/view/modis",

  // ── Instrument characteristics ────────────────────────────
  "instrument_type":  "Multi-purpose imaging Vis/IR radiometer",
  "spectral_type":    "MWIR+LWIR",     // "MWIR" | "LWIR" | "MWIR+LWIR"
  "scanning_technique": "whiskbroom",
  "cooled":           "cryogenic",     // "cryogenic" | "passive_radiative" | "uncooled" | "unknown"

  // ── Geometry ──────────────────────────────────────────────
  "spatial_resolution_m": 1000,        // Native IFOV at nadir, metres (1–500 000)
  "swath_km":         2330,            // Cross-track swath, km (null for sounders/limb)
  "orbit_type":       "SSO",           // "SSO" | "GEO" | "LEO_non-SSO" | "HEO" | "ISS"

  // ── Spectral bands (TIR channels only) ────────────────────
  "no_of_bands_total":    36,
  "no_of_thermal_bands":  16,
  "thermal_bands": [ { ... } ],        // See sub-schema below

  // ── Operational timeline ──────────────────────────────────
  "usage_from":   1999,                // First year in operation
  "usage_to":     null,                // Last year (null = still operational)
  "status":       "operational",       // "operational" | "historical" | "planned" | "unknown"

  // ── Platform links ────────────────────────────────────────
  "satellites":   ["Terra", "Aqua"],

  // ── Data quality ──────────────────────────────────────────
  "data_quality": "complete",          // "complete" | "incomplete" | "needs_review"
  "notes":        null,
  "additional_sources": ["https://..."]
}
```

### `thermal_bands` sub-schema

Each element describes one spectral channel:

```jsonc
{
  "band_id":      "B31",          // Short identifier
  "center_um":    11.03,          // Centre wavelength, µm
  "bandwidth_um": 0.50,           // Passband width (FWHM), µm
  "range_um":     [10.78, 11.28], // [lower, upper] wavelength, µm
  "region":       "LWIR",         // "MWIR" (3–6 µm) or "LWIR" (6–15 µm)
  "purpose":      "Cloud top temperature / SST",
  "nedt":         0.05            // Noise-equivalent ΔT, K (null if unknown)
}
```

> **Note on hyperspectral sensors:** AIRS (2378 channels), CrIS (1305), IASI (8461), and IASI-NG are stored as 2–3 representative spectral intervals rather than individual channel tables. Full channel lists are available in the respective instrument ATBDs.

---

## Satellite schema (`satellites_tir.json`)

```jsonc
{
  "name":             "Terra",
  "alt_names":        ["EOS-AM-1"],
  "operator":         "NASA",
  "country":          "USA",

  "orbit_type":       "SSO",
  "altitude_km":      705,
  "inclination_deg":  98.2,
  "period_min":       99.0,
  "mass_kg":          5190,

  "launch_date":      "1999-12-18",   // ISO-8601
  "decommission_date": null,
  "status":           "operational",

  "tir_sensors":      ["MODIS", "ASTER", "CERES"],  // Sensors present in this dataset
  "all_sensors":      ["MODIS", "ASTER", "CERES", "MOPITT", "MISR"],

  "sources":          ["https://..."],
  "notes":            null
}
```

---

## Scope

### Included

- Thermal imagers — whiskbroom, pushbroom, staring arrays with bands in 3–15 µm
- VIS/IR multi-spectral sensors with at least one confirmed thermal channel (AVHRR, MODIS, Landsat TM/ETM+/TIRS, AHI, SEVIRI, …)
- Nadir-pointing hyperspectral IR sounders (AIRS, CrIS, IASI, IASI-NG, …)
- Limb sounders with TIR bands (MIPAS, ACE-FTS, HALOE, LIMS, SAMS, …)
- Commercial / new-space TIR sensors (SatVu HOTSAT, OroraTech FOREST, constellr HiVE, Albedo Clarity, …)
- Future / planned sensors (TRISHNA, SBG-TIR, LSTM, Landsat Next, MTG-I/S, MetOp-SG, JPSS-3/4, FY-3G/H, GOSAT-GW, …)

### Excluded (38 sensors filtered out)

| Category | Count | Examples |
|---|---|---|
| Solar irradiance monitors | 20 | ACRIM I/II/III, TIM, VIRGO, PREMOS |
| Passive microwave radiometers | 17 | AMSR, AMSR-E, AMSR2, GMI, CIMR, SMMR, Delta-2D, SHF |
| Active microwave (SAR / scatterometer) | 1 | AMI |
| Pure VIS/NIR/SWIR (no TIR band confirmed) | 1 | CZCS |

---

## Data quality

Every record carries a `data_quality` tag:

| Tag | Meaning | Count |
|---|---|---|
| `complete` | All five tier-1 fields populated and cross-validated | 52 |
| `incomplete` | One or more tier-1 fields still `null` after checking all sources | 115 |
| `needs_review` | Provisional values from secondary sources | ~5 |

**Tier-1 fields:** `thermal_bands`, `spatial_resolution_m`, `swath_km`, `scanning_technique`, `orbit_type`.

Field coverage summary:

| Field | Coverage |
|---|---|
| thermal_bands | 167 / 167 (100%) |
| scanning_technique | 167 / 167 (100%) |
| orbit_type | 167 / 167 (100%) |
| spatial_resolution_m | 162 / 167 (97%) |
| swath_km | 92 / 167 (55%) |

`swath_km` is the main gap: limb sounders have no meaningful swath, and many historical sensors have no published value.

---

## Quick start

### Load and filter sensors

```python
import json

with open("sensors_tir.json") as f:
    sensors = json.load(f)

# All operational LWIR sensors with sub-100 m resolution
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

# Sensor count by agency
print(df.groupby("agency")["acronym"].count().sort_values(ascending=False).head(10))

# Sensors launched per decade
df["decade"] = (df["usage_from"] // 10 * 10).astype("Int64")
print(df.groupby("decade")["acronym"].count())
```

### Query thermal bands

```python
import json

with open("sensors_tir.json") as f:
    sensors = json.load(f)

# Sensors with a split-window channel near 11 µm
def has_band_near(s, center, tol=0.5):
    return any(
        abs((b.get("center_um") or 0) - center) <= tol
        for b in (s.get("thermal_bands") or [])
    )

window = [s["acronym"] for s in sensors if has_band_near(s, 11.0)]
print(f"{len(window)} sensors have a channel near 11 µm")
```

### Planned sensors timeline

```python
import json

with open("sensors_tir.json") as f:
    sensors = json.load(f)

planned = sorted(
    [s for s in sensors if s["status"] == "planned"],
    key=lambda x: x.get("usage_from") or 9999
)
for s in planned:
    print(f"{s.get('usage_from','?')}  {s['acronym']:<20}  {s.get('agency','?')}")
```

---

## Data sources

Records were built by merging the following sources in descending priority:

1. [WMO OSCAR/Space](https://space.oscar.wmo.int/) — spectral ranges, IFOV, swath, orbit, agency
2. Instrument ATBDs and user guides — authoritative band tables for hyperspectral sounders
3. [ESA eoPortal](https://www.eoportal.org/) — mission overviews and updated specifications
4. [CEOS EO Handbook](https://database.eohandbook.com/) — cross-checks for scanning technique, orbit, status
5. [NASA Earthdata](https://www.earthdata.nasa.gov/) — NASA instruments and satellites
6. Agency mission pages (NOAA, ESA, JAXA, JMA, CMA, CNES, ISRO, CSA, UKSA, EUMETSAT, Roscosmos)
7. [Gunter's Space Page](https://space.skyrocket.de/) — satellite launch dates, mass, orbital parameters
8. Manufacturer datasheets — commercial new-space sensors

---

## Known limitations

- **swath_km** is missing for ~45% of sensors: limb sounders have no swath; many historical instruments have no published value.
- **cooled** is unknown for 44% of sensors (older OSCAR records do not specify detector technology).
- **Hyperspectral band entries** are representative: AIRS, CrIS, IASI, IASI-NG store 2–3 spectral intervals instead of thousands of individual channels.
- **Commercial new-space sensors** have limited public spectral documentation; band entries marked `needs_review` are derived from product datasheets.

---

## How to cite

**APA:**
> Rezaie, H., & Hay, G. J. (2026). The past, present and future of thermal remote sensing. *MDPI Remote Sensing*, *25*(x), xxxx. https://doi.org/10.3390/sXXXXXXX

**BibTeX:**
```bibtex
@article{rezaie2026thermal,
  author    = {Rezaie, H. and Hay, G. J.},
  title     = {The Past, Present and Future of Thermal Remote Sensing},
  journal   = {MDPI Remote Sensing},
  year      = {2026},
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

Open an issue or pull request if you spot an error or a missing sensor. For corrections, include a source URL. For new sensors, confirm at least one band in 3–15 µm from a primary source.
