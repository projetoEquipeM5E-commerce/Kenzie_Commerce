from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import CartSerializer
from .models import Cart
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.models import Product
from users.permissions import IsAccountOwner


class CartCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        id = self.kwargs["id"]
        product = get_object_or_404(Product, id=id)
        serializer.save(product=product, user=self.request.user)


class CartListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartDetailedView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    lookup_field = "id"

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
