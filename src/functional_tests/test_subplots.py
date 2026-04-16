import os
import matplotlib.pyplot as plt
import numpy as np

def test_multiple_subplots_generation():
   
    """
    Test funkcjonalny sprawdzający poprawne renderowanie wielu wykresów (subplots)
    na jednej figurze oraz ich zapis do pliku.
    """
    
    # dane wejściowe
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    #Wykresy
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(x, y1, color='blue')
    ax1.set_title('Wykres Sinus')

    ax2.plot(x, y2, color='red')
    ax2.set_title('Wykres Cosinus')
    output_file = "test_artifact_subplots.png"

    plt.savefig(output_file)
    plt.close(fig)
    
    # Weryfikacja
    assert os.path.exists(output_file) == True, "Plik z wieloma wykresami (subplots) nie został utworzony!"

    #Czyszczenie 
    if os.path.exists(output_file):
        os.remove(output_file)