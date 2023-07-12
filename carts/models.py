from django.db import models


class Cart(models.Model):
    total = models.FloatField(default=0)
    user = models.OneToOneField(
        "users.User", on_delete=models.PROTECT, related_name="cart"
    )
