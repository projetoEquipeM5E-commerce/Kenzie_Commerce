from rest_framework import serializers
from carts.models import Cart
from users.serializers import UserSerializer
from products.serializers import ProductSerializer
from rest_framework.exceptions import ValidationError


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    products = ProductSerializer(read_only=True, many=True)

    def create(self, validated_data: dict) -> Cart:
        user = validated_data["user"]
        product = validated_data["product"]

        if product.stock < 1:
            raise ValidationError("No products in stock.")

        if user.cart:
            cart = Cart.objects.get(user=user)
            cart.products.add(product)
            cart.save()
            return cart

        total = 0
        cart = Cart.objects.create(user=user, total=0)
        cart.products.add(product)
        for product in cart.products.all():
            total += product.price

        cart.total = total
        cart.save()
        return cart

    class Meta:
        model = Cart
        fields = ["id", "total", "user", "products"]
