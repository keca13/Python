# To jest gra typu "odgadnij liczbę".
import random
secretNumber = random.randint(1, 20)
print('Mam na myśli pewną liczbę z zakresu od 1 do 20.')

# Sześciokrotnie prosimy gracza o odgadnięcie liczby.
for guessesTaken in range(1, 7):
    print('Spróbuj odgadnąć liczbę.')
    guess = int(input())

    if guess < secretNumber:
        print('Podana liczba jest za mała.')
    elif guess > secretNumber:
        print('Podana liczba jest za duża.')
    else:
        break # Ten warunek dotyczy sytuacji, w której gracz odgadł liczbę!

if guess == secretNumber:
    print('Doskonale! Odgadłeś liczbę w ciągu ' + str(guessesTaken) + ' prób!')
else:
    print('Nie udało się. Liczba, którą miałem na myśli to ' + str(secretNumber) + '.')
