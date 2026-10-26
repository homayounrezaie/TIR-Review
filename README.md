# TIR-Review: spaceborne thermal infrared instrument inventory

Inventory of spaceborne thermal infrared (TIR) instrument designs and the satellite platforms that carried them. It supports the review:

> Rezaie, H. & Hay, G. J. (2026). *The Past, Present and Possible Future of Thermal Remote Sensing.* Remote Sensing (MDPI).

> [!IMPORTANT]
> **v1.0 is not yet released.** The audited data give 185 designs, 391 platform deployments and 83 deployments operational on 18 August 2026. Manuscript v7 reports 174, 306 and 55. `scripts/reproduce_paper_numbers.py` therefore fails, by design, until the two are reconciled. See [`VALIDATION_REPORT.md`](VALIDATION_REPORT.md).

## Scope

**Thermal infrared** here means the two atmospheric windows used for surface observation:

- **MWIR**: mid-wave infrared, about 3–5 µm
- **LWIR**: long-wave infrared, about 8–14 µm

An instrument is included if it (i) was carried on a satellite or the International Space Station, (ii) has at least one MWIR or LWIR channel and (iii) has a design documented by a primary source. Imagers, multichannel radiometers and atmospheric sounders are included and labelled by primary observational purpose. Excluded: non-imaging broadband radiometers (e.g. Explorer 7, ERBE), instruments whose infrared channels all lie outside both windows, airborne instruments, and classified or undocumented systems. Full rules: [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md).

- **Spaceborne inventory:** systematic within these criteria, compiled from WMO OSCAR/Space, agency/operator documentation and peer-reviewed instrument papers, using **English-language sources**. Designs documented in OSCAR but not yet included are listed in `VALIDATION_REPORT.md` §9.
- **Airborne, drone and terrestrial systems** are discussed in the paper through representative examples. They are **not** inventoried here, and that coverage is non-exhaustive.
- Statuses describe conditions on the **audit date, 18 August 2026**.

## Contents

| Path | What it is |
|---|---|
| `sensors/sensors_tir.csv` (`.json`) | One row per **instrument design**: channels, native and product sampling, specification source |
| `satellites/satellites_tir.csv` (`.json`) | One row per **platform deployment** (a satellite or the ISS carrying an included design): dates, status on 18 Aug 2026, status source |
| `excluded_records.csv` | Records removed or merged, each with the reason and source |
| `DATA_DICTIONARY.md` | Every field, its units and allowed values, and the decision rules |
| `VALIDATION_REPORT.md` | Totals reproduced (yes/no), unresolved records, changes, and disagreements with the manuscript |
| `scripts/reproduce_paper_numbers.py` | Recomputes the paper's numbers from the CSVs and fails if any differs |
| `scripts/csv_to_json.py` | Regenerates the JSON files from the CSVs (CSVs are authoritative) |
| `figures/` | Legacy figures from pre-v1.0 data; not used in the manuscript |

### Status categories (on 18 August 2026)

| Status | Meaning |
|---|---|
| `operational` | in orbit and delivering data (instrument operation, not public data availability) |
| `commissioning` | launched, not yet declared operational |
| `planned` | approved or scheduled by an agency, not yet launched |
| `proposed` | announced by a provider but not formally approved |
| `retired` | ended after normal operation |
| `failed` | lost at launch or before delivering usable data |

`retired` + `failed` = *historical* in the paper's figures.

### Spatial sampling
`native_sampling_m` is the finest nominal sampling at nadir among a design's **MWIR/LWIR** channels, using native rather than product sampling. Resampled or sharpened product grids are stored separately in `product_sampling_m`, and provider-reported values are flagged in `value_type`. These values describe pixel spacing, not radiometric performance.

## Reproduce the paper's numbers

```bash
python -m pip install -r requirements.txt
python scripts/reproduce_paper_numbers.py              # checks totals, Figure 12 and Figure 17
python scripts/reproduce_paper_numbers.py --out results/   # also writes the figure tables as CSV
python scripts/csv_to_json.py --check                  # confirms JSON matches CSV
```

The script prints each check as `OK` or `FAIL` and exits with status 1 if any total, the 2024 operational count, or the Figure 17 endpoints differ from the manuscript.

## How to cite

Please cite the article and the dataset version (see [`CITATION.cff`](CITATION.cff)):

> Rezaie, H. & Hay, G. J. (2026). *The Past, Present and Possible Future of Thermal Remote Sensing.* Remote Sensing.
> Rezaie, H. & Hay, G. J. (2026). *Spaceborne thermal infrared instrument and platform inventory*, version 1.0. https://github.com/homayounrezaie/TIR-Review

## Licence

- **Data** (`sensors/`, `satellites/`, `excluded_records.csv` and the documentation): [CC BY 4.0](LICENSE-DATA)
- **Code** (`scripts/`): MIT

See [`LICENSE`](LICENSE).

## Contact

Homayoun Rezaie, Department of Geography, University of Calgary: homayoun.rezaie@ucalgary.ca. Corrections with a source are welcome as GitHub issues.
