from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from addresses.models import Address
from addresses.serializers import AddressSerializer

# from addresses.serializers import AddressSerializer


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    address = AddressSerializer()
    # address = AddressSerializer(write_only=True)

    def create(self, validated_data: dict):
        address = validated_data.pop("address")
        create_address = Address.objects.create(**address)
        
        if validated_data.get("is_seller"):
            user = User.objects.create_superuser(**validated_data, address=create_address)
        else:
            user = User.objects.create_user(**validated_data, address=create_address)
        return user

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_superuser",
            "is_seller",
            "is_client",
            "address",
        ]
        extra_kwargs = {"password": {"write_only": True}}
