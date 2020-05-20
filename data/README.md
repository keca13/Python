# py_bd_001 / info dla plikow bazadanych.py i bazydanych
# tworzymy baze test.db

# pobieramy i rozpakowujemy ze strony https://sqlite.org/download.html: sqlite-tools-win32-x86-*zip dla windows 
# pobieramy i instalujemy ze strony https://sqlitestudio.pl/index.rvt?act=download sqlite studio

# przypisujemy zmienna srodowiskowa do folderu gdzie znajduje sie plik sqlite3.exe

$>sqlite3 test.db

# po zalogowaniu sie do sqlite wybieramy baze .databases
sqlite>.databases

# tworzymy tabele wraz z kolumnami
create table tabela(marka varchar(30), model varchar(30), rocznik int);
.quit
