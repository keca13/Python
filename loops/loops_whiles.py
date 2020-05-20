
def koszta():
	utrzymanie = 0
	i = 0
	centrale = 0
	while i <= 11:
		centrale = centrale + 29
		utrzymanie = utrzymanie + 10
		i = i + 1
		print("Suma utrzymanie: ",utrzymanie ,"Suma centrale: ", centrale)



a =  input('Chcesz wiedziec ile zaplacisz za VoIP przez rok, t czy n?')
  
if a == 'n':
	print("ok bye")
else:
	koszta()
	print("Przemyslales? call  me 483801010")

