def isPhoneNumber(text):
    if len(text) != 12:
        return False  # Liczba znaków nieodpowiada numerowi telefonu.
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # To nie jest numer kierunkowy.
    if text[3] != '-':
        return False  # Brak pierwszego myślnika.
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # Brak trzech pierwszych cyfr.
    if text[7] != '-':
        return False  # Brak drugiego myślnika.
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # Nie ma czterech ostatnich cyfr.
    return True  # "text" jest numerem telefonu!

print('415-555-4242 to jest numer telefonu:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi to jest numer telefonu:')
print(isPhoneNumber('Moshi moshi'))
