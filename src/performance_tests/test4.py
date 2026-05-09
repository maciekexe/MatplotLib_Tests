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