# Testy akceptacyjne – wersja 1

Dokument zawiera trzy scenariusze akceptacyjne zgodne z aktualnym README.

## Scenariusz 1 – Wygenerowanie prostego wykresu liniowego

**Cel:** Użytkownik chce wygenerować podstawowy wykres liniowy.

**Kroki:**

1. Użytkownik uruchamia funkcję generującą wykres.
2. System tworzy figurę i wykres.
3. Wykres zapisywany jest do pliku PNG.

**Oczekiwany rezultat:**  
Plik PNG istnieje i zawiera poprawny wykres.

## Scenariusz 2 – Renderowanie wykresu słupkowego

**Cel:** Użytkownik chce wygenerować wykres słupkowy z etykietami.

**Kroki:**

1. Użytkownik uruchamia funkcję generującą wykres.
2. System tworzy wykres słupkowy.
3. Wykres zapisywany jest do pliku PNG.

**Oczekiwany rezultat:**  
Plik PNG istnieje i zawiera poprawny wykres słupkowy.

## Scenariusz 3 – Generowanie złożonego dashboardu analitycznego

**Cel:** Użytkownik chce wygenerować dashboard z wieloma typami wykresów.

**Kroki:**

1. System tworzy figurę z GridSpec.
2. Renderowane są trzy różne wykresy.
3. Dashboard zapisywany jest do pliku PNG.

**Oczekiwany rezultat:**  
Plik PNG istnieje i zawiera wszystkie trzy wykresy.
