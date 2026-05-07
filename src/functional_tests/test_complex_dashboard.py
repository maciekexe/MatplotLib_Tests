# TODO: implement complex dashboard test
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
import os

def test_complex_dashboard(tmp_path):
    output_file = tmp_path / "dashboard.png"

    fig = plt.figure(figsize=(12, 8))
    gs = GridSpec(3, 3, figure=fig)


    ax1 = fig.add_subplot(gs[0, :2])
    x = np.arange(0, 10, 1)
    y = np.sin(x)
    y_err = np.random.uniform(0.1, 0.3, size=len(x))

    ax1.errorbar(x, y, yerr=y_err, fmt='-o', color='blue', label="Pomiar")
    ax1.set_title("Wykres liniowy z błędami pomiarowymi")
    ax1.set_xlabel("Czas [s]")
    ax1.set_ylabel("Amplituda")
    ax1.legend()

    ax1.annotate(
        "Lokalne maksimum",
        xy=(1, np.sin(1)),
        xytext=(2, 0.8),
        arrowprops=dict(arrowstyle="->")
    )


    ax2 = fig.add_subplot(gs[0, 2])
    categories = ["A", "B", "C"]
    values = [5, 3, 7]
    ax2.bar(categories, values, color=["red", "green", "orange"])
    ax2.set_title("Wykres słupkowy")


    ax3 = fig.add_subplot(gs[1, :2])
    scatter_x = np.random.rand(50)
    scatter_y = np.random.rand(50)
    scatter_c = np.random.rand(50)
    ax3.scatter(scatter_x, scatter_y, c=scatter_c, cmap="viridis")
    ax3.set_title("Wykres punktowy (scatter)")


    ax4 = fig.add_subplot(gs[1:, 2])
    data = np.random.randn(200)
    ax4.hist(data, bins=20, color="purple", alpha=0.7)
    ax4.set_title("Histogram")


    ax5 = fig.add_subplot(gs[2, :2])
    t = np.linspace(0, 2*np.pi, 100)
    ax5.plot(t, np.cos(t), color="black")
    ax5.set_title("Wykres kosinusoidalny")

    fig.tight_layout()
    fig.savefig(output_file)
    plt.close(fig)

    assert output_file.exists()
    assert os.path.getsize(output_file) > 0
