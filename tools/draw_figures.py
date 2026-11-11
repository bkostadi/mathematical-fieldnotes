"""Rebuild the PNGs used by the website. Requires matplotlib and numpy."""

from collections import Counter
from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


FIGURES = Path(__file__).resolve().parents[1] / "assets" / "figures"
FOREST = "#173e38"
CREAM = "#f5ecd6"
COPPER = "#ffb384"
T = np.linspace(0, 2 * np.pi, 721)
X, Y = np.cos(T), np.sin(T)


def plate(width, height, background):
    figure = plt.figure(figsize=(width / 100, height / 100), dpi=100)
    figure.patch.set_facecolor(background)
    axes = figure.add_axes([0, 0, 1, 1])
    axes.set_axis_off()
    axes.set_aspect("equal")
    return figure, axes


def save(figure, name, transparent=False):
    figure.savefig(FIGURES / name, dpi=100, transparent=transparent)
    plt.close(figure)


def shear_plot():
    width, height = 960, 476
    figure, axes = plate(width, height, FOREST)
    yrange = 1.29
    xrange = yrange * width / height
    axes.set_xlim(-xrange, xrange)
    axes.set_ylim(-yrange, yrange)
    for i in range(-12, 13):
        shade = "#30564d" if i % 2 == 0 else "#254a42"
        axes.axvline(i / 4, color=shade, lw=0.8)
        axes.axhline(i / 4, color=shade, lw=0.8)
    axes.axvline(0, color="#6a8b7d", lw=1)
    axes.axhline(0, color="#6a8b7d", lw=1)
    for amount in np.arange(1, 13) / 13:
        axes.plot(X + amount * Y, Y, color="#709688", lw=1)
    axes.plot(X + Y, Y, color=COPPER, lw=2.4)
    axes.plot(X, Y, color=CREAM, lw=1.6, dashes=(3, 3.2))
    axes.plot(1, 1, "o", color=COPPER, ms=9)
    axes.text(xrange - 0.12, 0.05, "x", color=CREAM, size=13, style="italic")
    axes.text(0.055, yrange - 0.11, "y", color=CREAM, size=13, style="italic")
    save(figure, "shear.png")


def marks():
    for name, size, background, primary, accent in [
        ("algebra-mark.png", 260, "#e5ecdf", "#548472", "#255b49"),
        ("fieldmark.png", 128, "none", "#316c58", "#163e32"),
    ]:
        figure, axes = plate(size, size, background)
        axes.set(xlim=(-1.83, 1.83), ylim=(-1.83, 1.83))
        if name == "algebra-mark.png":
            for v in (-1.5, -1, -0.5, 0, 0.5, 1, 1.5):
                axes.axhline(v, color="#ced9ca", lw=0.9)
                axes.axvline(v, color="#ced9ca", lw=0.9)
        for k in np.linspace(0, 1.15, 5):
            axes.plot(X + k * Y, Y, color=primary, lw=1.7)
        axes.plot(X + 1.15 * Y, Y, color=accent, lw=2.8)
        save(figure, name, transparent=background == "none")


def dice_plots():
    counts = Counter(a + b for a, b in product(range(1, 7), repeat=2))
    sums = sorted(counts)
    heights = [counts[x] for x in sums]
    figure, axes = plate(260, 260, "#f4e5d7")
    axes.set(xlim=(0.8, 13.2), ylim=(-2.8, 9.6))
    axes.bar(sums, heights, width=0.67,
             color=["#a24d33" if x == 7 else "#c58a65" for x in sums])
    axes.plot([1.3, 12.7], [0, 0], color="#704d3d", lw=1.3)
    save(figure, "probability-mark.png")

    figure, axes = plt.subplots(figsize=(12.4, 5.8), dpi=100)
    figure.patch.set_facecolor("#edf0e5")
    axes.set_facecolor("#edf0e5")
    figure.subplots_adjust(left=0.11, right=0.96, top=0.88, bottom=0.20)
    axes.set_axisbelow(True)
    axes.grid(axis="y", color="#cdd8c9", lw=1)
    axes.bar(sums, heights, width=0.68,
             color=["#a24d33" if x == 7 else "#467865" for x in sums])
    axes.set(xlim=(1.35, 12.65), ylim=(0, 6.6), xticks=sums, yticks=[0, 2, 4, 6])
    axes.tick_params(length=0, pad=8, labelsize=17, colors="#263e34")
    for spine in axes.spines.values():
        spine.set_visible(False)
    axes.axhline(0, color="#567262", lw=1.4)
    axes.set_xlabel("Sum of the two dice", fontsize=17, labelpad=12, color=FOREST)
    axes.set_ylabel("Ordered outcomes", fontsize=17, labelpad=12, color=FOREST)
    save(figure, "dice-sums.png")


if __name__ == "__main__":
    FIGURES.mkdir(parents=True, exist_ok=True)
    shear_plot()
    marks()
    dice_plots()
