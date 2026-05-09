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