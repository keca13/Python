import pandas as pd


#wczytujemy cen IPCALL
file01 = input('CSV file: >>>')

cen = pd.read_csv(file01,usecols = ['prefix', 'description', 'voice_rate'], dtype='unicode', index_col=False)
cen_short = cen.head(3252)
html = cen_short.to_html(index=False)
print(html)
#html = html[['prefix', 'description', 'voice_rate']]

www_file = open("cennik3.html", "w")
www_file.write(html)

www_file.close()
