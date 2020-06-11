import pickle
import re

#text = """ Żyrafy od samego _Rzeczownik__lpoj__"""

with open('data.txt', 'r') as file:
	contents = file.read()


#line = "Kocham $"
szukany = input("Czego szukasz: ")
zmiana = input("Zmiana na: ")

#m = re.findall("\\$",contents,re.IGNORECASE)
m = re.findall(szukany,contents,re.IGNORECASE)
d = contents.replace(szukany,zmiana)

print(m)
#print(d)


#zapisujemy liste wyszukanych elementów
with open("date3.txt", "wb") as plik3:
	pickle.dump(m,plik3)

#zapisujemy zmiane w nowym pliku
with open("date4.txt", "w") as plik3:
	plik3.write(d)