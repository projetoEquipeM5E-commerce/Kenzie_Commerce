from rest_framework import generics


# Create your views here.
class CartView(generics.CreateAPIView):
    lookup_field = "cart_id"
