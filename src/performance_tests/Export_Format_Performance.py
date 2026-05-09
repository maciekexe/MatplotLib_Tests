import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import time


def export(format, filename):
    x = np.linspace(0, 100, 20000)
    y = np.sin(x)

    start = time.time()

    plt.figure()
    plt.plot(x, y)
    plt.savefig(filename, format=format)
    plt.close()

    return time.time() - start


def test_export_format_performance(tmp_path):
    png_time = export("png", tmp_path / "plot.png")
    svg_time = export("svg", tmp_path / "plot.svg")

    with open(tmp_path / "export.log", "w") as f:
        f.write(f"PNG: {png_time}\n")
        f.write(f"SVG: {svg_time}\n")

    assert png_time != svg_time