from django.db import models
from users.models import User


from products.models import Product
class Cart(models.Model):
    # id = models.IntegerField(primary_key=True)
    total = models.FloatField(default=0)
    user = models.OneToOneField(User, on_delete=models.PROTECT,related_name='cart')
    products = models.ManyToManyField("products.Product", related_name='carts')
    class Meta:
        ordering = ["id"]
    