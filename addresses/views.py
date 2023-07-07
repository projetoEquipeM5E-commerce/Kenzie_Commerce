from django.shortcuts import render
from rest_framework import generics
from .serializers import AddressSerializer
from .models import Address
from drf_spectacular.utils import extend_schema
# Create your views here.

