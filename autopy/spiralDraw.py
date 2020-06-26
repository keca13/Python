import pyautogui, time
time.sleep(5)
pyautogui.click() # Kliknięcie w celu aktywacji programu.
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2) # Przesunięcie kursora myszy w prawo.
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2) # Przesunięcie kursora myszy w dół.
    pyautogui.dragRel(-distance, 0, duration=0.2) # Przesunięcie kursora myszy w lewo.
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)  # Przesunięcie kursora myszy w górę.