from example import *

print("Witaj w programie do obsługi gości hotelowych")

wybor = -1



while(wybor != 0):
	wybor = int(input("\nWybierz opcje:\n1-dodaj nowego goscia\n2-usun goscia\n3-znajdz goscia\n0-zakoncz dzilanie programu\n -> : "))


	if (wybor == 1):
		dodajGoscia()
	elif (wybor == 2):
		nazwisko = input("\nPodaj nazwisko usuwanego goscia: ")
		usunGoscia(nazwisko)
	elif(wybor == 3):
		nazwisko = input("\nPodaj nazwisko szukanego goscia: ")
		szukajGoscia(nazwisko)
	elif(wybor < 0 or wybor > 3):
		print("Nie ma takiej opcji")

	print("\nDziękuje za skorzystanie z mojego programu")
