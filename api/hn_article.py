# -*- coding=cp1250 -*-
#http://news.ycombinator.com
import requests
import json

#Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'

r = requests.get(url)
print(f"Kod stanu: {r.status_code}")

#Analiza struktur danych

response_dict = r.json()
readable_file = 'hn_data2.json'

with open(readable_file, 'w') as f:
	json.dump(response_dict, f, indent=4)