myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Podaj imię zwierzaka:')
name = input()
if name not in myPets:
    print('Nie mam zwierzaka o imieniu ' + name)
else:
    print(name + ' to mój zwierzak.')
