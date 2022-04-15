from django.db import models


# Create your models here.
class CategoriesArticles(models.Model):
    nomCat = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "tb_categories_articles"


class Articles(models.Model):
    nomArticle = models.CharField(max_length=255, unique=True)
    categorie = models.ForeignKey(CategoriesArticles, on_delete=models.CASCADE)
    prix = models.IntegerField(default=0)

    class Meta:
        db_table = "tb_articles"
