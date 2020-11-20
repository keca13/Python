basket = []
shop_shelf = ['banany','jablka','cytryny','ziemniaki', 'cebula']

goods = len(shop_shelf) -1

print('What is in your shop')
for i in shop_shelf:
    print(i, end=',')


watching_goods = 0
print(goods)
while watching_goods <= goods:
    print('You take this product {} in your hand '.format(shop_shelf[watching_goods]))
    decision = input('Do you want take this product do hand?')
    if decision == 'YES':
        basket.append(shop_shelf[watching_goods])
        shop_shelf[watching_goods] = ''
    watching_goods += 1

print('What is in your basket: ')
for i in basket:
    print(i, end=', ')

print('\nWhat is in your shop: ')
for i in shop_shelf:
    print(i, end=', ')

print('')
