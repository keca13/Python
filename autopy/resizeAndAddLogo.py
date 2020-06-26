#! python3
# resizeAndAddLogo.py - Zmiana wielkości wszystkich obrazów w bieżącym katalogu
# roboczym, aby mieściły się w kwadracie o wymiarach 300 na 300 pikseli.
# Następnie w prawym dolnym rogu będzie umieszczone logo catlogo.png.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Iteracja przez wszystkie pliki w bieżącym katalogu roboczym.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or filename == LOGO_FILENAME:
        continue # Pominięcie plików innych niż obrazy oraz obrazu o nazwie pliku takiej samej jak logo.

    im = Image.open(filename)
    width, height = im.size

    # Sprawdzenie, czy konieczna jest zmiana wielkości obrazu.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Obliczenie nowej szerokości i wysokości obrazu.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Zmiana wielkości obrazu.
        print('Zmiana wielkości obrazu %s...' % (filename))
        im = im.resize((width, height))

    # Dodanie logo.
    print('Dodanie logo do obrazu %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Zapis wprowadzonych zmian.
    im.save(os.path.join('withLogo', filename))
