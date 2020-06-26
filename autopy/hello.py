# Ten program wyświetla powitanie i prosi o podanie imienia.

print('Witaj, świecie!')
print('Jak masz na imię?') # Prośba o podanie imienia.
myName = input()
print('Miło Cię poznać, ' + myName + '.')
print('Liczba znaków w Twoim imieniu wynosi:')
print(len(myName))
print('Ile masz lat?') # Prośba o podanie wieku.
myAge = input()
print('Za rok będziesz mieć ' + str(int(myAge) + 1) + ' lat.')
