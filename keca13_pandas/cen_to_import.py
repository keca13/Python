import pandas as pd


#wczytujemy cen IPCALL
file01 = input('IPcall file: >>>')
file02 = input('Netia file: >>>')

cen = pd.read_csv(file01, dtype='unicode', index_col=False)

#oddzielamy czesc polska cennika
#cen.head(3252)
cen_pol = cen.head(3252)
cen_pol.to_csv('cen_pol_test.csv', index = False)
#wczytujemy cen Netia

cen_netia = pd.read_csv(file02, dtype='unicode', index_col=False)
#cen_netia.columns.tolist()
#change plase columns cen netia
cen_netia = cen_netia[['Prefix', 'Destination', 'Rate Euro/min']]
#cen_netia.to_csv('csv\ipcall\cen_netia.csv', index = False, header=False)
#w kolumnie "Rate %" zamieniamy comma na dot
cen_netia['Rate Euro/min'] = (cen_netia['Rate Euro/min'].replace(',', '.', regex=True).astype(float))
#cen_netia.to_csv('csv\ipcall\cen_netia.csv', index = False, header=False)

# objekt przydatny jesli kolumna "prefix" jest bez prefixu 00 w innym razie zakomentowac
cen_netia['prefix'] = ('00' + cen_netia['prefix'])


#zmiana nazwy kolumn
cen_netia.rename(columns={'Prefix': 'prefix'}, inplace=True)
cen_netia.rename(columns={'Destination': 'description'}, inplace=True)
cen_netia.rename(columns={'Rate Euro/min': 'voice_rate'}, inplace=True)


#Series Object
#rate_netia = cen_netia['Rate Euro/min']
#cen_netia.columns.to_list()
cen_netia['from_day'] = 0
cen_netia['to_day'] = 6
cen_netia['from_hour'] = 0
cen_netia['to_hour'] = 2400
cen_netia['grace_period'] = 0
cen_netia['minimal_time'] = -1
cen_netia['resolution'] = -1
cen_netia['rate_multiplier'] = -1
cen_netia['rate_addition'] = -1
cen_netia['surcharge_time'] = -1
cen_netia['surcharge_amount'] = -1.0000
cen_netia['free_seconds'] = 0
cen_netia['country_code'] = 'PL'
#cen_netia.dtypes

#cen_netia
#cen_netia['voice_rate'] = cen_netia['voice_rate'].astype('float64')
#cen_netia.dtypes
#should by 'voice_rate' as float64
cen_netia['voice_rate'] = cen_netia['voice_rate'] * 8
cen_netia.to_csv('cen_netia_test.csv', index=False)

#cen_netia
#dodajemy da cenniki
all_cen = cen_pol.append(cen_netia)
#all_cen
#all_cen.dtypes
#usuwamy wiersze z POLAND
#exportujemy docelowy cen
all_cen.to_csv('Export_all_cen_test.csv', index=False)
#select-by-partial-string-from-a-pandas-dataframe
#poland = all_cen[all_cen['description'] == 'POLAND (OLO)'].index
#or
poland = all_cen[all_cen['description'].str.contains("POLAND")].index
all_cen.drop(poland, inplace=True)

file03 = input('Output file in csv format: >>>')

all_cen.to_csv(file03, index=False)

all_cen.to_csv('Export_all_cennik_test2.csv', index=False)
all_cen[['prefix', 'description', 'voice_rate']].to_csv('web.csv', index=False)



print('Check your file: ', file03, 'web.csv')
