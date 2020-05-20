import sqlite3

nazwaBazyDanych = "test.db"

def otworzPolaczenie():
    global polaczenie
    polaczenie = sqlite3.connect(nazwaBazyDanych)

def zamknijPolaczenie():
    polaczenie.close()

def dodajSamochod():
    marka = input("Podaj marke samochodu: ")
    model = input("Podaj model samochodu: ")
    rocznik = input("Podaj rocznik samochodu: ")
    zapytanie = "INSERT INTO tabela VALUES ('" + marka + "','" + model + "', '" + rocznik + "')"
    print(zapytanie)
    polaczenie.execute(zapytanie)
    polaczenie.commit()

def usunSamochod():
    marka = input("Podaj marke samochodu: ")
    model = input("Podaj model samochodu: ")
    rocznik = input("Podaj rocznik samochodu: ")
    zapytanie = "DELETE FROM tabela WHERE marka='"+ marka +"' AND model='"+ model +"'AND rocznik="'+ rocznik'
    polaczenie.execute(zapytanie)
    polaczenie.commit()

def wyszukajSamochod():
    kursor = polaczenie.cursor()
    marka = input("Podaj marke samochodu: ")
    model = input("Podaj model samochodu: ")
    rocznik = input("Podaj rocznik samochodu: ")
    zapytanie = "SELECT * FROM tabela WHERE marka='"+ marka +"' AND model='"+ model +"' AND rocznik=" '+ rocznik'
    kursor.execute(zapytanie)
    
#print(kursor.fetchone())
