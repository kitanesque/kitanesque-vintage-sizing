---
license: cc-by-4.0
language:
- en
pretty_name: "Kitanesque vintage sizing and labels: tape measurements and label data for second-hand clothing"
size_categories:
- 1K<n<10K
tags:
- fashion
- clothing
- sizing
- size-chart
- vintage
- second-hand
- denim
- jeans
- low-rise
- knitwear
- cashmere
- dresses
- clothing-labels
- care-labels
- rn-number
- country-of-origin
- measurements
- tabular
- uk
- open-data
configs:
- config_name: jeans
  data_files: data/kitanesque-vintage-jeans-measurements-2026-10-26.csv
  default: true
- config_name: knitwear
  data_files: data/kitanesque-vintage-knitwear-measurements-2026-10-26.csv
- config_name: dress
  data_files: data/kitanesque-vintage-dress-measurements-2026-10-26.csv
- config_name: rise
  data_files: data/kitanesque-vintage-rise-measurements-2026-10-26.csv
- config_name: labels
  data_files: data/kitanesque-vintage-labels-measurements-2026-10-26.csv
- config_name: garments
  data_files: data/kitanesque-vintage-garments-measurements-2026-10-26.csv
---

# Kitanesque vintage sizing and labels: tape measurements and label data for second-hand clothing

Six tables, 1378 rows, from the stock of Kitanesque, an independent online vintage shop in the UK. Every garment was measured by hand, laid flat, before it was listed for sale, and every label that could be read was photographed and read. The tables set what the label says (a W number, a UK size, a fibre, a country, an RN number) against what the tape measure and the public registers say.

This is version 2026-10-26. The first version (2026-10-18) had two tables, jeans and knitwear. This one adds dresses, the front rise of every pair of jeans, the labels, and one table with every garment measurement in the catalogue.

- **Live versions, rebuilt as pieces are listed and sold:** [Jeans sizing by brand](https://kitanesque.co.uk/jeans-sizing-by-brand/) · [Knitwear sizing by brand](https://kitanesque.co.uk/knitwear-sizing-by-brand/) · [Dress sizing by brand](https://kitanesque.co.uk/dress-sizing-by-brand/) · [What counts as low-rise](https://kitanesque.co.uk/what-counts-as-low-rise/) · [Date vintage clothing by its label](https://kitanesque.co.uk/date-vintage-clothing-by-label/) · [Size guide](https://kitanesque.co.uk/size-guide/) · all of them on [Guides & data](https://kitanesque.co.uk/guides/)
- **Shop:** [kitanesque.co.uk](https://kitanesque.co.uk/)
- **Snapshot date:** 2026-10-26 · **Licence:** CC BY 4.0 · **DOI:** 10.5281/zenodo.23452245 (all versions)

## What is in it

| Config / file | Rows | What one row is |
|---|---|---|
| `jeans` · `data/kitanesque-vintage-jeans-measurements-2026-10-26.csv` | 108 | One pair of jeans (denim only) with a W size on the label and a measured waistband, from 74 labels. Label waist W23–W37. 67 in stock, 41 sold on the snapshot date. |
| `knitwear` · `data/kitanesque-vintage-knitwear-measurements-2026-10-26.csv` | 106 | One women's knitted piece with a measured bust and a UK size on its listing, from 79 labels (jumper/knit top 64 · cardigan 24 · knit dress 13 · knit vest/top 4 · knit jacket 1). 55 cashmere. 43 in stock, 63 sold. |
| `dress` · `data/kitanesque-vintage-dress-measurements-2026-10-26.csv` | 55 | One women's dress with a measured bust and a UK size on its listing, from 44 labels; 27 of them stretch or wrap dresses, flagged. 27 in stock, 28 sold. |
| `rise` · `data/kitanesque-vintage-rise-measurements-2026-10-26.csv` | 112 | One pair of jeans with a measured front rise and the band it falls in (ultra-low, low, mid, high), with or without a brand or a W label. 69 in stock, 43 sold. |
| `labels` · `data/kitanesque-vintage-labels-measurements-2026-10-26.csv` | 439 | One piece whose brand or care label was photographed and read: country, fibre composition, care wording, sizes printed, RN/CA number with its registrant, number of label photographs. 201 in stock, 238 sold. |
| `garments` · `data/kitanesque-vintage-garments-measurements-2026-10-26.csv` | 558 | One garment with at least one tape measurement: bust, waist and hips flat and round, length, sleeve, front rise, inside leg, with the listed size, era, give, material and cut. 189 tops, 200 bottoms, 75 dresses, 94 outerwear. Accessories left out. 257 in stock, 301 sold. |

Column-by-column definitions are in [`data_dictionary.md`](data_dictionary.md).

**How the tables relate.** The same garment can appear in several tables: a pair of jeans is in `jeans`, `rise` and `garments`, and in `labels` if its label was read; a jumper is in `knitwear` and `garments`. `listing_url` is the same value everywhere and joins them. `rise` is wider than `jeans` (it keeps pairs without a brand or without a W label); `garments` is the widest of the measurement tables; `labels` is independent of the measurements.

## What is measured, and how

- **Girths** (bust, waist, hips): the garment is laid flat and unstretched and measured straight across; the `*_round_in` columns are that number doubled. Bust straight across under the arms; waist across the waistband or the narrowest point; hips across the widest point. In `garments` both the flat number and the doubled one are given; the flat column is blank when the listing gave the measurement round.
- **Lengths:** length from the shoulder seam (or the top of the waistband on bottoms) to the hem; sleeve from the underarm seam to the cuff; front rise from the crotch seam, where the four seams meet, straight up to the top of the waistband; inside leg along the inseam from the crotch seam to the hem.
- **Unit:** inches, as written on the listing, usually to the nearest 0.5 in. Second-hand garments as sold, not as made.
- **The listed size** (`listed_uk_size`, `listed_size`) is the size the piece was sold as, chosen by hand after measuring and trying it on a UK 8 model (5′6″). It is never computed from the label or from a chart. The `uk_standard_*` columns give the body measurement a UK woman of that size is usually made for, from the one size table used across the shop, so garment and standard can be compared.
- **Rise bands** (`rise_band`) are the shop's working bands on the front rise measured flat: ultra-low under 7 in, low 7 to 8 in, mid over 8 and under 10 in, high 10 in and over.
- **Labels** (`labels`): every photograph in the listing gallery was read by optical character recognition, run locally (Apple Vision); country, fibre percentages, sizes, care phrases and RN/CA numbers were parsed from the text with rules. RN numbers were looked up in the US Federal Trade Commission's RN register and CA numbers in the Canadian Competition Bureau's register, and the registrant was compared with the brand on the listing. A reading that disagreed with the listing was flagged for review, never corrected automatically. The columns are facts as printed on the label; none of them is a judgement of authenticity.

## Some numbers from the snapshot

- **Jeans:** on the 108 pairs, the waistband measured from -4 to +6 in against the W number printed on the label; +0.8 in on average. Era tags: 60 Y2K, 3 1990s.
- **Front rise:** across the 112 pairs the median front rise is 8.5 in (lowest 6, highest 12.5); 44 of them at 8 in or under. By band: 6 ultra-low, 38 low, 46 mid, 22 high. Y2K pairs: 64, median 8.5 in.
- **Knitwear:** the bust came out +1.4 in against the UK standard for the listed size on average (106 pieces compared); 28 of them within 1.5 in of it.
- **Dresses:** on the 28 woven dresses the bust came out +0.2 in against the standard on average (28 compared). Stretch or wrap dresses, listed but not compared: 27 (a stretch dress measured flat reads well under the body it is made for). Dresses with a waist measurement as well: 31.
- **Labels:** of the 439 pieces, 248 name a country of manufacture (31 countries), 317 give a fibre composition, 154 carry care wording, 115 a printed size and 97 an RN or CA number. Numbers registered to the brand on the listing: 47; to a different company: 50. 612 label photographs in all.
- **Garments:** 558 pieces from 347 labels; 353 with a bust, 263 with a waist, 20 with hips, 162 with a front rise. Stretch fabrics (knit, jersey), measured unstretched: 193. Cut for women 511, for men 34, unisex 13.

## How it was collected

Kitanesque is a small online shop: one buyer chooses every piece, and one person measures, photographs and lists it. The measurements were written into each listing on kitanesque.co.uk between 29 August 2026 and 24 October 2026 and read back from the listings for these files; the label facts were read from the listing photographs as described above. Sold pieces stay in the data, so the sample does not shrink as stock sells; sold pieces stay online, marked as sold.

## Limitations and biases

- **One shop, one buyer.** Brands and eras reflect what the shop stocks: mostly US and UK labels, with a strong Y2K denim lean and a lot of cashmere. Not a random sample of the market.
- **Mostly women's.** All knitwear and dresses, and most jeans, are women's.
- **Second-hand garments.** Fabric may have stretched or shrunk with wear and washing; measurements describe the garment as sold.
- **Measured flat, by hand.** About ±0.5 in.
- **Label sizes as printed.** W numbers and letter sizes are vanity-sized differently by every brand and era; that difference is the point of the data. The listed size is the one on the listing, which usually but not always matches the label.
- **Small counts per brand.** Most labels appear once or twice.
- **Label reading.** A worn, curled or blurred label can be misread by the OCR, and a percentage can be mis-parsed; `country` is as printed, and a reprinted label can lie. `rn_matches_brand` compares the registrant's name with the brand on the listing, so licensees, parent companies and renamed firms show as `no`.
- **Grouping columns are coarse.** `garment` in `labels` is a word taken from the listing title; `material` in `garments` is the listing's material term, not the label's composition (that is in `labels`).
- **Rise bands** are one shop's working definitions, not an industry standard.
- **Snapshot.** The live files on the website keep changing; these files are fixed at 2026-10-26.

## Versions

| Version | Files | Rows | Where |
|---|---|---|---|
| 2026-10-18 | jeans, knitwear | 198 | Zenodo version 1 under the same concept DOI; the git history of this repository |
| 2026-10-26 | jeans, knitwear, dress, rise, labels, garments | 1378 | this version |

New versions are made every few months (first Monday of January, April, July and October, skipped when fewer than 20 new pieces have been measured). The concept DOI 10.5281/zenodo.23452245 always resolves to the latest version.

## Licence and how to cite

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Free to use, share and adapt, including commercially, with credit and a link back.

> Dălcăran, A. (2026). *Kitanesque vintage sizing and labels: tape measurements and label data for second-hand clothing* (Version 2026-10-26) [Data set]. Kitanesque Ltd. https://doi.org/10.5281/zenodo.23674846

Concept DOI for all versions: https://doi.org/10.5281/zenodo.23452245. A `CITATION.cff` file is included. Please link to [kitanesque.co.uk](https://kitanesque.co.uk/) when you quote the numbers.

## Maintainer

Kitanesque Ltd (company no. 17442810, England and Wales) · [kitanesque.co.uk](https://kitanesque.co.uk/) · hello@kitanesque.co.uk

Measurements and label photographs by Andra Dălcăran, founder of Kitanesque ([ORCID 0009-0002-7786-6702](https://orcid.org/0009-0002-7786-6702)). Corrections and questions are welcome by email.
