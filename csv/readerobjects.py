import csv
# konstrukcja *with* pozwala na otworzenie pliku i korzystanie z niego wewnątrz niej
# po jej opuszczeniu automatycznie zamknie strumień odczytu
with open('test.csv', 'r',  encoding='utf-8') as csvfile:
    # deklarujemy nasz *czytacz*
    # parametr *delimiter* jest opcjonalny i wskazuje jaki został w pliku użyty separator
    csvreader = csv.reader(csvfile, delimiter=',')
    #csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:
        print(row[0]) # wartość kolumny 1 z tego wiersza
        print(row[1]) # analogicznie - 2 kolumna
        #print(row['kolumna 3']) # 3cia
