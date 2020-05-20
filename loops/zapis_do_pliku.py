# zapis do pliku dzieki pętli while  z operatorem logicznym
# oraz instrukcji warunkowej IF

plik = open("dane.txt", "w")

while True:
	wiersz = input("wpisz wiersz do zapisania: ")

    #puste pole w input i nacisniecie enter spowoduje 
	if wiersz =='':
		print("Koniec zapisywania w pliku.")
		break
	else:
		plik.write(wiersz)
		plik.write("\n")

plik.close()
