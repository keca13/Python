
# -*- coding=cp1250 -*-
import requests

#Wykonywanie wywołania API i zachowanie otrzymanej odpowiedzi
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
print(f"Kod stanu: {r.status_code}")

#Umieszczanie odpowiedzi API w zmiennej
response_dict = r.json()

print("Klucze ze słownika response_dict: ",response_dict.keys())
print(f"Całkowita liczba repozytoriów: {response_dict['total_count']}")

#Przetworzenie informacji o repozytoriach
repo_dicts = response_dict['items']
print(f"Liczba zwróconych repozytoriów: {len(repo_dicts)}")

#Przeanalizowanie drugiego repozytorium
repo_dict = repo_dicts[1]
print(f"\nKlucze: {len(repo_dict)}")

for key in sorted(repo_dict.keys()):
	print(key)

#print(f"\nWybrane informacje o pierwszym repozytorium\n")
#count = 0
#for repo_dict in repo_dicts:
	#count = count + 1
	#print(count)
	#print(f"Nazwa: {repo_dict['name']}")
	#print(f"Właściciel: {repo_dict['owner']['login']}")
	#print(f"Gwiazdki: {repo_dict['stargazers_count']}")
	#print(f"Repozytorium: {repo_dict['html_url']}")
	#print("---------------")
	#print(f"Utworzone: {repo_dict['created_at']}")
	#print(f"Uaktualnione: {repo_dict['updated_at']}")
	#print(f"Opis: {repo_dict}['description']")

