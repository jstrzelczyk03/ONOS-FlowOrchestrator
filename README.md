# ONOS-FlowOrchestrator

Repozytorium zawiera projekt realizowany w ramach przedmiotu SCHT, dotyczący sieci SDN i płaszczyzny sterowania, przeprowadzany jest z wykorzystaniem kontrolera ONOS oraz emulatora Mininet. W plikach znajdują się m.in. przykłady konfiguracji węzłów sieci przez styk REST w ONOS, gotowe reguły przepływów i skrypty ułatwiające zarządzanie siecią.

## Struktura repozytorium

- **Aplikacja**  
  - networkControl.py – Skrypt w Pythonie, który używa biblioteki networkx do wczytywania pliku topology.txt, tworzenia grafu i generowania plików JSON z regułami dla ONOS.  
  - OnosInput.json – Szablon przepływów w ONOSie, na którym opiera się networkControl.py.  
  - topology.txt – Tekstowy opis topologii z informacjami o łączach (np. opóźnienia, przepustowość, porty).

- **Pliki_json_zad_1**  
  Zawiera pliki JSON z regułami przepływów dla pierwszego zadania, gdzie testowaliśmy pojedyncze sesje UDP/TCP.

- **Pliki_json_zad_2**  
  Pliki JSON z regułami do zadania drugiego, w którym konfigurujemy różne pary hostów i sprawdzamy, jak sieć zachowuje się przy wielu sesjach (UDP/TCP).

- **Topologia**  
  - MyTopo.py – Plik definiujący topologię w Mininecie (klasa MyTopo). Tworzy 10 hostów (h1-h10) i 10 przełączników (s1-s10), a następnie łączy je z odpowiednimi parametrami.

- **Sprawozdanie (PDF)**  
  Zawiera opis eksperymentów, uzyskane wyniki oraz wnioski. Znajdziesz w nim dokładne omówienie zadań i używanych narzędzi.

## Zadania (skrót)

1. **Zadanie 1**  
   Konfiguracja węzłów pełnej sieci przez styk REST ONOS, tak aby odtworzyć sesje z poprzedniego ćwiczenia laboratoryjnego (transport UDP/TCP) po tych samych trasach.

2. **Zadanie 2**  
   Usprawnienie konfiguracji węzłów (również przez styk REST) w celu poprawy parametrów przesyłu przy wielu jednoczesnych strumieniach.

3. **Zadanie 3**  
   Implementacja aplikacji sterującej w Pythonie (korzystającej z biblioteki HTTP). Aplikacja wczytuje topologię z pliku, wyznacza ścieżki i konfiguruje przepływy w ONOS.

4. **Zadanie 4**  
   Wykorzystanie tej aplikacji do optymalizacji ruchu przy wielu sesjach, a następnie porównanie wyników z wcześniejszą, mniej zoptymalizowaną konfiguracją.

Więcej szczegółów na temat konfiguracji, komend i przebiegu eksperymentów znajduje się w sprawozdaniu PDF.

---

### Autorzy
- Jakub Strzelczyk
- Jakub Grzechnik
