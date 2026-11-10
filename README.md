# TIR-Review

Spaceborne thermal infrared (TIR) instrument and satellite inventory accompanying:

> Rezaie, H. & Hay, G. J. (2026). *The Past, Present and Possible Future of Thermal Remote Sensing.* Remote Sensing.

**Version 1.1.** Status of every record is fixed at the audit date, **18 August 2026**.

| | v1.1 |
|---|--:|
| Instrument designs | 185 |
| Platform deployments (one per satellite, or per payload hosted on the ISS) | 391 |
| Instrument–deployment links | 543 |
| Operational on 18 August 2026 | 83 |
| Unresolved status | 5 |

## Files

| Path | Contents |
|---|---|
| `sensors/sensors_tir.csv` (+ `.json`) | one row per instrument design, with specification sources |
| `satellites/satellites_tir.csv` (+ `.json`) | one row per platform deployment, with status sources and dates |
| `excluded_records.csv` (+ `.json`) | records removed or merged, and candidates not included, with the reason |
| `DATA_DICTIONARY.md` | fields, allowed values, counting rules, missing values, partial dates and figure definitions |
| `scripts/calculate_figures.py` | checks the data rules and calculates the totals and the tables behind Figures 12 and 17 |
| `results/` | `figure12_operational_by_year.csv`, `figure17_sampling_records.csv` |
| `CHANGELOG.md` | what changed between versions, including how the totals were revised |

The CSV files are authoritative; the JSON files are generated from them with `python scripts/csv_to_json.py`.

## Reproduce the figures

```bash
pip install -r requirements.txt
python scripts/calculate_figures.py --out results/
```

## Licence

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (`LICENSE-DATA`). Code: see `LICENSE`.

Please cite the article and the dataset version you used (see `CITATION.cff`).
