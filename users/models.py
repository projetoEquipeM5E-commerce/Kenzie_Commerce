from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True)
    is_seller = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)
    address = models.OneToOneField(
        "addresses.Address", on_delete=models.CASCADE, related_name="address"
    )
