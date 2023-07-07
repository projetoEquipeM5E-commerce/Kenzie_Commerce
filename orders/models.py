from django.db import models


class StatusChoices(models.TextChoices):
    order_placed = ("PEDIDO REALIZADO",)
    in_progress = ("EM ANDAMENTO",)
    delivered = ("ENTREGUE",)
    default = "CARRINHO VAZIO"


class Order(models.Model):
    status = models.CharField(
        max_length=30, choices=StatusChoices.choices, default=StatusChoices.default
    )
    created_at = models.DateTimeField(auto_now_add=True)
    made_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )
