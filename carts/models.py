from django.db import models
from users.models import User


class Cart(models.Model):
    # cart_id = models.IntegerField(primary_key=True)
    total = models.FloatField(default=0)

    # Chave estrangeira para a tabela User (exemplo)
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="cart")
