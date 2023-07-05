from django.shortcuts import render
from rest_framework import generics
from .serializers import AddressSerializer
from .models import Address

# Create your views here.


class AdressView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
