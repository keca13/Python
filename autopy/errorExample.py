def spam():
    bacon()

def bacon():
    raise Exception('To jest komunikat błędu.')

spam()
