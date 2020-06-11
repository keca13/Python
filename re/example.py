import re

#text = """ Żyrafy od samego _Rzeczownik__lpoj__"""

with open('data.txt', 'r') as file:
	contents = file.read()

def mad_libs(mls):
	"""
	:param mls: Łancuch znaków,
	__to_sugestia__,tylko __sugestia__."""

	a = input("szukane słowo: ")
	hints = re.findall(a,mls)
	#hints = re.findall("\\$",mls,re.IGNORECASE)

	if hints is not None:
		for word in hints:
			q = "Zamieniamy {} na:".format(word)
			new = input(q)
			mls = mls.replace(word,new)
			#mls = mls.replace(word,new,re.MULTILINE)
			print('\n')
			#mls = mls.replace("\n","")
			print(mls)
			with open('data2.txt','w') as file2:
				file2.write(mls)
			break
	else:
		print("Nieprawidłowy parametr mls")

mad_libs(contents)


