# ADM leds - ESP32
Skrypt na PC do [kontrolera](https://github.com/Adam-Sidor/ADMleds_ESP32),  umożliwia on automatyczne włączanie Ledów po włączeniu komputera i połączenia go z internetem.

---

## Spis treści
1. [Opis projektu](#opis-projektu)  
2. [Wymagania](#wymagania)  
3. [Instalacja](#instalacja)  
4. [Użycie](#użycie)  
5. [Funkcjonalności](#funkcjonalności)  
6. [Licencja](#licencja)  
7. [Kontakt](#kontakt)  

---

## Opis projektu
- Projekt wspomaga sterowanie taśmą LED WS2812B za pomocą zapytań HTTP.
- Skrypt dostępny na PC. 

---

## Wymagania
-  [Kontroler LED](https://github.com/Adam-Sidor/ADMleds_ESP32) 
- Interpreter języka Python   

---

## Instalacja
Instrukcja krok po kroku, jak skonfigurować i uruchomić projekt:  
1. Sklonowanie repozytorium:  
   ```bash
   git clone https://github.com/Adam-Sidor/ADMleds_PC
   ```
2. Utwórz plik `config.txt` i zapisz do niego adresy IP [kontrolerów](https://github.com/Adam-Sidor/ADMleds_ESP32):
    ```
    IP:[adresIP1;adresIP2]
    ```
3. Ustaw odpowiednią ścieżkę do pliku `config.txt` w pliku `auto_on.py` w lini:
    ```Python
    IPs = readIPs("Your file path")
    ```

---

## Użycie
1. Bash:
    ```bash
    python auto_on.py
    ```
2. Startup (Opcjonalnie):
    1. Naciśnij `Win + R` i wpisz `shell:startup`.
    2. Umieść skrót do skryptu `auto_on.py`.


---

## Funkcjonalności
- Skrypt na PC pozwala na włączanie kilku urządzeń jednocześnie.
- Automatyczne czekanie na połączenie z siecią.

---

## Licencja
Wszystkie prawa zastrzeżone. Projekt został udostępniony wyłącznie w celach demonstracyjnych i edukacyjnych.  
- Możesz korzystać z tego projektu do użytku osobistego i edukacyjnego.  
- Wykorzystanie komercyjne lub redystrybucja projektu w całości lub w części wymaga wyraźnej pisemnej zgody autora.

---

## Kontakt
- Autor: Adam Sidor  
- E-mail: sidoadsi1@gmail.com  
- LinkedIn: [Mój profil](https://www.linkedin.com/in/adam-sidor-088a56341)  
