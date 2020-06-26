import random

messages = ['To pewne',
    'Zdecydowanie tak',
    'Tak',
    'Niejasna odpowiedź, spróbuj ponownie',
    'Zapytaj ponownie później',
    'Skoncentruj się i zapytaj ponownie',
    'Moja odpowiedź brzmi nie',
    'To nie wygląda zbyt dobrze',
    'Bardzo wątpliwe']

print(messages[random.randint(0, len(messages) - 1)])
