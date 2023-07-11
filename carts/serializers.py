from rest_framework import serializers
from rest_framework.response import Response
from .models import Cart
from products.serializers import ProductSerializer
from products.models import Product
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework import status
from users.serializers import UserSerializer
from products.models import Product

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    products = ProductSerializer(read_only=True,many=True)  

    class Meta:
        model = Cart
        fields = [
            "id",
            "total",
            "user",
            "products"
        ]
        read_only_fields = ["total"]

   
# def create(self, request, *args, **kwargs)
    def create(self, validated_data):
        user = validated_data["user"]
        product = validated_data["product"]
 
        if product.stock < 1:
            raise ValidationError("Estoque insuficiente para o produto.")
          
        total = 0
       
        cart = Cart.objects.create(user=user, total=0)
        cart.products.add(product)
        for product in cart.products.all():
            total += product.price
          
        cart.total = total
        cart.save()
        return cart
        
