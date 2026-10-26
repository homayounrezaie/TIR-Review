# Data dictionary

This inventory supports Rezaie & Hay, *The Past, Present and Possible Future of Thermal Remote Sensing* (Remote Sensing, 2026). It has two linked tables:

| File | Unit of record |
|---|---|
| `sensors/sensors_tir.csv` (+ `.json`) | one **instrument design** |
| `satellites/satellites_tir.csv` (+ `.json`) | one **platform deployment**: one satellite (or the ISS) carrying at least one included design |
| `excluded_records.csv` | records removed from the inventory, with the rule that excluded them |

The JSON files are generated from the CSVs (`python scripts/csv_to_json.py`) and must not be edited by hand.

**Audit date:** 18 August 2026. All statuses describe conditions on that date.

---

## Decision rules

### 1. Inclusion
An instrument is included if it

1. was carried on a satellite or the International Space Station (ISS);
2. has at least one channel in the **MWIR window (about 3–5 µm)** or the **LWIR window (about 8–14 µm)**; and
3. has a design documented by a primary source (agency or operator documentation, WMO OSCAR/Space, or a peer-reviewed instrument paper).

Imagers, multichannel radiometers and atmospheric sounders are included and labelled by primary observational purpose (`primary_purpose`). Instruments that also carry sounding channels outside the two windows are included when they observe in at least one of them.

Excluded:

- non-imaging or broadband radiation-budget radiometers without a discrete MWIR/LWIR channel (e.g. the Explorer 7 radiometer, ERBE);
- instruments whose only infrared channels lie outside both windows (e.g. 15 µm CO₂ pressure-modulated radiometers such as SSU and PMR);
- airborne instruments;
- classified and undocumented instruments.

A channel counts as MWIR if its central wavelength lies in 3.0–5.0 µm, and as LWIR if it lies in 8.0–14.0 µm. A channel reported only as a spectral range counts if the range overlaps either window.

Excluded records are moved to `excluded_records.csv` with the reason; nothing is deleted silently.

### 2. Units of record
- **One record per named instrument design.** A modified instrument is a *new* design when its thermal channel set or detector changed (e.g. AVHRR/1 → AVHRR/2, which added a second LWIR channel). Two observing modes of one instrument are one design (e.g. TES limb and nadir).
- **One record per satellite carrying an included design** (a platform deployment). A spacecraft that was relocated or renamed during its life (e.g. Meteosat-7 → Meteosat-7 IODC, GOES-13 → EWS-G1) is one deployment; the other names are kept in `alt_names`.

### 3. Duplicates and naming
Records drawn from different catalogues were matched by instrument name, operator, platform and launch date, and duplicates were merged. Alternative names are kept in `alt_names`. Each instrument and satellite is listed under the name used in its most recent agency/operator documentation (for WMO-documented systems, the OSCAR/Space acronym).

### 4. Status on the audit date
Exactly one of six values, assigned from the most recent agency, operator or mission source:

| Value | Meaning |
|---|---|
| `operational` | in orbit and the thermal instrument(s) delivering data |
| `commissioning` | launched, not yet declared operational |
| `planned` | approved or scheduled by an agency, not yet launched |
| `proposed` | announced by a provider but not formally approved |
| `retired` | ended after normal operation |
| `failed` | lost at launch or before delivering usable data |

`retired` + `failed` are reported together as **historical** in the paper's figures. There is no `unknown` value.

Clarifications:

- *Operational* refers to instrument operation and data delivery, **not** to public data availability (commercial and defence data count).
- A deployment with several included instruments is operational while **any** of them still delivers thermal data. Instruments that stopped earlier, and payloads delivering thermal data with reduced functionality, are described in `notes`.
- A spacecraft held in on-orbit storage or stand-by and not delivering data on the audit date is `retired`, with `end_date` set to the date its operational service ended, and the stand-by state recorded in `notes`. (The six-category scheme has no separate stand-by value.)
- Commercial missions not yet launched are `proposed` unless an agency approved or scheduled them.
- Sources accessed after the audit date are used **only** to document conditions on the audit date (e.g. a later page that dates an event before 18 August 2026). Events after the audit date are ignored for status but may be mentioned in `notes`.

### 5. Spatial sampling
`native_sampling_m` is the **finest nominal sampling at nadir among the design's MWIR and LWIR channels**, using native rather than product sampling where they differ. Values follow the terminology of the cited source (ground sampling distance, IFOV footprint or "resolution at s.s.p."), which is recorded in `notes` where it matters. Visible, NIR and SWIR channels are never used.

- Product, resampled or sharpened grids go in `product_sampling_m`, never in `native_sampling_m`.
- Provider-reported values (commercial operators) are marked `value_type = provider-reported`.
- Limb and solar-occultation sounders have no nadir sampling; `native_sampling_m` is empty with a note.
- For non-square pixels, the larger dimension is recorded and both are given in `notes`.

---

## `sensors/sensors_tir.csv`

| Field | Type / units | Meaning | Allowed values |
|---|---|---|---|
| `acronym` | text | Unique design identifier, as named in the most recent agency/operator documentation. Referenced by `satellites.tir_sensors`. | unique |
| `full_name` | text | Full instrument name. | |
| `alt_names` | JSON list | Other names under which the design appears in catalogues or the literature. | |
| `agency` | text | Providing agency or operator. | |
| `primary_purpose` | category | Primary observational purpose. | `surface imaging`, `sounding`, `radiometry`, `other` |
| `thermal_bands_um` | JSON list of text | MWIR/LWIR channels as reported by `spec_source` (centre, or lower–upper limit, in µm). Channels outside both windows are omitted. | |
| `n_thermal_bands` | integer | Number of MWIR/LWIR channels. For interferometers and spectrometers, the number of spectral bands reported by the source that overlap the windows. | ≥ 1, or empty |
| `native_sampling_m` | number, metres | Finest nominal native sampling at nadir among MWIR/LWIR channels (rule 5). | > 0, or empty |
| `product_sampling_m` | number, metres | Grid of the distributed thermal product where it differs from native sampling. | > 0, or empty |
| `value_type` | category | Nature of `native_sampling_m`. | `specified` (agency/design specification), `measured` (on-orbit characterisation), `provider-reported` (commercial operator statement), `sharpened` (only when no native value exists) |
| `swath_km` | number, km | Nominal swath width, where the spec source gives one. | |
| `revisit_days` | number, days | Nominal single-satellite revisit/repeat, where the spec source gives one. | |
| `cooled` | category | Detector cooling, where the spec source states it. | `cryogenic` (active cryocooler), `passive_radiative`, `uncooled`, or empty |
| `spec_source` | URL(s) | Source(s) of the specification values, separated by `; `. | required |
| `spec_access_date` | ISO date | Date `spec_source` was accessed. | |
| `confidence` | category | `high`: values stated explicitly for the thermal channels in an agency/OSCAR/peer-reviewed source; `medium`: values from a summary statement, a planned design, or a single provider source; `low`: the source flags the information as provisional or incomplete. | `high`, `medium`, `low` |
| `notes` | text | Ambiguities, judgement calls, merged records. | |

## `satellites/satellites_tir.csv`

| Field | Type / units | Meaning | Allowed values |
|---|---|---|---|
| `name` | text | Platform name as in the most recent agency/operator documentation (OSCAR acronym where available). | unique |
| `alt_names` | JSON list | Other names, including relocation/renamed-mission records merged into this one. | |
| `operator` | text | Operating agency or company. | |
| `country` | text | Country (or organisation, e.g. ESA, EUMETSAT) of the operator. | |
| `launch_date` | ISO date, partial allowed | Launch date: `YYYY-MM-DD`, `YYYY-MM` or `YYYY` as precise as the source. For planned missions, the scheduled date; empty if none is fixed. | |
| `operational_start` | ISO date, partial allowed | Date the thermal instrument(s) started delivering data (end of commissioning), where the source gives it. | |
| `end_date` | ISO date, partial allowed | Date thermal data delivery ended (for `retired`/`failed`). Empty for active or future deployments. | |
| `status_2026_08_18` | category | Status on the audit date (rule 4). | `operational`, `commissioning`, `planned`, `proposed`, `retired`, `failed` |
| `status_source` | URL(s) | Source(s) used to assign status and dates, separated by `; `. | required |
| `status_access_date` | ISO date | Date `status_source` was accessed. | |
| `tir_sensors` | JSON list | `acronym`s of included designs carried. | each must exist in `sensors` |
| `orbit_type` | text | Orbit as given by the source (e.g. `Sunsynchronous orbit`, `Geostationary orbit`, `ISS`). | |
| `primary_purpose` | text | Main mission of the platform as described by the source. | |
| `notes` | text | Instrument-level status differences, reduced functionality, stand-by, data-quality caveats. | |

---

## Figure definitions used by `scripts/reproduce_paper_numbers.py`

- **Operational deployments per year (Figure 12):** a deployment counts in year *Y* if it was operational on 31 December of *Y*: from the year of `operational_start` (or `launch_date` if no separate start is recorded) up to, but not including, the year of `end_date`. For the audit year (2026), the count is the number of deployments with `status_2026_08_18 = operational`. Failed, planned, proposed and commissioning deployments never count.
- **Successive records in native sampling (Figure 17):** each design is placed at the launch date of its first deployment that was launched and not `failed` (i.e. one that delivered data); a design sets a record when its `native_sampling_m` is strictly finer than every earlier design's.
