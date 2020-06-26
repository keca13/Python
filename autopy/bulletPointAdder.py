#! python3
# Na początku każdego wiersza tekstu znajdującego się w schowku
# dodaje gwiazdki tworzące listę wypunktowaną w artykule Wikipedii.

import pyperclip
text = pyperclip.paste()

# Rozdzielić poszczególne wiersze i dodać gwiazdki.
lines = text.split('\n')
for i in range(len(lines)): # Iteracja przez wszystkie indeksy listy "lines".
    lines[i] = '* ' + lines[i] # Dodanie gwiazdki do każdego ciągu tekstowego na liście "lines".
text = '\n'.join(lines)
pyperclip.copy(text)
