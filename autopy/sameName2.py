def spam():
    global eggs
    eggs = 'spam'

eggs = 'zmienna globalna'
spam()
print(eggs)
