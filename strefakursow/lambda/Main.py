dodaj = lambda a,b: a+b
print(dodaj(30,30))

lista = [dodaj(x,y) for x,y in ([20,20],[40,40])]
print(lista)

#Domknięcia

def make_incrementor(n):
    return lambda x: x+n

dodaj200 = make_incrementor(200)
print(dodaj200(50))

#Sortowanie

kwadrat_liczby = sorted(range(-5,13),key = lambda x: x**2)
print(kwadrat_liczby)