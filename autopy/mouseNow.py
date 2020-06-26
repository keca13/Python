#! python3
# mouseNow.py - Wyświetla bieżące położenie kursora myszy.
import pyautogui
print('Naciśnij klawisze Ctrl+C, aby zakończyć działanie programu.')
try:
    while True:
        # Pobranie i wyświetlenie współrzędnych kursora myszy.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nGotowe!')
