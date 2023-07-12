from django.db import models


class StatusChoices(models.TextChoices):
    order_placed = ("PEDIDO REALIZADO",)
    in_progress = ("EM ANDAMENTO",)
    delivered = ("ENTREGUE",)


class Order(models.Model):
    status = models.CharField(
        max_length=30, choices=StatusChoices.choices, default=StatusChoices.order_placed
    )
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )
