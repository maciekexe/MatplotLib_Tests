import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def test_simple_2d_plot_png_generation(tmp_path):
    # Arrange
    x = [0, 1, 2, 3, 4]
    y = [value ** 2 for value in x]

    output_file = tmp_path / "simple_2d_plot.png"

    # Act
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Simple 2D Plot")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")

    fig.savefig(output_file)
    plt.close(fig)

    # Assert
    assert output_file.exists(), "Plik PNG nie został utworzony."
    assert os.path.getsize(output_file) > 0, "Plik PNG jest pusty."
