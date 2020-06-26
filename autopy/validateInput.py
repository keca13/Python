while True:
    print('Podaj swój wiek:')
    age = input()
    if age.isdecimal():
        break
    print('Wiek musi być podany w postaci liczby.')

    while True:
        print('Wybierz nowe hasło (jedynie litery i cyfry):')
        password = input()
        if password.isalnum():
            break
        print('Hasło może składać się jedynie z liter i cyfr.')