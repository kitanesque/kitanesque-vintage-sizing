# Changelog

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
