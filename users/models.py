from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)
    is_seller = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)
    address = models.OneToOneField("addresses.Address", related_name="address")
