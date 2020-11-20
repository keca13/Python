## Katalog alikacji

mkdir learning_log

cd learning_log



## tworzymy wirtualne srodowisko venv o dowolnej nazwie (ll_env)

#ni README.txt  #ni like touch in powershell

python -m venv ll_env
or
C:\python37\python -m venv ll_env

#To activate venv

source ll_env/bin/activate # in UNIX system

.\env37\Scripts\activate.ps1 # in windows powershell



## Instalacja Framework Django

pip install django

pip
## Tworznie projektu

.\ll_env\Scripts\activate.ps1

django-admin startproject learning_log .




#requirements

.\ll_env\Scripts\activate.ps1

pip freeze > requirements.txt

#.gitignore

ni/touch .gitignore # ll_env/



## add git repository
#https://marklodato.github.io/visual-git-guide/index-pl.html

git add files - kopiuje pliki (w ich aktualnym stanie) do przechowalni (stage).
git commit zapisuje migawkę (snapshot) przechowalni (stage) jako nowy commit.
git reset -- files usuwa pliki z przechowalni (stage); oznacza to, że komenda ta kopiuje pliki z ostatniego commita do przechowalni (stage), nadpisując jej stan. Używa się jej między innymi do "cofania" komendy git add files. Komendy git reset można użyć również do całkowitego usunięcia wszystkich zmian.
git checkout -- files kopiuje pliki z przechowalki (stage) do katalogu roboczego (working directory). Komendy tej używa się do cofnięcia wszelkich zmian lokalnych.

git commit -a automatycznie dodaje zmiany ze wszystkich znanych plików (dotyczy to zarówno git add jak i git rm dla plików usuniętych z katalogu roboczego (working directory)), a następnie wykonuje komendę git commit.
git commit files tworzy nowy commit, który zawiera całą zawartość ostatniego commita oraz migawkę (snapshot) wybranych plików. Oczywiście pliki kopiowane są również do przechowalni (stage).
git checkout HEAD -- files kopiuje pliki z ostatniego commita zarówno do przechowalni (stage) jak i katalogu roboczego (working directory).

git --help

git init

git status -s

git diff

git diff --staged

git add .

git status

git commit -m "wpisz commit"

git status

git log

#przywracanie stanu

git log

git checkout 0a16ab02c0ddbb6e3c4881f6e6e2e5c4874fa083

git stat
#usuwanie pliku

git rm PROJECTS.md

# usuwanie po  git add . bez commit
git rm -rf --cached .
git add .



#Zmiana nazwy pliku

git mv README.txt README.md

#usuwanie zmian po git add .
git rm --cached <file>





## Utworzenie Bazy danych sqlite3
python manage.py check
python manage.py migrate
python manage.py makemigrations app

python manage.py migrate

python manage.py createsuperuser



## Przegladanie projektu

python .\manage.py runserver

http://127.0.0.1:8000/



## Uruchamianie aplikacji

python manage.py startapp app

python manage.py makemigrations app

python manage.py migrate



## Uruchamianie konsoli

python manage.py shell


## dodatkowe pliki
python --version > runtime.txt
pip freeze > .\requirements.txt

## heroku
heroku create
heroku login -i
git push heroku master
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku run python manage.py shell
heroku run bash
heroku apps:rename learning-log-13
heroku pg:backups capture
heroku pg:backups download
heroku addons
heroku pg:infi