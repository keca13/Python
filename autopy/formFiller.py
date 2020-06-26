#! python3
# https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform
# formFiller.py - Automatycznie wypełnia formularz sieciowy.

import pyautogui, time

# Zdefiniowanie odpowiednich współrzędnych we własnym komputerze.
nameField = (388, 392)
submitButton = (413, 645)
submitButtonColor = (75, 141, 249)
submitAnotherLink = (760, 224)

formData = [{'name': 'Alicja', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Powiedz Bobowi, że mówię mu cześć.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Karol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Proszę zabrać kukiełki z pokoju.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Chronić niewinnych. Służyć społeczeństwu. Stać na straży prawa.'},
            ]

pyautogui.PAUSE = 0.5

for person in formData:
    # Umożliwienie użytkownikowi zakończenia działania skryptu.
    print('>>> 5-SEKUNDOWA PRZERWA POZWALAJĄCA UŻYTKOWNIKOWI NACISNĄĆ CTRL-C <<<')
    time.sleep(5)

    # Zaczekanie na wczytanie strony formularza sieciowego.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)

    print('Wprowadzenie informacji o osobie %s...' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])

    # Wypełnienie pola Name.
    pyautogui.typewrite(person['name'] + '\t')

    # Wypełnienie pola Greatest Fear(s).
    pyautogui.typewrite(person['fear'] + '\t')

    # Wypełnienie pola Source of Wizard Powers.
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

    # Wypełnienie pola RoboCop.
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # Wypełnienie pola Additional Comments.
    pyautogui.typewrite(person['comments'] + '\t')

    # Kliknięcie przycisku Prześlij.
    pyautogui.press('enter')

    # Zaczekanie na wczytanie strony.
    print('Kliknięto przycisk Prześlij.')
    time.sleep(5)

    # Kliknięcie łącza "Submit another response".
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
