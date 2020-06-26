def spam():
    print(eggs) # BŁĄD!
    eggs = 'Zmienna lokalna funkcji spam().'

eggs = 'global'
spam()
