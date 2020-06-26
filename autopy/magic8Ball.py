import random

def getAnswer(answerNumber):
    if answerNumber == 1:
       return 'To pewne'
    elif answerNumber == 2:
        return 'Zdecydowanie tak'
    elif answerNumber == 3:
        return 'Tak'
    elif answerNumber == 4:
        return 'Niejasna odpowiedź, spróbuj ponownie'
    elif answerNumber == 5:
        return 'Zapytaj ponownie później'
    elif answerNumber == 6:
        return 'Skoncentruj się i zapytaj ponownie'
    elif answerNumber == 7:
        return 'Moja odpowiedź brzmi nie'
    elif answerNumber == 8:
        return 'To nie wygląda zbyt dobrze'
    elif answerNumber == 9:
        return 'Bardzo wątpliwe'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
