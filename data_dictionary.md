# Data dictionary — Kitanesque vintage sizing, snapshot 2026-10-18

Two CSV files, UTF-8 without BOM, comma-separated, LF line endings, one header row. Empty cell = not measured / not recorded. All lengths in inches, measured by hand with the garment laid flat and unstretched, to the nearest 0.5 in.

Every measurement was taken by Andra Dălcăran (Kitanesque Ltd) before the piece was listed for sale, and written into the listing. The website reads the numbers back from the listings; nothing in these files is estimated, interpolated or computed from a size chart, except the column `uk_standard_bust_in`, which is a reference value from a size table (see below).

## 1. `data/kitanesque-vintage-jeans-measurements-2026-10-18.csv` — 94 rows

One row per pair. Pieces with a waist size printed on the label (W number) and a measured waistband. Shorts, skirts, dresses, jumpsuits and dungarees are excluded (inside leg under 18 in, or the listing title says so). Pieces without an identified brand are excluded.

| Column | Type | Unit | Meaning |
|---|---|---|---|
| `brand` | string | — | Brand on the label, as listed. |
| `garment` | string | — | `jeans` for every row. Since 18 Oct 2026 the live data holds denim only (trousers and skorts that carry a W label are filtered out at the source); the column is kept for forward compatibility. |
| `label_waist` | string | — | Waist size printed on the label, e.g. `W28`. As printed; US-style W sizes on most pairs. |
| `era` | string | — | Decade tag on the listing where known: `Y2K` (roughly 1998–2008) or `90s`. Empty = not tagged; it does not mean modern. |
| `waistband_round_in` | number | in | Waistband measured straight across the top, laid flat, and doubled. This is the garment's waistband, not the wearer's waist. |
| `rise_in` | number | in | Front rise, from the crotch seam to the top of the waistband. Recorded for every row. |
| `inside_leg_in` | number | in | Inside leg, along the inseam from the crotch seam to the hem. Recorded for every row. |
| `listed_uk_size` | string | UK women's size | The UK size the piece was listed as on kitanesque.co.uk, chosen by hand by Andra after measuring and trying the piece on a UK 8 model (5′6″). Never computed from the label or a chart. A range such as `8-10` means it fits across both. Empty for 1 row. |
| `cut_for` | string | — | `women` (92), `men` (1) or `unisex` (1). |
| `in_stock` | string | — | `yes` if the piece was still for sale on 2026-10-18, `no` if sold. Sold pieces are kept so the sample does not shrink as stock sells. |
| `listed_on` | date | YYYY-MM-DD | Date the piece was first published on kitanesque.co.uk (2026-08-29 to 2026-10-14). Not the manufacturing date. |
| `listing_url` | url | — | The product page. All 94 answered HTTP 200 on 2026-10-18; sold pieces stay online marked as sold. |

## 2. `data/kitanesque-vintage-knitwear-measurements-2026-10-18.csv` — 104 rows

One row per women's knitted piece (jumpers, cardigans, knit dresses, knit vests, one knitted blazer) with a measured bust and a UK size on its listing.

| Column | Type | Unit | Meaning |
|---|---|---|---|
| `brand` | string | — | Brand on the label, as listed. |
| `garment` | string | — | `jumper/knit top` (63), `cardigan` (24), `knit dress` (12), `knit vest/top` (4), `knit jacket` (1). Added for this snapshot from the listing URL. |
| `listed_uk_size` | string | UK women's size | The UK size on the piece's listing, chosen by hand by Andra (see the jeans table). Usually the size on the label; where they disagree, the listing wins. The same column name as in the live CSV on the website (called `label_uk_size` there before 18 Oct 2026). |
| `bust_round_in` | number | in | Bust measured straight across under the arms, laid flat, and doubled. |
| `uk_standard_bust_in` | number | in | Reference body bust for `listed_uk_size`, from the women's size table used on kitanesque.co.uk: UK 4 = 30.5, 6 = 31.5, 8 = 33, 10 = 35, 12 = 37, 14 = 39, 16 = 41, 18 = 43.5, 20 = 46, 22 = 48.5. For a range the mean of the sizes in it (e.g. 8-10 = 34). A reference value, not a measurement. |
| `length_in` | number | in | From the shoulder seam to the hem. |
| `sleeve_in` | number | in | From the underarm seam to the cuff. Empty for 27 rows (sleeveless, short sleeves or not recorded). |
| `material` | string | — | Main fibre from the care label: Cashmere (54), Wool (19), Cotton (5), Silk (2), Viscose (1), Linen (1). Empty for 22 rows where the label had no clear main fibre. |
| `in_stock` | string | — | `yes` (45) / `no` (59, sold). |
| `listed_on` | date | YYYY-MM-DD | First published on kitanesque.co.uk (2026-08-29 to 2026-10-13). |
| `listing_url` | url | — | The product page; all answered HTTP 200 on 2026-10-18. |

## Differences from the live CSVs on the website

The website serves the same data live at `/kitanesque-jeans-measurements.csv` and `/kitanesque-knitwear-measurements.csv` (rebuilt as pieces are listed and sold). This snapshot: adds the `garment` column to both files and removes the UTF-8 byte-order mark; otherwise the rows are the live rows. Since 18 Oct 2026 the live files themselves hold denim only (jeans) and knitted pieces only (knitwear), and the knitwear column is named `listed_uk_size`. `make_snapshot.py` rebuilds a snapshot from the live files with the same rules.
