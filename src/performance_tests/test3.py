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