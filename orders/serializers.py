from rest_framework import serializers
from .models import Order
from users.serializers import UserSerializer
from products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    products = ProductSerializer(read_only=True, many=True)

    def create(self, validated_data: dict) -> Order:
        user = validated_data["user"]
        product = validated_data["product"]
        
        sellers = set([item.seller for item in validated_data if hasattr(item, 'products')])
        if len(sellers) > 1:
            for seller in sellers:
                order = Order.objects.create(user=user, seller=seller)
                order.products.add(product)
                order.save()
            return order
        order = Order.objects.create(user=user)
        order.products.add(product)
        order.save()
        return order

    def update(self, instance: Order, validated_data: dict):
        for key, value in validated_data.items:
            if key == "status":
                value == instance.status
            else:
                setattr(instance, key, value)
            instance.save()
            return instance

    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "user", "products"]
