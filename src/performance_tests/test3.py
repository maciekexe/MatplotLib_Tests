import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import time

def create_subplots(n, filename):
    start = time.time()

    fig, axes = plt.subplots(n, n, figsize=(6, 6))

    for ax in axes.flat:
        x = np.linspace(0, 10, 100)
        ax.plot(x, np.sin(x))

    plt.savefig(filename)
    plt.close()

    return time.time() - start

def test_subplot_scaling(tmp_path):
    small = create_subplots(2, tmp_path / "small.png")
    large = create_subplots(5, tmp_path / "large.png")

    with open(tmp_path / "subplot.log", "w") as f:
        f.write(f"2x2: {small}\n")
        f.write(f"5x5: {large}\n")