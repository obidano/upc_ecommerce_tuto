from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    telephone = models.IntegerField(default=None)
    adresse = models.CharField(max_length=255)
    is_customer = models.BooleanField(default=False)
    date_inscription = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_user'

