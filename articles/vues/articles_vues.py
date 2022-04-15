from django.http import JsonResponse
from articles.models import Articles
import json


def creerArticleVue(requete):
    data = json.loads(requete.body)
    article = data['article']
    idCategorie = data['idCategorie']
    prixArticle = data['prixArticle']

    # insertion dans la table des articles
    new_article = Articles()
    new_article.nomArticle = article
    new_article.categorie_id = idCategorie
    new_article.prix = prixArticle
    new_article.save()

    reponse_serveur = dict(message="Nouvel article Enregistré")
    return JsonResponse(reponse_serveur)


def miseAJourArticleVue(requete):
    data = json.loads(requete.body)
    idArticle = data['idArticle']
    article = data['article']
    prixArticle = data['prixArticle']

    article_existant = Articles.objects.filter(id=idArticle)
    article_existant.update(nomArticle=article, prix=prixArticle)

    reponse_serveur = dict(message="Article Mis à jour")
    return JsonResponse(reponse_serveur)


def recupererDonneesArticlesVue(requete):
    selection = Articles.objects.values()
    reponse_serveur = dict(message=list(selection))
    return JsonResponse(reponse_serveur)


def recupererUnArticleVue(requete):
    data = requete.GET
    idArticle = data['idArticle']

    selection = Articles.objects.filter(id=idArticle).values()
    reponse_serveur = dict(message=list(selection))
    return JsonResponse(reponse_serveur)


def recupererArticleParCategorieVue(requete):
    data = requete.GET
    idCategorie = data['idCategorie']

    selection = Articles.objects.filter(categorie_id=idCategorie).values()
    reponse_serveur = dict(message=list(selection))
    return JsonResponse(reponse_serveur)
