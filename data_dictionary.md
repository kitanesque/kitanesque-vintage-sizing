# Data dictionary — Kitanesque vintage sizing and labels, snapshot 2026-10-26

Six CSV files, UTF-8 without byte-order mark, comma-separated, LF line endings, one header row each. An empty cell means not measured, not recorded or not read; it never means zero. Lengths are in inches, as written on the listing: at most one decimal in `jeans`, `knitwear`, `dress` and `rise`, up to two decimals in `garments` (trailing zeros dropped, so `34` not `34.0`).

Every measurement was taken by Andra Dălcăran (Kitanesque Ltd) with the garment laid flat and unstretched, before the piece was listed for sale, and written into the listing. The website reads the numbers back from the listings; nothing in these files is estimated, interpolated or converted, with three documented exceptions: the `uk_standard_*` columns are reference values from a size table, `rise_band` is a banding of the measured rise, and `garment` is a grouping word read from the listing's URL or title. The label facts in `labels` were read from the listing photographs by optical character recognition and parsed by rules; they are what the label prints, not a judgement of authenticity.

Columns shared by every file:

| Column | Meaning |
|---|---|
| `brand` | Brand as listed (the shop's canonical brand term for the piece, normally the first word of the title). Blank in `rise`, `labels` and `garments` when the listing has no brand term; `jeans`, `knitwear` and `dress` leave such pieces out. |
| `in_stock` | `yes` if the piece was for sale on 2026-10-26, `no` if it had sold. Sold pieces are kept so the sample does not shrink as stock sells. |
| `listed_on` | Date the piece was first published on kitanesque.co.uk, `YYYY-MM-DD`. Not a manufacturing date. |
| `listing_url` | The product page. Sold pieces stay online, marked as sold. The same value in every file, so it joins the tables. |

**The UK women's size table** behind every `uk_standard_*` column (body measurements in inches a UK woman of that size is usually made for; the one table used across the shop):

| UK size | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|
| bust | 30.5 | 31.5 | 33 | 35 | 37 | 39 | 41 | 43.5 | 46 | 48.5 |
| waist | 23.5 | 24.5 | 26 | 28 | 30 | 32 | 34 | 36.5 | 39 | 41.5 |
| hips | 33.5 | 34.5 | 36 | 38 | 40 | 42 | 44 | 46.5 | 49 | 51.5 |

For a two-size listing such as `8-10` the standard is the mean of the two (bust 34). Blank when the listed size is outside the table.

## 1. `data/kitanesque-vintage-jeans-measurements-2026-10-26.csv` — 108 rows

One row per pair of jeans: denim (the title says jeans or denim, or the material term does), a waist size printed on the label (W number), a measured waistband, a brand. Shorts (inside leg under 18 in), skirts, dresses, jumpsuits, dungarees, trousers, chinos, cords, skorts and leggings are excluded at the source. Sorted by brand, then label waist, then listing id. Listed 2026-08-29 to 2026-10-24.

| Column | Type | Unit | Meaning |
|---|---|---|---|
| `brand` | string | — | See above. Never blank in this file. |
| `garment` | string | — | `jeans` for every row. The live file has held denim only since 18 Oct 2026; the column is kept for forward compatibility (the snapshot script would write `trousers` or `skort` if such a row ever came through). |
| `label_waist` | string | — | Waist size printed on the label, e.g. `W28`. As printed; US-style W sizes on most pairs. W23 to W37 in this file. |
| `era` | string | — | Decade tag on the listing where known: `Y2K` (roughly 1998–2008), `90s`, `80s`, `70s` or `60s`. Blank = not tagged; it does not mean modern. 60 Y2K and 3 90s in this file. |
| `waistband_round_in` | number | in | Waistband measured straight across the top, laid flat, and doubled. The garment's waistband, not the wearer's waist. Never blank. |
| `rise_in` | number | in | Front rise, from the crotch seam to the top of the waistband. The same measurement is called `front_rise_in` in `rise` and `garments`. Blank when not recorded. |
| `inside_leg_in` | number | in | Inside leg, along the inseam from the crotch seam to the hem. Blank when not recorded. |
| `listed_uk_size` | string | UK women's size | The UK size the pair was listed as, chosen by hand after measuring and a try-on on a UK 8 model (5′6″). Never computed. A range such as `8-10` means it fits across both. Blank when the listing carries no UK size (men's pairs, for instance). |
| `cut_for` | string | — | `women` (106), `men` (1) or `unisex` (1). |
| `in_stock` | string | — | `yes` (67) / `no` (41). |
| `listed_on` | date | YYYY-MM-DD | See above. |
| `listing_url` | url | — | See above. |

## 2. `data/kitanesque-vintage-knitwear-measurements-2026-10-26.csv` — 106 rows

One row per women's knitted piece (jumpers, cardigans, knit dresses, knit vests, knitted jackets) with a measured bust, a UK size on its listing and a brand. Knitted means the title or material says so (jumper, cardigan, knit, crochet…) or, for a roll-neck or V-neck, the fibre is a knitting fibre; sweatshirts, hoodies and fleeces are out, as are woven coats, jackets, shirts, blouses and dresses. Sorted by brand, then listed size, then listing id. Listed 2026-08-29 to 2026-10-24.

| Column | Type | Unit | Meaning |
|---|---|---|---|
| `brand` | string | — | See above. Never blank in this file. |
| `garment` | string | — | `jumper/knit top`, `cardigan`, `knit dress`, `knit vest/top` or `knit jacket`, read from the listing URL by the snapshot script (jumper/knit top 64 · cardigan 24 · knit dress 13 · knit vest/top 4 · knit jacket 1). |
| `listed_uk_size` | string | UK women's size | The UK size on the listing, chosen by hand (see the jeans table). Usually the size on the label; where they disagree, the listing wins. `8-10` = fits both. Never blank in this file. |
| `bust_round_in` | number | in | Bust measured straight across under the arms, laid flat, and doubled. Never blank. |
| `uk_standard_bust_in` | number | in | Reference body bust for `listed_uk_size` from the table above (mean for a range). A reference value, not a measurement. Blank when the size is outside the table. |
| `length_in` | number | in | From the shoulder seam to the hem. Blank when not recorded. |
| `sleeve_in` | number | in | From the underarm seam to the cuff. Blank when sleeveless, short-sleeved or not recorded. |
| `material` | string | — | Main fibre from the listing's material terms, first match in this order: Cashmere, Merino, Lambswool, Alpaca, Mohair, Angora, Wool, Silk, Cotton, Linen, Viscose, Acrylic, Blend. Blank when none of these is on the listing. 55 cashmere in this file. |
| `in_stock` | string | — | `yes` (43) / `no` (63). |
| `listed_on` | date | YYYY-MM-DD | See above. |
| `listing_url` | url | — | See above. |

## 3. `data/kitanesque-vintage-dress-measurements-2026-10-26.csv` — 55 rows

One row per women's dress with a measured bust, a UK size on its listing and a brand, in stock and sold. A dress is what the measurer tagged as a dress, minus jumpsuits, playsuits, rompers, co-ords, two-pieces, skirt sets and trouser suits. Sorted by brand, then listed size, then listing id. Listed 2026-08-29 to 2026-10-24.

| Column | Type | Unit | Meaning |
|---|---|---|---|
| `brand` | string | — | See above. Never blank in this file. |
| `listed_uk_size` | string | UK women's size | The UK size on the listing, chosen by hand after measuring and a try-on. `8-10` = fits both. Never blank in this file. |
| `bust_round_in` | number | in | Bust straight across under the arms, laid flat, doubled. Never blank. |
| `uk_standard_bust_in` | number | in | Reference bust for the listed size (table above). Blank when the size is outside the table. |
| `waist_round_in` | number | in | Waist across the narrowest point, laid flat, doubled. Blank when the dress has no waist to measure (shifts, slips, straight cuts) or it was not recorded. Rows with a value: 31. |
| `uk_standard_waist_in` | number | in | Reference waist for the listed size. Blank whenever `waist_round_in` is blank, or the size is outside the table. |
| `hips_round_in` | number | in | Hips across the widest point of the skirt, laid flat, doubled, where the cut has one. Blank when not measured. Rows with a value: 8. |
| `uk_standard_hips_in` | number | in | Reference hips for the listed size. Blank whenever `hips_round_in` is blank, or the size is outside the table. |
| `length_in` | number | in | From the shoulder seam (or the top of the bodice on a strapless dress) to the hem. Blank when not recorded. |
| `decade` | string | — | Decade on the listing, from its tags or its title: `Y2K`, `00s`, `90s`, `80s`, `70s` or `60s`. Blank when none. Called `era` in the other files. |
| `stretch` | string | — | `yes` for a stretch or wrap dress: the measurer recorded the fabric as stretch (bodycon, ribbed knit, jersey) or the title says bodycon, liquid metal, wet look, stretch, jersey, ribbed, elastane, lycra, spandex or wrap. Such a dress is in the file with its measurements, but the live page never compares it against the standard, because a stretch dress measured unstretched reads well under the body it is made for and a wrap dress has no fixed bust. `no` otherwise. 27 yes, 28 no. |
| `in_stock` | string | — | `yes` (27) / `no` (28). |
| `listed_on` | date | YYYY-MM-DD | See above. |
| `listing_url` | url | — | See above. |

## 4. `data/kitanesque-vintage-rise-measurements-2026-10-26.csv` — 112 rows

One row per pair of jeans (denim, the same test as the jeans file) with a front rise on the tape, in stock and sold; shorts (inside leg under 18 in) are out. Unlike the jeans file, pairs without a brand term or without a W label are kept. Sorted by front rise, lowest first, then listing id. Listed 2026-08-29 to 2026-10-24.

| Column | Type | Unit | Meaning |
|---|---|---|---|
| `brand` | string | — | See above. Blank when the listing has no brand term (3 rows). |
| `label_waist` | string | — | Waist printed on the label, e.g. `W28`. Blank when the label carries no W number. Rows with a value: 111. |
| `era` | string | — | Decade tag on the listing: `Y2K`, `90s`, `80s`, `70s` or `60s`. Blank when not tagged. 64 Y2K in this file. |
| `front_rise_in` | number | in | Front rise, from the crotch seam, where the four seams meet, straight up to the top of the waistband, measured flat and buttoned. Never blank. 6 to 12.5 in this file, median 8.5. |
| `rise_band` | string | — | The shop's working band for that rise: `ultra-low` under 7 in; `low` 7 in to 8 in inclusive; `mid` over 8 in and under 10 in (in practice 8.5–9.5); `high` 10 in and over. A banding of the column to its left, nothing else. 6 / 38 / 46 / 22 in this file. |
| `waistband_round_in` | number | in | Waistband straight across the top, laid flat, doubled. Blank when not recorded. |
| `inside_leg_in` | number | in | Inside leg, crotch seam to hem. Blank when not recorded. |
| `listed_uk_size` | string | UK women's size | The UK size on the listing, chosen by hand; `8-10` = fits both. Blank when the listing has no UK size. |
| `cut_for` | string | — | `women`, `men` or `unisex`, as listed. |
| `in_stock` | string | — | `yes` (69) / `no` (43). |
| `listed_on` | date | YYYY-MM-DD | See above. |
| `listing_url` | url | — | See above. |

## 5. `data/kitanesque-vintage-labels-measurements-2026-10-26.csv` — 439 rows

One row per published piece, in stock and sold, whose brand or care label was photographed and read and gave at least one of: country, fibre composition, care wording, printed size, RN/CA number. Garments and accessories alike. Sorted by brand (pieces without a brand last), then `listed_on`, then listing id. Listed 2026-08-29 to 2026-10-24.

How the reading was done: every photograph in the listing gallery went through optical character recognition run locally (Apple Vision); country, fibre names with percentages, sizes, care phrases and RN/CA numbers were parsed from the text with rules written for the labels seen in the shop (English and the main European label languages). RN numbers were looked up in the US Federal Trade Commission's RN register, CA numbers in the Canadian Competition Bureau's register, and the registrant compared with the brand on the listing. A reading that disagreed with the listing was flagged for review; nothing was corrected automatically. No raw OCR text, prices or confidence scores are in the file.

| Column | Type | Unit | Meaning |
|---|---|---|---|
| `brand` | string | — | See above. Blank when the listing has no brand term (27 rows). |
| `garment` | string | — | A coarse grouping word from the listing title (URL slug as a fallback), first match in this order: `other` (shorts, jumpsuits, swimwear, scarves, belts, hats, gloves…), `bag`, `shoes`, `jacket`, `coat`, `dress`, `skirt`, `cardigan`, `jumper`, `top`, `trousers`, `jeans`; `other` when nothing matches. A grouping, not a classification (a denim jacket is `jacket`, a denim skirt `skirt`). |
| `era` | string | — | Decade on the listing, from its tags or title: `Y2K`, `00s`, `90s`, `80s`, `70s` or `60s`. Blank when none. |
| `country` | string | — | Country of manufacture as printed on the label (after "Made in"), e.g. `Italy`, `Hong Kong`, `the EU`. Blank when no country was read. Rows with a value: 248, naming 31 distinct countries. |
| `composition` | string | — | Fibres and percentages as printed, lower-case fibre names, `; `-separated, e.g. `cotton 98; elastane 2`; the percentage is left off when the label gave none (`cashmere`). Blank when no composition was read. Rows with a value: 317. |
| `care_label` | string | — | Care phrases read from the care tag, `; `-separated, e.g. `wash at 30°; do not tumble dry`. Blank when none. Rows with a value: 154. |
| `label_size` | string | — | Sizes printed on the label, `; `-separated, e.g. `W28; L32`, `UK 10; EU 38`, `M`. What the label says, not the size the piece was listed as. Blank when none was read. Rows with a value: 115. |
| `rn_ca` | string | — | RN (US FTC) or CA (Canada) registration numbers on the label, `; `-separated, e.g. `RN 12345; CA 67890`. Blank when none. Rows with a value: 97. |
| `rn_registrant` | string | — | The registrant of each number as the public register prints it. Blank when there is no number or the register returned nothing. Rows with a value: 97. |
| `rn_matches_brand` | string | — | `yes` when a number on the label is registered to the brand on the listing; `no` when the registrant is known and is a different company (licensees, parent companies and renamed firms show as `no`); blank when there is no number or the registrant is unknown. 47 yes, 50 no. |
| `label_photos` | integer | count | Number of label photographs in the listing gallery (the photographs the facts were read from). 612 in all. |
| `in_stock` | string | — | `yes` (201) / `no` (238). |
| `listed_on` | date | YYYY-MM-DD | See above. |
| `listing_url` | url | — | See above. |

## 6. `data/kitanesque-vintage-garments-measurements-2026-10-26.csv` — 558 rows

One row per published garment with at least one tape measurement on its listing, in stock and sold; accessories (bags, belts, scarves) are out, and so is a record that only has the label sizes and no tape number. Sorted by brand (pieces without a brand last), then garment, then `listed_on`, then listing id. Listed 2026-08-29 to 2026-10-24. Numbers to two decimals at most.

| Column | Type | Unit | Meaning |
|---|---|---|---|
| `brand` | string | — | See above. Blank when the listing has no brand term (51 rows). |
| `garment` | string | — | The kind the measurer tagged: `top` (jumpers, cardigans, shirts, blouses, tops; 189), `bottom` (jeans, trousers, shorts, skirts; 200), `dress` (dresses, also jumpsuits and playsuits; 75), `outer` (coats, jackets, blazers; 94). When the record has no kind, a word from the title decides; blank when neither says (0 rows). |
| `listed_size` | string | — | The size on the listing, never calculated: the UK size term(s) when there are any, written `UK 8` or `UK 8-10` (note the `UK ` prefix, unlike the other files), otherwise the first size term as listed (`W26`, `M`). Blank when the listing carries no size. |
| `era` | string | — | Decade tag on the listing: `Y2K`, `00s`, `90s`, `80s`, `70s`, `60s` or `50s`. Blank when not tagged. |
| `bust_flat_in` | number | in | Bust straight across under the arms, laid flat. Blank when not measured, or when the listing gave the bust round only. |
| `bust_round_in` | number | in | Bust round: the flat number doubled, or as written when the listing measured round. Blank when not measured. Rows with a bust: 353. |
| `waist_flat_in` | number | in | Waist across the waistband or the narrowest point, laid flat. Blank as for bust. |
| `waist_round_in` | number | in | Waist round (flat doubled, or as written). Rows with a waist: 263. |
| `hip_flat_in` | number | in | Hips across the widest point, laid flat. Blank as for bust. |
| `hip_round_in` | number | in | Hips round (flat doubled, or as written). Rows with hips: 20. |
| `length_in` | number | in | From the shoulder seam, or the top of the waistband on bottoms, to the hem. Blank when not recorded. Rows with a value: 386. |
| `sleeve_in` | number | in | From the underarm seam to the cuff (a shoulder-to-cuff sleeve is a different measurement and is not in the file). Blank when sleeveless or not recorded. |
| `front_rise_in` | number | in | Front rise, crotch seam to the top of the waistband. Blank for anything but bottoms, and for bottoms where it was not recorded. Rows with a value: 162. |
| `inside_leg_in` | number | in | Inside leg along the inseam, crotch seam to hem. Blank as above. |
| `give` | string | — | How much the fabric gives, as the measurer recorded it: `none`, `some` (a little stretch, or an adjustable waist) or `stretch` (knit, jersey; measured unstretched, so the numbers read small). Blank when the record has no give class. 193 stretch, 117 some. |
| `material` | string | — | Main material from the listing's material terms, first match in a fixed preference order (fibres such as Cashmere, Merino, Wool, Silk, Linen; skins such as Leather, Suede, Shearling; fabrics such as Denim, Corduroy, Velvet, Tweed; faux phrases; then Cotton, Viscose and the rest; the first term as listed if none matches). Blank when the listing has no material term. The label's own composition is in `labels`. |
| `cut_for` | string | — | `women` (511), `men` (34) or `unisex` (13). |
| `in_stock` | string | — | `yes` (257) / `no` (301). |
| `listed_on` | date | YYYY-MM-DD | See above. |
| `listing_url` | url | — | See above. |

## Differences from the live CSVs on the website

The website serves the same data live, rebuilt as pieces are listed and sold, at `/kitanesque-jeans-measurements.csv`, `/kitanesque-knitwear-measurements.csv`, `/kitanesque-dress-measurements.csv`, `/kitanesque-rise-measurements.csv`, `/kitanesque-label-data.csv` and `/kitanesque-garment-measurements.csv`. This snapshot removes the UTF-8 byte-order mark and writes LF line endings; the jeans file gains the `garment` column, the knitwear file gains `garment` (and would rename a pre-18-Oct-2026 `label_uk_size` header to `listed_uk_size`); the other four files are the live rows and columns as they stand. `make_snapshot.py` in the same folder rebuilds a snapshot from the live files with these rules.
