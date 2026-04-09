import matplotlib.pyplot as plt
import numpy as np
import time
import os


def test_performance_large_dataset():

    data = np.random.randn(1000000)
    start_time = time.time()

    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title("Wydajność: 1 000 000 punktów")

    output_path = "src/performance_tests/large_data_plot.png"
    plt.savefig(output_path)
    plt.close()

    duration = time.time() - start_time
    print(f"\n[LOG] Czas generowania: {duration:.4f}s")

    assert os.path.exists(output_path), "Plik wykresu nie został utworzony!"
    assert duration < 20.0, f"Zbyt długi czas generowania: {duration:.2f}s"


if __name__ == "__main__":
    test_performance_large_dataset()