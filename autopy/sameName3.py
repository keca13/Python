def spam():
    global eggs # To jest zmienna globalna.
    eggs = 'spam'

def bacon():
    eggs = 'bacon' # To jest zmienna lokalna.

def ham():
    print(eggs) # To jest zmienna globalna.

eggs = 42 # To jest zmienna globalna.
spam()
print(eggs)
