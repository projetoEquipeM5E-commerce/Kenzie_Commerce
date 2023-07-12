from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)

    seller = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="products"
    )
    orders = models.ManyToManyField("orders.Order", related_name="products")
    carts = models.ManyToManyField("carts.Cart", related_name="products")
