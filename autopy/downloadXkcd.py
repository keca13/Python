#! python3
# downloadXkcd.py - Pobiera wszystkie komiksy opublikowane w witrynie XKCD.

import requests, os, bs4

url = 'http://xkcd.com' # Początkowy adres URL.
os.makedirs('xkcd', exist_ok=True) # Komiksy są przechowywane w katalogu ./xkcd.
while not url.endswith('#'):
    # Pobranie strony.
    print('Pobranie strony %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Ustalenie adresu URL pliku obrazu komiksu.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Nie udało się odnaleźć pliku obrazu komiksu.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Pobranie obrazu.
        print('Pobranie obrazu %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Zapis obrazu w katalogu ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Pobranie adresu URL w przycisku Prev.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Gotowe!')
