#! python3
# readCensusExcel.py - Przygotowuje dane dotyczące populacji
# i obszarów geograficznych spisu powszechnego w poszczególnych hrabstwach.

import openpyxl, pprint
print('Otwieranie skoroszytu...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}
# Umieszczenie w countyData wielkości populacji i liczby obszarów geograficznych spisu powszechnego.
print('Odczyt wierszy...')
for row in range(2, sheet.get_highest_row() + 1):
    # Każdy wiersz w arkuszu kalkulacyjnym zawiera dane dla jednego obszaru geograficznego spisu powszechnego.
    state  = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop    = sheet['D' + str(row)].value

    # Upewniamy się, że istnieje klucz dla danego stanu.
    countyData.setdefault(state, {})
    # Upewniamy się, że istnieje klucz dla danego hrabstwa w tym stanie.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Każdy wiersz przedstawia jeden obszar geograficzny, więc przeprowadzamy inkrementację o 1.
    countyData[state][county]['tracts'] += 1
    # Populację hrabstwa zwiększamy o populację w tym obszarze geograficznym spisu powszechnego.
    countyData[state][county]['pop'] += int(pop)

# Otworzenie nowego pliku tekstowego i zapis w nim zawartości struktury danych countyData.
print('Zapis wyników...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Gotowe!')
