from bazydanych import *

wybor = -1

otworzPolaczenie()

while(wybor != 0):
    wybor = int(input("Dokonaj wyboru:\n1-dodaj auto\n2-usun auto\n3-wyszukaj auto\n0-wyjdz z programu\n -> : "))
    if (wybor == 1):
        dodajSamochod()
    elif (wybor ==2):
        usunSamochod()
    elif (wybor == 3):
        wyszukajSamochod()
    elif (wybor < 0 or wybor > 3):
        print("Nie ma takiej opcji!")

zamknijPolaczenie()
