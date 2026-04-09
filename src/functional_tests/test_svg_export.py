import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def test_complex_plot_svg_export(tmp_path):
    # Arrange
    x = [0, 1, 2, 3, 4, 5]
    y1 = [value for value in x]
    y2 = [value ** 2 for value in x]

    output_file = tmp_path / "complex_plot.svg"

    # Act
    fig, ax = plt.subplots()
    ax.plot(x, y1, label="Linear")
    ax.plot(x, y2, label="Quadratic")
    ax.set_title("Complex Plot")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.legend()

    fig.savefig(output_file, format="svg")
    plt.close(fig)

    # Assert
    assert output_file.exists(), "Plik SVG nie został utworzony."
    assert os.path.getsize(output_file) > 0, "Plik SVG jest pusty."