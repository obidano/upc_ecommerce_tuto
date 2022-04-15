import requests
import json

ip_serveur = 'http://localhost:8000'
# url = f'{ip_serveur}/api/categorie/creer'
url = f'{ip_serveur}/api/article/creer'

# donnees_a_envoyer = dict(nomCategorie="Agricultureeeee")
donnees_a_envoyer = dict(article="Blé", idCategorie=1, prixArticle=100)

reponse = requests.post(url, json.dumps(donnees_a_envoyer))
try:
    print('SUCCESS: REPONSE SERVEUR')
    print(json.dumps(reponse.json(), indent=4, ensure_ascii=False))
except Exception as e:
    erreur = e
    print('ERREUR: REPONSE SERVEUR')
    print(erreur)
