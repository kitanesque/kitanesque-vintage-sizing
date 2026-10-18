# Kitanesque vintage sizing: label sizes against the tape

**What does a size on a second-hand label actually measure?** This dataset answers it for 198 pre-owned and vintage garments, each measured flat by hand before sale: 94 pairs of jeans with the waist printed on the label (W23–W37) set against the waistband on the tape, and 104 women's knitted pieces with their UK size set against the bust on the tape. Nothing is estimated from a size chart. Snapshot of 18 October 2026, CC BY 4.0.

DOI (canonical, cite this): [10.5281/zenodo.23452246](https://doi.org/10.5281/zenodo.23452246) · Also on: [Hugging Face](https://huggingface.co/datasets/kitanesque/kitanesque-vintage-sizing) · [Kaggle](https://www.kaggle.com/datasets/andradalcaran/vintage-clothing-sizing-label-vs-tape)

- **Live version, updated as pieces are listed and sold:** [Jeans sizing by brand](https://kitanesque.co.uk/jeans-sizing-by-brand/) · [Knitwear sizing by brand](https://kitanesque.co.uk/knitwear-sizing-by-brand/)
- **Maintainer:** Kitanesque Ltd (company no. 17442810, England and Wales) · [kitanesque.co.uk](https://kitanesque.co.uk/) · hello@kitanesque.co.uk

## Files

| File | Rows | What one row is |
|---|---|---|
| `data/kitanesque-vintage-jeans-measurements-2026-10-18.csv` | 94 | One pair of jeans (denim only), from 66 labels. Label waist W23–W37. 54 in stock, 40 sold on the snapshot date. |
| `data/kitanesque-vintage-knitwear-measurements-2026-10-18.csv` | 104 | One women's knitted piece: 63 jumpers and knit tops, 24 cardigans, 12 knit dresses, 4 knit vests, 1 knitted blazer, from 79 labels. 54 cashmere. 45 in stock, 59 sold. |

Column-by-column definitions are in [`data_dictionary.md`](data_dictionary.md).

## What is measured, and how

- **Jeans:** waistband straight across the top, doubled (`waistband_round_in`); front rise from the crotch seam to the top of the waistband (`rise_in`); inside leg from the crotch seam to the hem (`inside_leg_in`). Plus the waist printed on the label (`label_waist`) and the era tag where known (56 Y2K, 3 from the 1990s).
- **Knitwear:** bust straight across under the arms, doubled (`bust_round_in`); length from the shoulder seam to the hem; sleeve from the underarm seam to the cuff; main fibre from the care label.
- **The UK size** (`listed_uk_size`) is the size the piece was sold as, chosen by hand after measuring and trying it on a UK 8 model (5′6″). It is never computed. For knitwear, `uk_standard_bust_in` gives the body bust a UK woman of that size is usually made for, from the size table used across the shop, so the two can be compared.

Unit: inches, to the nearest 0.5 in. Garments laid flat and unstretched.

## Some numbers from the snapshot

- The 94 pairs of jeans: the waistband measured from 4 in under to 6 in over the W number on the label; on average 0.7 in over.
- 56 Y2K pairs of jeans with a rise: median front rise 8.5 in; 21 sit under 8 in.
- Knitwear: the bust came out on average 1.5 in roomier than the UK standard for the size it was listed as; 28 of 104 pieces within 1.5 in of it.

## How it was collected

Kitanesque is a small online shop: one buyer chooses every piece, and one person measures and lists it. The measurements were written into each listing on kitanesque.co.uk between 29 August and 14 October 2026 and read back from the listings for this file. Sold pieces stay in the data, so the sample does not shrink as stock sells. All listing URLs answered HTTP 200 on the snapshot date; sold pieces stay online marked as sold.

## Limitations and biases

- **One shop, one buyer.** Brands and eras reflect what the shop stocks: mostly US and UK labels, with a strong Y2K denim lean (Miss Me, Silver, Maurices, True Religion, l.e.i.) and a lot of cashmere. Not a random sample of the market.
- **Mostly women's.** 92 of 94 pairs of jeans, and all knitwear, are women's.
- **Second-hand garments.** Fabric may have stretched or shrunk with wear and washing; measurements describe the garment as sold, not as made.
- **Measured flat, by hand.** About ±0.5 in.
- **Label sizes as printed.** W numbers are vanity-sized differently by every brand and era; that difference is the point of the data. For knitwear the size is the one on the listing, which usually but not always matches the label.
- **Small counts per brand.** 66 and 79 labels across 94 and 104 rows; most brands appear once or twice.
- **Snapshot.** The live files on the website keep growing; this file is fixed at 2026-10-18.

## Licence and how to cite

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), full text in [`LICENSE`](LICENSE). Free to use, share and adapt, including commercially, with credit and a link back.

> Dălcăran, A. (2026). *Kitanesque vintage sizing: label sizes against tape measurements for second-hand jeans and knitwear* (Version 2026-10-18) [Data set]. Kitanesque Ltd. https://doi.org/10.5281/zenodo.23452246

A `CITATION.cff` file is included. Please link to [kitanesque.co.uk](https://kitanesque.co.uk/) when you quote the numbers.

## Maintainer

Kitanesque Ltd (company no. 17442810, England and Wales) · [kitanesque.co.uk](https://kitanesque.co.uk/) · hello@kitanesque.co.uk

Measurements by Andra Dălcăran, founder of Kitanesque. Corrections and questions are welcome by email.
