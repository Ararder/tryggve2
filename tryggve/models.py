from django.db import models
from django.conf import settings

static_url = settings.STATIC_URL
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    image = models.URLField(max_length=200)
