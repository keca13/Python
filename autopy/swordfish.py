while True:
    print('Kim jesteś?')
    name = input()
    if name != 'Janek':
        continue
    print('Witaj, Janek! Jakie jest hasło? (To nazwa ryby).')
    password = input()
    if password == 'miecznik':
        break
print('Masz dostęp.')