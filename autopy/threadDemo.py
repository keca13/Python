import threading, time
print('Uruchomienie programu.')

def takeANap():
    time.sleep(5)
    print('Obudź się!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('Zakończenie programu.')
