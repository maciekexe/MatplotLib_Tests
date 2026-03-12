# Projekt zespołowy – System testowania OOB modułu Matplotlib

## 🎯 Cel projektu
Celem projektu jest zaprojektowanie i zrealizowanie uproszczonego systemu testowania OOB (Out Of The Box) dla najnowszej stabilnej wersji biblioteki **Matplotlib** dostępnej w repozytorium PyPI. Matplotlib to klasyczna biblioteka do tworzenia wykresów 2D i 3D w Pythonie. 

Projekt ma charakter praktyczny i skupia się na pracy zespołowej z wykorzystaniem GitHuba, wdrożeniu podstawowego CI/CD (uruchamianego manualnie) oraz przeprowadzeniu testów funkcjonalnych i wydajnościowych.

## 👥 Zespół i podział ról
Projekt realizowany jest w zespole 3-osobowym.

* **Maciej Kamiński – Tech Leader**
  * **Rola:** Zarządzanie repozytorium, koordynacja prac, dbałość o harmonogram.
  * **Zadania techniczne:** Konfiguracja środowiska i struktury projektu, implementacja CI/CD, przeprowadzanie Code Review oraz implementacja 2 testów funkcjonalnych.
* **Nataniel Żbikowski**
  * **Rola:** Analiza wydajności biblioteki oraz przygotowanie materiałów podsumowujących projekt.
  * **Zadania techniczne:** Zaprojektowanie i implementacja 2 testów wydajnościowych. Opracowanie krótkiej prezentacji końcowej.
* **Karol Stolc**
  * **Rola:** Dbałość o jakość z perspektywy użytkownika oraz główna dokumentacja testowa.
  * **Zadania techniczne:** Stworzenie dokumentu z 3 scenariuszami testów akceptacyjnych. Zaprojektowanie i napisanie pozostałych 3 testów funkcjonalnych weryfikujących realne użycie Matplotlib.

## 💬 Komunikacja
* **Codzienna komunikacja:** Serwer Discord, Messenger
* **Zarządzanie zadaniami i kodem:** GitHub (Issues, Pull Requesty, Code Review).

## 📅 Harmonogram projektu
Projekt trwa około 2,5 miesiąca i został podzielony na następujące etapy:

1. **Punkt kontrolny 1 (Aktualny): Organizacja projektu** 
   * Założenie repozytorium, podział ról, ustalenie harmonogramu i planowanie testów.
2. **Punkt kontrolny 2: Zarządzanie kodem** 
   * Wykorzystanie Issues i Pull Requestów, podział zadań w praktyce, wstępny kod testów.
3. **Punkt kontrolny 3: Testowanie**
   * Uruchomienie działającej pipeline, weryfikacja działających testów funkcjonalnych i wydajnościowych
4. **Release: Ocena końcowa** 
   * Kompletna dokumentacja, działająca pipeline, omówienie problemów w zespole oraz prezentacja końcowa

## 🧪 Strategia testowa i wstępne scenariusze

### Testy funkcjonalne 
Testy będą sprawdzać realne użycie biblioteki Matplotlib. Skupimy się na:
1. Generowaniu prostego wykresu liniowego 2D i zapisie do pliku `.png`.
2. Tworzeniu wykresu słupkowego (bar chart) z niestandardowymi kolorami i etykietami osi.
3. Eksportowaniu skomplikowanego wykresu do formatu wektorowego `.svg`.
4. Weryfikacji poprawnego renderowania wielu wykresów na jednej figurze.
5. Tworzenie prostego wykresu przestrzennego 3D i weryfikacja poprawnego wygenerowania artefaktu.

### Testy wydajnościowe 
Testy będą mierzyć czas wykonania operacji i zapisywać wynik do loga:
1. Pomiar czasu wygenerowania i zapisu do pliku bardzo dużego zbioru danych w porównaniu do małego zbioru.
2. Pomiar i porównanie czasu renderowania i eksportu tego samego skomplikowanego wykresu do pliku .png przy standardowej rozdzielczości (np. 100 DPI) oraz bardzo wysokiej rozdzielczości (np. 600 DPI).

### Testy akceptacyjne
Zostaną opisane w osobnym dokumencie (`testy_akceptacyjne.md`) i będą zawierać cel testu, oczekiwany rezultat oraz kryterium zaliczenia.

### CI/CD Pipeline
Wykorzystamy GitHub Actions. Pipeline będzie uruchamiana manualnie, zainstaluje środowisko oraz Matplotlib z PyPI, uruchomi testy jednostkowe biblioteki, a następnie uruchomi nasze testy funkcjonalne i wydajnościowe, wyświetlając podsumowanie.

## 📂 Struktura katalogów projektu
## 📂 Struktura katalogów projektu

```
.
├── .github/
│   └── workflows/
│       └── pipeline.yml            # Odpowiedzialny: Maciej Kamiński 
├── docs/
│   └── testy_akceptacyjne.md       # Odpowiedzialny: Karol Stolc (Dokument z 3 scenariuszami testów akceptacyjnych)
├── src/
│   ├── functional_tests/           # Odpowiedzialni: Karol Stolc (3 testy) & Maciej Kamiński (2 testy)
│   │   ├── test_2d_plot.py         # -> Karol Stolc
│   │   ├── test_bar_chart.py       # -> Karol Stolc
│   │   ├── test_svg_export.py      # -> Karol Stolc
│   │   ├── test_subplots.py        # -> Maciej Kamiński
│   │   └── test_3d_plot.py         # -> Maciej Kamiński
│   └── performance_tests/          # Odpowiedzialny: Nataniel Żbikowski (2 testy wydajnościowe)
│       ├── test_large_dataset.py   # -> Nataniel Żbikowski
│       └── test_dpi_render.py      # -> Nataniel Żbikowski
├── build_scripts/                  
│   └── build_matplotlib.sh         # dodatkowo
├── requirements.txt                # Odpowiedzialny: Maciej Kamiński
└── README.md                       # Odpowiedzialność wspólna (Koordynuje Maciej Kamiński)
```
