from unicodedata import name
from django.db import models

# Create your models here.


class Coffe(models.Model):
    name = models.CharField(max_length=100)
    amound = models.CharField(max_length=100)
    paiment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)