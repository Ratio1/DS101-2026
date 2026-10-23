"""Recover the Lecture 02 teaching fixture from the slide deck.

The deck's charts are drawn shapes, not pictures: every account is a shape at an exact position.
This script reads those positions back into data values.

- Slide 9  (Recency vs Frequency): 84 points -> R and F for every account.
- Slide 10 (Recency vs Net value): the same 84 accounts, same order -> M.
- Shape order is account order A001...A084 (checked against slides 8 and 22).
- Slide 11 (k-means toy): points and centroids, printed for the notebook builder.

Run from the homeworks folder:
    uv run python lecture_2/tools/extract_slide_rfm.py
Output: lecture_2/tools/slide_rfm_targets.csv
"""

import re
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[3]
DECK = ROOT / "DS101 Lecture 02 - Fundamentals I - Data EDA and Pharma.pptx"
OUT = Path(__file__).resolve().parent / "slide_rfm_targets.csv"
POINT_MAX_EMU = 100_000  # data points are small; the A001 highlight ring and centroids are larger


def shapes(deck, slide):
    """Return (preset, center_x, center_y, x, y, width, height) for every positioned shape."""
    xml = deck.read(f"ppt/slides/slide{slide}.xml").decode()
    out = []
    for sp in re.findall(r"<p:sp>.*?</p:sp>", xml, re.S):
        pos = re.search(r'<a:off x="(\d+)" y="(\d+)"/><a:ext cx="(\d+)" cy="(\d+)"', sp)
        preset = re.search(r'prst="(\w+)"', sp)
        if pos and preset:
            x, y, w, h = map(int, pos.groups())
            out.append((preset.group(1), x + w / 2, y + h / 2, x, y, w, h))
    return out


def panels(shape_list):
    """Plot frames from the axis lines: (x_left, x_right, y_bottom, y_top) per panel, left to right."""
    horizontal = [s for s in shape_list if s[0] == "line" and s[6] == 0 and s[5] > 1_000_000]
    frames = {}
    for _, _, _, x, y, w, _ in horizontal:
        left, right, bottom, top = frames.get(x, (x, x + w, y, y))
        frames[x] = (left, right, max(bottom, y), min(top, y))
    return [frames[x] for x in sorted(frames)]


def scale(value, lo_emu, hi_emu, hi_value):
    return (value - lo_emu) / (hi_emu - lo_emu) * hi_value


def main():
    deck = zipfile.ZipFile(DECK)

    s9 = shapes(deck, 9)
    (x0, x1, yb, yt), = panels(s9)
    pts9 = [s for s in s9 if s[0] == "ellipse" and s[5] < POINT_MAX_EMU]
    r = np.array([scale(s[1], x0, x1, 90) for s in pts9])
    f = np.array([scale(s[2], yb, yt, 18) for s in pts9])
    assert len(pts9) == 84
    # Positions are whole EMUs, so values are integers up to a tiny rounding error.
    assert np.abs(r - r.round()).max() < 0.01 and np.abs(f - f.round()).max() < 0.01

    s10 = shapes(deck, 10)
    frames = panels(s10)
    pts10 = [s for s in s10 if s[0] == "ellipse"]
    assert len(pts10) == 3 * 84
    rec = [s for s in s10 if s[0] == "ellipse"][84:168]          # panel 2: recency vs net value
    (px0, px1, pyb, pyt) = frames[1]
    r10 = np.array([scale(s[1], px0, px1, 90) for s in rec])
    m = np.array([scale(s[2], pyb, pyt, 10_000) for s in rec])
    assert np.array_equal(r10.round(), r.round()), "slide 10 order differs from slide 9"

    targets = pd.DataFrame({
        "account_id": [f"A{i:03d}" for i in range(1, 85)],
        "recency_days": r.round().astype(int),
        "frequency_orders": f.round().astype(int),
        "monetary_net_cu": m.round(2),
    })

    # Accounts quoted on slides 8 and 22
    quoted = {"A001": (10, 3, 460), "A010": (12, 12, 4437), "A040": (70, 2, 251), "A070": (28, 4, 599),
              "A071": (9, 3, 654), "A075": (10, 3, 708), "A084": (14, 4, 579)}
    t = targets.set_index("account_id")
    for account, (rr, ff, mm) in quoted.items():
        row = t.loc[account]
        assert (row.recency_days, row.frequency_orders, round(row.monetary_net_cu)) == (rr, ff, mm), account

    # Slide 16 cluster table
    X = StandardScaler().fit_transform(np.log1p(t))
    labels = KMeans(n_clusters=3, n_init=20, random_state=42).fit_predict(X)
    medians = t.groupby(labels).median()
    medians.insert(0, "accounts", pd.Series(labels).value_counts())
    rows = sorted(tuple(row) for row in medians.round(0).values.tolist())
    assert rows == [(22, 12, 3, 550), (28, 10, 13, 4491), (34, 63, 4, 545)], medians
    print("cluster sizes and medians (slide 16):")
    print(medians.round(2).to_string())

    targets.to_csv(OUT, index=False)
    print(f"wrote {OUT} ({len(targets)} accounts)")

    # Slide 11 toy example
    s11 = shapes(deck, 11)
    fx0, fx1, fyb, fyt = panels(s11)[0]
    small = [s for s in s11 if s[0] in ("ellipse", "diamond") and s[5] < 200_000 and s[1] < fx1]
    big = [s for s in s11 if s[0] == "diamond" and s[5] > 200_000]
    to_xy = lambda s, x0_: (round(scale(s[1], x0_, x0_ + (fx1 - fx0), 9), 2), round(scale(s[2], fyb, fyt, 9), 2))
    print("toy points  :", [to_xy(s, fx0) for s in small])
    print("toy groups  :", [s[0] for s in small])
    second_x0 = panels(s11)[1][0]
    print("centroids 1 :", [to_xy(s, fx0) for s in big if s[1] < fx1])
    print("centroids 2 :", [to_xy(s, second_x0) for s in big if s[1] > fx1])


if __name__ == "__main__":
    main()
