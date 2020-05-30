# -*- coding: utf-8 -*-
#http://news.ycombinator.com
from operator import itemgetter
import requests
import json
#Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)
print(f"Kod stanu: {r.status_code}")


#Przetwarzanie informacji o każdym artykule.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:1]:
	#Przygotowanie oddzielnego wywołania API dla każdego artykułu
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	#print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()
	print(response_dict)

	#Utworzenie słownika dla każdego artykułu
	submission_dict = {
		'title':response_dict['title'],
		'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
		'comments': response_dict['descendants'],
		}

	submission_dicts.append(submission_dict)


submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse=True)

print(submission_dict)

for submission_dict in submission_dicts:
	print(f"\nTytul artykulu: {submission_dict['title']}")
	print(f"\nlacze do dyskusji: {submission_dict['hn_link']}")
	print(f"\nLiczba komentarzy: {submission_dict['comments']}")

readable_file = 'hn_data.json'
with open(readable_file, 'w') as f:
	json.dump(submission_dicts, f, indent=4)