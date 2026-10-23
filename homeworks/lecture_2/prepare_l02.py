"""Generate the synthetic Lecture 02 teaching fixture.

Fictional business accounts buying products (no patients, no clinical data).

Every account's R, F and net M come from the Lecture 02 slides themselves:
`tools/slide_rfm_targets.csv` was read back from the chart shapes on slides 9 and 10
(see `tools/extract_slide_rfm.py`). This script creates transaction lines that produce
exactly those values, plus the data-quality cases from slides 3-4:

- 1,109 raw rows x 7 columns: 1 exact duplicate line, 2 unparseable dates, 1,106 clean rows.
- 84 accounts, observation window 1 Jan - 31 Mar 2026, snapshot 1 Apr 2026.
- A001 has exactly the slide rows (R = 10 days, F = 3 orders, M = 460 CU).
- 17 credit notes; 4 of them name a product the account did not buy in the window.

Run:  uv run python lecture_2/prepare_l02.py   (from the homeworks folder)
Outputs: data/transactions_raw.csv and data/customer_rfm.csv
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
WINDOW_START = pd.Timestamp("2026-01-01")
SNAPSHOT = pd.Timestamp("2026-04-01")
N_DAYS = (SNAPSHOT - WINDOW_START).days  # 90 days, day 0 = 1 Jan
CLEAN_ROWS = 1106
N_CREDITS = 17             # including A001's credit
N_UNMATCHED_CREDITS = 4    # credits for a product the account did not buy (homework H1)
MIN_LINE_CENTS = 500
HERE = Path(__file__).resolve().parent
TARGETS = HERE / "tools" / "slide_rfm_targets.csv"
OUT_DIR = HERE / "data"


def load_plans(rng):
    """One plan per account (except A001): target R, F, M in cents, lines per order, credit flag."""
    targets = pd.read_csv(TARGETS)
    assert ((targets["frequency_orders"] <= N_DAYS + 1 - targets["recency_days"])).all(), \
        "some account has more orders than days before its last purchase"

    others = targets[targets["account_id"] != "A001"].reset_index(drop=True)
    credit_idx = set(rng.choice(len(others), size=N_CREDITS - 1, replace=False).tolist())
    unmatched_idx = set(rng.choice(sorted(credit_idx), size=N_UNMATCHED_CREDITS, replace=False).tolist())

    plans = []
    for i, row in others.iterrows():
        max_lines = 4 if row.frequency_orders >= 8 else 3
        plans.append({
            "account_id": row.account_id,
            "r": int(row.recency_days),
            "f": int(row.frequency_orders),
            "m_cents": int(round(row.monetary_net_cu * 100)),
            "lines": rng.integers(1, max_lines, size=int(row.frequency_orders)),
            "credit": int(i in credit_idx),
            "credit_unmatched": i in unmatched_idx,
        })
    return targets, plans


def adjust_line_counts(rng, plans, target):
    """Add or remove product lines (never whole orders) to hit the row target."""
    total = sum(p["lines"].sum() + p["credit"] for p in plans)
    while total != target:
        plan = plans[rng.integers(len(plans))]
        i = rng.integers(len(plan["lines"]))
        if total < target and plan["lines"][i] < 4:
            plan["lines"][i] += 1
            total += 1
        elif total > target and plan["lines"][i] > 1:
            plan["lines"][i] -= 1
            total -= 1


def split_value(rng, gross_cents, n_lines):
    """Split a gross purchase value (cents) into positive line values (cents) that sum exactly."""
    if gross_cents < n_lines * MIN_LINE_CENTS:
        raise ValueError("gross value too small for the number of lines")
    shares = rng.dirichlet(np.full(n_lines, 2.0))
    spare = gross_cents - n_lines * MIN_LINE_CENTS
    values = MIN_LINE_CENTS + np.floor(shares * spare).astype(int)
    values[np.argmax(values)] += gross_cents - values.sum()
    return values


def account_lines(rng, plan):
    """Expand one account plan into line records (event, order_no, day, product, cents)."""
    last_day = N_DAYS - plan["r"]
    earlier = rng.choice(last_day, size=plan["f"] - 1, replace=False) if plan["f"] > 1 else []
    days = np.sort(np.append(earlier, last_day)).astype(int)

    credit_cents = 0
    if plan["credit"]:
        credit_cents = -int(round(plan["m_cents"] * rng.uniform(0.03, 0.08)))
    n_lines = int(plan["lines"].sum())
    values = split_value(rng, plan["m_cents"] - credit_cents, n_lines)
    products = rng.choice(20, size=n_lines) + 1

    records, k = [], 0
    for order_no, (day, n) in enumerate(zip(days, plan["lines"])):
        for _ in range(n):
            records.append(("purchase", order_no, int(day), int(products[k]), int(values[k])))
            k += 1
    if plan["credit"]:
        first_bought = {}                       # product -> first day the account bought it
        for _, _, day, product, _ in records:
            first_bought.setdefault(product, day)
        if plan["credit_unmatched"]:
            product = int(rng.choice([p for p in range(1, 21) if p not in first_bought]))
            after = int(days[0])                # only after the account's first purchase
        else:
            product = int(rng.choice(sorted(first_bought)))
            after = first_bought[product]       # only after this product was bought
        credit_day = int(rng.integers(after + 1, N_DAYS)) if after + 1 < N_DAYS else after
        records.append(("credit", None, credit_day, product, credit_cents))
    return records


def a001_records():
    """A001 exactly as on slides 3, 6 and 7 (values in cents)."""
    jan10, feb20, mar22, mar25 = 9, 50, 80, 83
    return [
        ("purchase", 0, jan10, 3, 10_000),
        ("purchase", 1, feb20, 7, 15_000),
        ("purchase", 1, feb20, 12, 5_000),
        ("purchase", 2, mar22, 5, 20_000),
        ("credit", None, mar25, 5, -4_000),
    ]


def build_raw(rng):
    targets, plans = load_plans(rng)
    adjust_line_counts(rng, plans, CLEAN_ROWS - len(a001_records()))

    per_account = {"A001": a001_records()}
    for plan in plans:
        per_account[plan["account_id"]] = account_lines(rng, plan)

    rows, order_seq, credit_seq = [], 0, 0
    for account in sorted(per_account):
        order_ids = {}
        for event, order_no, day, product, cents in sorted(per_account[account], key=lambda x: x[2]):
            if event == "credit":
                credit_seq += 1
                order_id = f"C{credit_seq:03d}"
            else:
                if order_no not in order_ids:
                    order_seq += 1
                    order_ids[order_no] = f"O{order_seq:03d}"
                order_id = order_ids[order_no]
            date = (WINDOW_START + pd.Timedelta(days=day)).strftime("%Y-%m-%d")
            rows.append([account, order_id, date, f"P{product:02d}", event, cents / 100])

    # Two rows whose dates cannot be parsed: they must be quarantined, not guessed.
    rows.append(["A055", f"O{order_seq + 1:03d}", "2026-02-30", "P04", "purchase", 310.0])
    rows.append(["A023", f"O{order_seq + 2:03d}", "15/03/2026?", "P11", "purchase", 95.0])

    raw = pd.DataFrame(rows, columns=["account_id", "order_id", "order_date", "product_id",
                                      "event_type", "line_value_cu"])
    raw.insert(0, "line_id", [f"L{i:04d}" for i in range(1, len(raw) + 1)])

    # One exact duplicate line (same line_id, same content), inserted next to its original.
    dup_at = int(rng.integers(100, len(raw) - 100))
    raw = pd.concat([raw.iloc[: dup_at + 1], raw.iloc[[dup_at]], raw.iloc[dup_at + 1:]],
                    ignore_index=True)
    return raw, targets


def clean(raw):
    out = raw.drop_duplicates()
    dates = pd.to_datetime(out["order_date"], format="%Y-%m-%d", errors="coerce")
    return out[dates.notna()].assign(order_date=dates[dates.notna()])


def compute_rfm(clean_df):
    purchases = clean_df[clean_df["event_type"] == "purchase"]
    rfm = pd.DataFrame({
        "recency_days": (SNAPSHOT - purchases.groupby("account_id")["order_date"].max()).dt.days,
        "frequency_orders": purchases.groupby("account_id")["order_id"].nunique(),
        "monetary_net_cu": clean_df.groupby("account_id")["line_value_cu"].sum().round(2),
    })
    return rfm.reset_index()


def main():
    rng = np.random.default_rng(SEED)
    raw, targets = build_raw(rng)
    clean_df = clean(raw)
    rfm = compute_rfm(clean_df)

    assert raw.shape == (1109, 7), raw.shape
    assert raw["line_id"].duplicated().sum() == 1
    assert len(clean_df) == CLEAN_ROWS, len(clean_df)
    assert (clean_df["event_type"] == "credit").sum() == N_CREDITS
    merged = rfm.merge(targets, on="account_id", suffixes=("", "_slide"))
    assert len(merged) == 84
    for col in ["recency_days", "frequency_orders", "monetary_net_cu"]:
        assert (merged[col] - merged[col + "_slide"]).abs().max() < 0.005, col

    OUT_DIR.mkdir(exist_ok=True)
    raw.to_csv(OUT_DIR / "transactions_raw.csv", index=False)
    rfm.to_csv(OUT_DIR / "customer_rfm.csv", index=False)
    print(f"raw {raw.shape}, clean {clean_df.shape}, accounts {len(rfm)}; RFM equals the slide values")


if __name__ == "__main__":
    main()
