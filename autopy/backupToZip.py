#! python3
# backupToZip.py - Katalog wraz z całą zawartością zostaje umieszczony
# w archiwum ZIP, którego nazwa jest inkrementowana za każdym razem.

import zipfile, os

def backupToZip(folder):
    # Umieszczenie w archiwum ZIP całej zawartości katalogu.

    folder = os.path.abspath(folder) # Upewniamy się, że otrzymaliśmy bezwzględną ścieżkę dostępu do katalogu.

    # Ustalenie nazwy pliku, jaka powinna zostać użyta
    # przez kod na podstawie istniejących plików.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Utworzenie archiwum ZIP.
    print('Tworzenie archiwum %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Przejście przez całe drzewo katalogu i kompresja plików we wszystkich podkatalogach.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Dodawanie plików w %s...' % (foldername))
        # Dodanie bieżącego katalogu do archiwum ZIP.
        backupZip.write(foldername)

        # Dodanie wszystkich plików znajdujących się w tym katalogu do archiwum ZIP.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # W archiwum nie umieszczamy plików innych archiwów.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Gotowe!')


backupToZip('C:\\delicious')
