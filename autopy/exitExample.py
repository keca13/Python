import sys
while True:
    print('Wpisz exit, aby zakończyć działanie programu.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('Wpisałeś ' + response + '.')