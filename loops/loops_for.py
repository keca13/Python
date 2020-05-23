# petla for używana do przeglądania danych iterowalnych, takie jak łańcuchy znaków, lista, kratka czy słownik.
# Petle zagnieżdzone
#1
lista1 = [1,2,3,4]
lista2 = [6]
sum = []
for i in lista1:
  for j in lista2:
    sum.append(i + j)
print(sum)

#2
for i in range(1,5):
  print(i)
  for letter in ["a","b","c"]:
    print(letter)
    

#prosty przykład
s = "Some Text"
cnt = 0

for c in s:
    if c == "e":
        cnt = cnt + 1
print("found", cnt, "'e'")

#przykłady na plikach
import json
import pickle
import pprint


#przykłąd z zastosowaniem danych słownika zapisanych pliku txt w formacie json
with open("dane.txt", "r") as plik:
        dane_plik = json.load(plik)
        pprint.pprint(dane_plik)
        cnt = 0
        g = input("szukana wartosc: ")

        for c in dane_plik:
            if c == g:
                #liczy ie wartosci
                cnt = cnt + 1
        print("found", cnt, g)
        g =dane_plik[g]
        print(g)

#przykład z zastosowaniem danych słownika zapisanych pliku w formacje binarnym
with open("dane", "rb") as plik:
        dane_plik = pickle.load(plik)
        pprint.pprint(dane_plik)
        cnt = 0
        g = input("szukana wartosc: ")

        for c in dane_plik:
            if c == g:
                #liczy ie wartosci
                cnt = cnt + 1
        print("found", cnt, g)
        g =dane_plik[g]
        print(g)

