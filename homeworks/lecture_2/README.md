# Lecture 02 homework: data, EDA and the Pharma-style RFM case

Companion notebook for *DS101 Lecture 02 - Fundamentals I - Data EDA and Pharma*.
Set up the environment first: see [`../README.md`](../README.md).

## Files

| File | Content |
|---|---|
| `practice.ipynb` | **Start here.** Slide-by-slide walkthrough with explanations and saved outputs, then the homework tasks (empty cells) |
| `practice_solution.ipynb` | Same walkthrough plus worked answers for every homework task |
| `data/transactions_raw.csv` | Raw data: 1,109 rows x 7 columns, one row per product line or credit |
| `data/customer_rfm.csv` | Reference RFM table: 84 accounts, to check your own computation |
| `prepare_l02.py` | Seeded generator that rebuilds both CSV files |
| `tools/slide_rfm_targets.csv` | R, F and M of all 84 accounts, read from the slide charts |
| `tools/extract_slide_rfm.py` | Instructor tool: reads those values from the `.pptx` |
| `tools/build_notebooks.py` | Instructor tool: single source that builds and runs both notebooks |

## What the notebook covers

| Notebook section | Slides |
|---|---|
| 1-2. Inspect, data quality | 3-4 |
| 3. Leakage | 5 |
| 4-5. Unit of analysis, RFM | 6-8 |
| 6. Exploratory plots | 9-10 |
| 7-8. k-means, scaling | 11-12 |
| 9-11. t-SNE, sensitivity, highlighting | 13-15 |
| 12. Cluster interpretation | 16 |
| 13. Segment vs recommendation | 17 |
| 14. Text representation | 18 |
| 15. Feature engineering | 19 |
| 16. Embeddings preview | 20-22 |
| Takeaways | 24 |

Homework tasks:

| Task | Topic | Slides |
|---|---|---|
| H1 | Review the credit lines | 3-4 |
| H2 | Window sensitivity of RFM | 7-8 |
| H3 | Choice of k: inertia and silhouette | 12 |
| H4 | t-SNE sensitivity to perplexity and seed | 14 |
| H5 | Embedding neighbors in 3-D, 4-D and 2-D | 22 |
| H6 | One finding, one limit | 23 |

## Data

The data is a synthetic teaching fixture: fictional business accounts buying products.
There are no patients and no clinical meaning, and it is not the historical Pharma dataset.

Columns of `transactions_raw.csv`:

| Column | Meaning |
|---|---|
| `line_id` | Product line identifier |
| `account_id` | Business account, `A001`-`A084` |
| `order_id` | Purchase order (`O...`) or credit note (`C...`); one order can have several lines |
| `order_date` | `YYYY-MM-DD`; two rows have unparseable dates on purpose |
| `product_id` | Product, `P01`-`P20` |
| `event_type` | `purchase` or `credit` |
| `line_value_cu` | Line value in currency units (CU), to the cent; credits are negative |

Observation window: 1 Jan - 31 Mar 2026. Snapshot: 1 Apr 2026.

## Match with the slides

The original data files behind the slides were not available. The slide charts, however, are
drawn shapes, so `tools/extract_slide_rfm.py` reads every account's R and F (slide 9) and net M
(slide 10) back from the shape positions. The generator then builds transactions that produce
exactly those values.

Exact match with the slides:

- 1,109 raw rows, 1 exact duplicate line, 2 quarantined rows, 1,106 clean rows; 84 accounts.
- A001's rows (slides 3, 6, 7) and the RFM table on slide 8.
- The scatter plots on slides 9-10 (same points).
- The k-means toy example on slide 11 (same points and centroids).
- The cluster table on slide 16: C1 28 / 10.0 / 13 / 4,491; C2 22 / 12.5 / 3 / 550; C3 34 / 63.0 / 4 / 545.
- The toy examples on slides 12, 17 and 18. (Slides 5 and 19 show no numbers; the notebook's
  small tables there are illustrations.)
- A001's three nearest neighbors on slide 22 (A084, A071, A075, same order), **only because** the
  training seed was picked for it: about 1-2% of seeds give this order. The notebook says so and
  shows other seeds.

Still different:

- t-SNE maps of the RFM features (slides 14, 15) are recomputed and look very close to the slides,
  but not pixel-identical (scikit-learn 1.9 instead of 1.8).
- The t-SNE map of the learned vectors (slide 21) differs more, because the learned vectors
  themselves come from a different training run.
- The learned vectors and their 4-D distances (slides 20, 22): the slide's training run is not
  available, and this objective does not fix the scale or shape of the vectors.
- Line-level details that the slides do not show (other accounts' individual lines, credits,
  products) are generated.

## For instructors

From the `homeworks` folder:

```bash
uv run python lecture_2/tools/extract_slide_rfm.py   # re-read slide values (needs the .pptx at the repo root)
uv run python lecture_2/prepare_l02.py               # rebuild the CSV files (checks every account against the slides)
uv run python lecture_2/tools/build_notebooks.py     # rebuild and run both notebooks
```

Edit the notebook text and code in `tools/build_notebooks.py`, not in the `.ipynb` files.
Otherwise the next rebuild overwrites your edits.
