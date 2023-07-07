from rest_framework import serializers
from .models import Order
from users.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    made_by = UserSerializer(read_only=True)

    def create(self, validated_data: dict):
        return super().create(**validated_data)

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
        fields = ["id", "status", "created_at", "made_by"]
