# Changelog

## 2026-11-22 — version 3

Same dataset, same concept DOI (10.5281/zenodo.23452245), same Hugging Face repository (`kitanesque/kitanesque-vintage-sizing`), same Kaggle dataset (`andradalcaran/vintage-clothing-sizing-label-vs-tape`), same GitHub repository (`kitanesque/kitanesque-vintage-sizing`). Version DOI on Zenodo: 10.5281/zenodo.24443705. Previous version: 2026-10-26, DOI 10.5281/zenodo.23674846.

**Files: six, the same as the previous version.** 1642 rows in all (was 1378 on 2026-10-26; 264 added). Pieces listed, measured and sold since the previous snapshot are added; nothing was renamed or removed.

| File | 2026-10-26 | 2026-11-22 |
|---|---|---|
| jeans | 108 rows | 139 rows |
| knitwear | 106 rows | 123 rows |
| dress | 55 rows | 56 rows |
| rise | 112 rows | 143 rows |
| labels | 439 rows | 517 rows |
| garments | 558 rows | 664 rows |

**Columns.** Unchanged since 2026-10-26 (see `data_dictionary.md`). `make_snapshot.py` checks every live header against the documented one and stops before writing anything when a header changes; a snapshot that needed `--force` has a note about the change written here by hand.

**Rise bands (10 November 2026).** `rise_band` in the front-rise file now follows the one scale used across the website: ultra-low under 7 in, low 7 in to under 8.5 in, mid 8.5 to 10.5 in, high over 10.5 in. Until the snapshot of 2026-10-26 mid ended under 10 in and high started at 10 in, so pairs measured at 10 and 10.5 in moved from `high` to `mid`; no measurement changed and the column name is the same.

**label_waist (22 November 2026).** In the jeans and front-rise files `label_waist` now holds a value only when a W number is printed on the label (53 of the 139 pairs of jeans). For brands that size in US, junior or European numbers (Maurices „US 7”, Wallflower „13 Reg”, C&A „EU42” and others) the W in our listing title is the waist we measured, not the label; until the snapshot of 2026-10-26 those rows carried that measured waist as `label_waist`, so their waistband equalled the „label” to the inch. Those rows, and rows whose label size is not on record, are now blank. No measurement changed; the label-against-tape figures in the description are computed on the rows with a printed W only.

**Collection window.** Listings from 2026-08-29 to 2026-11-22 (previous version: see below).

**Made with** `src/tools/datasets/publish_snapshot.py` (snapshot → Zenodo new version → Hugging Face commit → Kaggle version), package `pr/datasets-2026-11-22/`.

## 2026-10-26 — version 2

Same dataset, same concept DOI (10.5281/zenodo.23452245), same Hugging Face repository (`kitanesque/kitanesque-vintage-sizing`), same Kaggle dataset (`andradalcaran/vintage-clothing-sizing-label-vs-tape`), same GitHub repository (`kitanesque/kitanesque-vintage-sizing`). New version DOI on Zenodo: 10.5281/zenodo.23674846.

**Title.** *Kitanesque vintage sizing and labels: tape measurements and label data for second-hand clothing* (was *Kitanesque vintage sizing: label sizes against tape measurements for second-hand jeans and knitwear*). The old title no longer described the contents; the first version keeps its own title on Zenodo.

**Files: two → six.** 1378 rows in all (was 198).

| File | v1 (2026-10-18) | v2 (2026-10-26) | Change |
|---|---|---|---|
| jeans | 94 rows | 108 rows | same 12 columns; pairs listed since 18 Oct added, nothing removed |
| knitwear | 104 rows | 106 rows | same 11 columns; pieces listed since 18 Oct added |
| dress | — | 55 rows | **new**: women's dresses, bust/waist/hips round against the UK standard for the listed size, length, decade, stretch flag |
| rise | — | 112 rows | **new**: the front rise of every measured pair of jeans with the shop's rise band (ultra-low / low / mid / high), label waist, waistband, inside leg, era |
| labels | — | 439 rows | **new**: what the brand and care labels print (country, fibre composition, care wording, printed sizes, RN/CA numbers with registrants and brand match, number of label photographs), read by OCR from the listing photographs |
| garments | — | 558 rows | **new**: every garment measurement in the catalogue in one table (bust, waist, hips flat and round, length, sleeve, front rise, inside leg, give, material, listed size, era, cut), accessories left out |

**Naming.** `rise_in` (jeans) is the same measurement as `front_rise_in` (rise, garments); `era` (jeans, rise, labels, garments) and `decade` (dress) are the same field; `listed_uk_size` is a bare number or range (`8`, `8-10`) in jeans, knitwear, dress and rise, while `listed_size` in garments carries the prefix (`UK 8`, `UK 8-10`) or a non-UK size term (`W26`, `M`). Nothing was renamed between versions; the differences are between files, as the website writes them.

**Documentation.** `data_dictionary.md` covers the six files and the UK size table behind every `uk_standard_*` column. `README.md` (Hugging Face card) has six configs. `CITATION.cff` now carries the author's ORCID (0009-0002-7786-6702) and the version DOI. `make_snapshot.py` fetches six files, checks each header against the documented one, and writes `counts.json`; `fill_counts.py` pours the counts into the texts.

**Collection window.** Listings from 2026-08-29 to 2026-10-24 (v1: 2026-08-29 to 2026-10-14).

## 2026-10-18 — version 1

First release: 94 pairs of jeans and 104 women's knitted pieces, measured flat by hand, label size against the tape. Zenodo (version DOI 10.5281/zenodo.23452246; concept DOI 10.5281/zenodo.23452245), Hugging Face, Kaggle, GitHub. Package: `pr/datasets-2026-10-18/`.
