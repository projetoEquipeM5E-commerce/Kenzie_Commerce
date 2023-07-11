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
    orders = models.ManyToManyField(
        "users.User", related_name="made_by", through="products.ProductOrder"
    )
    


class ProductOrder(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)



