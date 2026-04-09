import matplotlib.pyplot as plt
import numpy as np
import time
import os


def measure_render_time(data_size, label):
    data = np.random.randn(data_size)

    start_time = time.time()

    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title(f"Test Wydajności: {label} ({data_size} punktów)")

    filename = f"src/performance_tests/plot_{label.lower()}.png"
    plt.savefig(filename)
    plt.close()

    end_time = time.time()
    return end_time - start_time, filename


def test_performance_comparison():

    print("\n" + "=" * 40)
    print("START TESTU PORÓWNAWCZEGO")
    print("=" * 40)

    small_size = 100
    time_small, path_small = measure_render_time(small_size, "Maly_Zbior")
    print(f"[1] Mały zbiór ({small_size} pkt): {time_small:.4f}s")

    large_size = 1000000
    time_large, path_large = measure_render_time(large_size, "Duzy_Zbior")
    print(f"[2] Duży zbiór ({large_size} pkt): {time_large:.4f}s")

    diff = time_large / time_small if time_small > 0 else 0
    print("-" * 40)
    print(f"WYNIK: Duży zbiór generował się {diff:.2f}x wolniej niż mały.")
    print("=" * 40)

    assert os.path.exists(path_small), "Plik małego zbioru nie został utworzony"
    assert os.path.exists(path_large), "Plik dużego zbioru nie został utworzony"
    assert time_large < 15.0, f"BŁĄD: Generowanie dużego zbioru trwało za długo: {time_large:.2f}s"


if __name__ == "__main__":
    test_performance_comparison()