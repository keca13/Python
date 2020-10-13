#https://pythoninoffice.com/split-and-merge-pdf-using-python/

from PyPDF4 import PdfFileReader, PdfFileWriter
import sys
#os.getcwd()
file_in = sys.argv[1]
#file_out = sys.argv[2]
#pdf = PdfFileReader(r'C:\Users\jacek\Downloads\referencje jacek(1).pdf')
pdf = PdfFileReader(file_in)
pdf.numPages
pdf.getDocumentInfo()
#pdf.getPage(1)
pdf_writer = PdfFileWriter()
#give a page number
page_number = int(input('Please give page number to split:'))
#pdf_writer.addPage(pdf.getPage(0))

pdf_writer.addPage(pdf.getPage(page_number))
file_out = input('name file out:')
#with open(r'E:\\python\\mytest\\myapp\\referencje_algo.pdf', 'wb') as f:
    #pdf_writer.write(f)
with open(file_out, 'wb') as f:
    pdf_writer.write(f)
