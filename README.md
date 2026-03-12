# Projekt zespołowy – System testowania OOB modułu Matplotlib

## 🎯 Cel projektu
Celem projektu jest zaprojektowanie i zrealizowanie uproszczonego systemu testowania OOB (Out Of The Box) dla najnowszej stabilnej wersji biblioteki **Matplotlib** dostępnej w repozytorium PyPI. Matplotlib to klasyczna biblioteka do tworzenia wykresów 2D i 3D w Pythonie. 

Projekt ma charakter praktyczny i skupia się na pracy zespołowej z wykorzystaniem GitHuba, wdrożeniu podstawowego CI/CD (uruchamianego manualnie) oraz przeprowadzeniu testów funkcjonalnych i wydajnościowych.

## 👥 Zespół i podział ról
Projekt realizowany jest w zespole 3-osobowym.

* **Maciej Kamiński – Tech Leader**
  * **Rola:** Zarządzanie repozytorium, koordynacja prac, dbałość o harmonogram oraz architekturę rozwiązań.
* **Nataniel Żbikowski**
  * **Rola:** 
* **Karol Stolc**
  * **Rola:** 

## 💬 Komunikacja
* **Codzienna komunikacja:** Serwer Discord
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

### Testy wydajnościowe 
Testy będą mierzyć czas wykonania operacji i zapisywać wynik do loga:
1. Pomiar czasu wygenerowania i zapisu do pliku bardzo dużego zbioru danych w porównaniu do małego zbioru.

### Testy akceptacyjne
Zostaną opisane w osobnym dokumencie (`testy_akceptacyjne.md`) i będą zawierać cel testu, oczekiwany rezultat oraz kryterium zaliczenia.

### CI/CD Pipeline
Wykorzystamy GitHub Actions. Pipeline będzie uruchamiana manualnie, zainstaluje środowisko oraz Matplotlib z PyPI, a następnie uruchomi nasze testy funkcjonalne i wydajnościowe, wyświetlając podsumowanie. Nie będziemy używać Dockerów ani matrix buildów.

## 📂 Struktura katalogów projektu
