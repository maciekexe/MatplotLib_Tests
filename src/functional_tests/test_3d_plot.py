import os
import pytest
import numpy as np
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt

def test_3d_surface_plot_generation(tmp_path):
    print("\n" + "=" * 40)
    print("START TESTU: RENDEROWANIE WYKRESU 3D")
    print("=" * 40)

 
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)


    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)
    
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='Amplituda')
    ax.set_title('Test Funkcjonalny: Powierzchnia 3D')
    ax.set_xlabel('Oś X')
    ax.set_ylabel('Oś Y')
    ax.set_zlabel('Oś Z')

    output_file = tmp_path / "3d_plot_test.png"
    fig.savefig(output_file, dpi=150)
    plt.close(fig)

    assert output_file.exists(), "BŁĄD: Plik z wykresem 3D nie został zapisany!"
    assert os.path.getsize(output_file) > 5000, "BŁĄD: Wygenerowany plik PNG jest zbyt mały."
    print(f"SUKCES: Wykres 3D zapisany do pliku {output_file.name}")