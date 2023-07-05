from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=150)
    number = models.PositiveSmallIntegerField()
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    complement = models.CharField(max_length=150, null=True)