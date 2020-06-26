def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol musi być pojedynczym znakiem.')
    if width <= 2:
        raise Exception('Szerokość musi mieć wartość większą niż 2.')
    if height <= 2:
        raise Exception('Wysokość musi mieć wartość większą niż 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('Nastąpiło zgłoszenie wyjątku: ' + str(err))
