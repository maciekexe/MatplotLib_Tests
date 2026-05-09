import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import time


def render_plot(dpi, filename):
    x = np.linspace(0, 50, 10000)
    y = np.cos(x)

    start = time.time()

    plt.figure(dpi=dpi)
    plt.plot(x, y)
    plt.savefig(filename)
    plt.close()

    return time.time() - start


def test_dpi_render_performance(tmp_path):
    low = render_plot(100, tmp_path / "low.png")
    high = render_plot(600, tmp_path / "high.png")

    with open(tmp_path / "dpi.log", "w") as f:
        f.write(f"100 DPI: {low}\n")
        f.write(f"600 DPI: {high}\n")

    assert high > low