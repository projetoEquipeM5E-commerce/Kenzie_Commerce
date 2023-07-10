from rest_framework import serializers
from rest_framework.response import Response
from .models import Cart
from products.serializers import ProductSerializer
from products.models import Product

class CartSerializer(serializers.ModelSerializer):
    cart_id = serializers.IntegerField(read_only=True)
    products = ProductSerializer(many=True)  

    class Meta:
        model = Cart
        fields = [
            "cart_id",
            "total",
            "user",
            "products"
        ]

    def create(self, validated_data: dict) -> Cart:
        return Cart.objects.create(**validated_data)
