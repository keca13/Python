def spam():
    eggs = 'Zmienna lokalna funkcji spam().'
    print(eggs)    # Wyświetla 'Zmienna lokalna funkcji spam().'

def bacon():
    eggs = 'Zmienna lokalna funkcji bacon().'
    print(eggs)    # Wyświetla 'Zmienna lokalna funkcji bacon().'
    spam()
    print(eggs)    # Wyświetla 'Zmienna lokalna funkcji bacon().'

eggs = 'Zmienna globalna.'
bacon()
print(eggs)        # Wyświetla 'Zmienna globalna.'
