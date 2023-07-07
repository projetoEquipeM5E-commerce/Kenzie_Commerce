from django.db import models
from users.models import User
from products.models import Product
class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    total = models.FloatField(default=0)
    user = models.OneToOneField(User, on_delete=models.PROTECT,related_name='cart')
    products = models.ForeignKey(Product, related_name='products',on_delete=models.PROTECT )
    class Meta:
        ordering = ['cart_id']
