# inventory.py
stuff = {'lina': 1, 'pochodni': 6, 'złote monety': 42, 'sztylet': 1, 'strzał': 12}

def display_inventory(inventory):
    print("Inwentarz:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Całkowita liczba przedmiotów: " + str(item_total))

display_inventory(stuff)
