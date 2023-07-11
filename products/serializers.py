from rest_framework import serializers
from .models import Product
from users.serializers import UserSerializer
from orders.serializers import OrderSerializer


class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)

    def create(self, validated_data: dict):
        return Product.objects.create(**validated_data)

    def update(self, instance: Product, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "category",
            "price",
            "stock",
            "available",
            "seller",
        ]


class ProductOrder(serializers.ModelSerializer):
    made_by = UserSerializer(read_only=True)
    orders = OrderSerializer()

    class Meta:
        model = Product
        fields = ["id", "made_by", "orders"]


class ProductCart(serializers.ModelSerializer):
    made_by = UserSerializer(read_only=True)
    product = ProductSerializer()

    class Meta:
        model = Product
        fields = ["id", "user", "product"]
