birthdays = {'Alicja': '1 kwiecień', 'Bob': '12 grudzień', 'Karol': '4 marzec'}

while True:
    print('Podaj imię: (pozostaw puste, aby zakończyć program)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' to dzień urodzin osoby o imieniu ' + name + '.')
    else:
        print('Nie znaleziono informacji o urodzinach osoby o imieniu ' + name + '.')
        print('Kiedy przypadają te urodziny?')
        bday = input()
        birthdays[name] = bday
        print('Baza danych urodzin została uaktualniona.')
