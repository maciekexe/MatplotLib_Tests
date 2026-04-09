import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def test_bar_chart_with_custom_colors_and_labels(tmp_path):
    # Arrange
    categories = ["A", "B", "C", "D"]
    values = [10, 15, 7, 12]
    colors = ["red", "green", "blue", "orange"]

    output_file = tmp_path / "bar_chart.png"

    # Act
    fig, ax = plt.subplots()
    ax.bar(categories, values, color=colors)
    ax.set_title("Custom Bar Chart")
    ax.set_xlabel("Category")
    ax.set_ylabel("Value")

    fig.savefig(output_file)
    plt.close(fig)

    # Assert
    assert output_file.exists(), "Plik PNG nie został utworzony."
    assert os.path.getsize(output_file) > 0, "Plik PNG jest pusty."
