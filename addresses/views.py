from django.shortcuts import render
from rest_framework import generics
from .serializers import AddressSerializer
from .models import Address
from drf_spectacular.utils import extend_schema
# Create your views here.


class AdressView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @extend_schema(operation_id="addresses_post", description="Rota de criar addresses no album", summary="Criar address")
        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)