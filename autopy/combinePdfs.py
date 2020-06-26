#! python3
# combinePdfs.py - Połączenie wszystkich dokumentów PDF
# w bieżącym katalogu roboczym w jeden plik w formacie PDF.

import PyPDF2, os

# Pobranie wszystkich plików w formacie PDF.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Iteracja przez wszystkie pliki w formacie PDF.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Iteracja przez wszystkie (poza pierwszą) strony i dodanie ich do wynikowego dokumentu PDF.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Zapis wynikowego dokumentu PDF w pliku.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
