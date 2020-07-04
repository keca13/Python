#! python3

import pdfkit as pdf
import pandas as pd
import bbb2


#from csv to html and pdf

bbb2.openfile()

OUTFILE_PDF = "bbb.pdf"

OUTFILE_HTML = "bbb.html"


file01 = input('CSV file: >>>')
en = pd.read_csv(file01, dtype='unicode', index_col=False)

print(en)


www = en.to_html(index=False)
#print(www)
print("#next step")

www_file = open("bbb.html", "w")
www_file.write(www)
www_file.close()



pdf.from_file(OUTFILE_HTML, OUTFILE_PDF)
