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
    
