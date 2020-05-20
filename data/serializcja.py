import pickle
import os

def zapiszDane():
	with open("daneGosci", "wb") as plik:
		pickle.dump(daneFosci, plik)


def odczytajDane():
	daneGosci = []
	statinfo = os.stat("daneGosci")
	if (statinfo.st_size == 0):
		return daneGosci
	try:
		with open("daneGosci","rb") as plik:
			daneGosci = pickle.load(plik)
	except EOFError:
		print("plik jest pusty")
	return daneGosci
