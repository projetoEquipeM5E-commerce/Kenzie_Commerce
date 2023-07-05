from django.db import models


# class StatusChoices(models.TextChoices):
#     order_placed = ("Pedido realizado.",)
#     in_progress = ("Em andamento.",)
#     delivered = ("Entregue.",)
#     default = "Carrinho vazio."


# class Order(models.Model):
#     status = models.CharField(
#         max_length=30, choices=StatusChoices.choices, default=StatusChoices.default
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     made_by = models.ForeignKey(
#         "users.User", on_delete=models.CASCADE, related_name="orders"
#     )

#     def __str__(self) -> str:
#         return f"Order ({self.id}) - ({self.status})"
