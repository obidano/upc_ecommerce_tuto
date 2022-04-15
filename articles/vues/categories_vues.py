from django.http import JsonResponse
from articles.models import CategoriesArticles
import json


def creerCategorieVue(requete):
    # capture des données venant d'un client
    data = json.loads(requete.body)
    nomCategorie = data['nomCategorie']

    # insertion dans la table categorie
    new_category = CategoriesArticles()
    new_category.nomCat = nomCategorie
    new_category.save()

    reponse_serveur = dict(message="Nouvelle Catégorie Enregistrée")
    return JsonResponse(reponse_serveur)


def miseAJourCategorieVue(requete):
    data = json.loads(requete.body)
    idCategorie = data['idCategorie']
    nomCategorie = data['nomCategorie']
    # mise à jour dans la table categorie
    category_existant = CategoriesArticles.objects.filter(id=idCategorie)
    category_existant.update(nomCat=nomCategorie)

    reponse_serveur = dict(message="Catégorie Mise à jour")
    return JsonResponse(reponse_serveur)


def recupererDonneesCategoriesVue(requete):
    selection = CategoriesArticles.objects.values()
    reponse_serveur = dict(message=list(selection))
    return JsonResponse(reponse_serveur)
