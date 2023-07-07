from rest_framework import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from orders.models import Order, OrderItem
from products.models import Product
from .models import Cart
class CartSerializer(serializers.ModelSerializer):
 cart_id = serializers.IntegerField(read_only=True)
 products =CartSerializer(many=True)#colocar o serializer do products aqui

class Meta:
        model = Cart
        fields = [
            "cart_id"
            "total",
            "user"
            "products"
        ]
    
def create(self, validated_data: dict) -> Cart:
        return Cart.objects.create(**validated_data)
