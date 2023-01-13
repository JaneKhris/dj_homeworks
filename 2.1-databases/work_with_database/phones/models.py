from django.db import models


class Phone(models.Model):

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    image = models.CharField(max_length=100,)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)

