import requests
import json

ip_serveur = 'http://localhost:8000'
url = f'{ip_serveur}/api/categorie/miseajour'
url = f'{ip_serveur}/api/article/miseajour'

donnees_a_envoyer = dict(idCategorie=1, nomCategorie="Agricultures")
donnees_a_envoyer = dict(idArticle=2, article="Blés", prixArticle=101)

reponse = requests.put(url, json.dumps(donnees_a_envoyer))
try:
    print('SUCCESS: REPONSE SERVEUR')
    print(json.dumps(reponse.json(), indent=4, ensure_ascii=False))
except Exception as e:
    erreur = e
    print('ERREUR: REPONSE SERVEUR')
    print(erreur)
