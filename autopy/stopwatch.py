#! python3
# stopwatch.py - Prosty program stopera.

import time

# Wyświetlenie informacji o sposobie działania programu.
print('Naciśnij Enter, aby rozpocząć. Kolejne naciśnięcie Enter oznacza nowe okrążenie. Naciśnięcie Ctrl+C kończy działanie programu.')
input() # Naciśnij Enter, aby rozpocząć.
print('Rozpoczęto działanie.')
startTime = time.time() # Pobranie godziny rozpoczęcia pierwszego okrążenia.
lastTime = startTime
lapNum = 1

# Rozpoczęcie pomiaru czasu okrążenia.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Okrążenie #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # Wyzerowanie czasu ostatniego okrążenia.
except KeyboardInterrupt:
    # Obsługa wyjątku zgłaszanego po naciśnięciu klawiszy Ctrl+C. Dzięki temu
    # nie będzie wyświetlony komunikat błędu.
    print('\nGotowe!')
