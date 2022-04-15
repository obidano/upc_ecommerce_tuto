import requests
import json

ip_serveur = 'http://localhost:8000'
url = f'{ip_serveur}/api/categorie/donnees'
url = f'{ip_serveur}/api/article/categorie?idCategorie=1'

reponse = requests.get(url)
try:
    print('SUCCESS: REPONSE SERVEUR')
    print(json.dumps(reponse.json(), indent=4, ensure_ascii=False))
except Exception as e:
    erreur = e
    print('ERREUR: REPONSE SERVEUR')
    print(erreur)
