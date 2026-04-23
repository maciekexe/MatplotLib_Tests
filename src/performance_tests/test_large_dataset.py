import os
import time
import pytest
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def measure_render_time(data_size, label, tmp_path):
    data = np.random.randn(data_size)
    start_time = time.time()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data)
    ax.set_title(f"Test Wydajności: {label} ({data_size} punktów)")

    output_file = tmppath / f"plot{label.lower()}.png"
    fig.savefig(output_file)
    plt.close(fig)

    end_time = time.time()
    return end_time - start_time, output_file

def test_performance_comparison(tmp_path):
    print("\n" + "=" * 40)
    print("START TESTU PORÓWNAWCZEGO")
    print("=" * 40)

    small_size = 100
    time_small, path_small = measure_render_time(small_size, "Maly_Zbior", tmp_path)
    print(f"[1] Mały zbiór ({small_size} pkt): {time_small:.4f}s")

    large_size = 1000000
    time_large, path_large = measure_render_time(large_size, "Duzy_Zbior", tmp_path)
    print(f"[2] Duży zbiór ({large_size} pkt): {time_large:.4f}s")

    diff = time_large / time_small if time_small > 0 else 0
    print("-" * 40)
    print(f"WYNIK: Duży zbiór generował się {diff:.2f}x wolniej niż mały.")
    print("=" * 40)

    assert path_small.exists(), "Plik małego zbioru nie został utworzony"
    assert path_large.exists(), "Plik dużego zbioru nie został utworzony"
    assert time_large < 15.0, f"BŁĄD: Generowanie dużego zbioru trwało za długo: {time_large:.2f}s"