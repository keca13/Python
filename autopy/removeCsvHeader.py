#! python3
# removeCsvHeader.py - Usunięcie nagłówka ze wszystkich plików CSV
# znajdujących się w bieżącym katalogu roboczym.

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Iteracja przez wszystkie pliki w bieżącym katalogu roboczym.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # Pominięcie wszystkich plików w formacie innym niż CSV.

    print('Usuwanie nagłówka z pliku ' + csvFilename + '...')

    # Odczyt pliku CSV (z pominięciem pierwszego wiersza).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # Pominięcie pierwszego wiersza.
        csvRows.append(row)
    csvFileObj.close()

    # Zapis pliku CSV.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
