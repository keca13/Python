catNames = []
while True:
    print('Podaj imię kota numer ' + str(len(catNames) + 1) + ' (Ewentualnie nic nie wpisuj, aby zakończyć.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # Konkatenacja listy.
print('Oto imiona kotów:')
for name in catNames:
    print('  ' + name)
