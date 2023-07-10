<<<<<<< HEAD
 from django.shortcuts import render
 from rest_framework import generics
 from .serializers import AddressSerializer
 from .models import Address
 from drf_spectacular.utils import extend_schema
 #Create your views here.
=======
from django.shortcuts import render
from rest_framework import generics
from .serializers import AddressSerializer
from .models import Address
from drf_spectacular.utils import extend_schema

# Create your views here.
>>>>>>> 27021352dc3b9c910930eace74e9765c9b2e199a


class AddressView(generics.CreateAPIView):
    ...
