# Function use for take goods for basket and return basket
def shopping(section=[]):
    goods = len(section)
    basket = []
    watching_goods = 0
    
    while watching_goods < goods:
        print('You take it in your hand: {}'.format(section[watching_goods]))
        decision = input('Do you want to put this product y/n: ')
        if decision == 'y':
            basket.append(section[watching_goods])
            section[watching_goods] = ''
        watching_goods += 1
    return basket

# Function use arguments as *basket
def cash_register(*argv):
    if argv is not None:
        for iarg in argv:
            for good in iarg:
                print(good, end=', ')
    print('')

shop_shelf1 = ['apple', 'Orange', 'Kiwi']
shop_shelf2 = ['Toy car', 'Toy Train', 'Toy Helicopter']

basket1 = shopping(shop_shelf1)
basket2 = shopping(shop_shelf2)

cash_register(basket1, basket2)