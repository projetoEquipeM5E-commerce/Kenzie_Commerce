from rest_framework import serializers
from .models import Product
from users.serializers import UserSerializer


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
        model: Product
        fields = [
            "id",
            "product_name",
            "category",
            "price",
            "stock",
            "available",
            "seller",
        ]
