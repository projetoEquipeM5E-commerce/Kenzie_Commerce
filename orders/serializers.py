from rest_framework import serializers
from .models import Order
from users.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    def create(self, validated_data: dict) -> Order:
        user = validated_data["user"]
        product = validated_data["product"]

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
        fields = ["id", "status", "created_at", "user"]
