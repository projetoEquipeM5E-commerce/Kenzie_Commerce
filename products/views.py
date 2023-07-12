from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsSellerOrAdmin


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer: ProductSerializer):
        serializer.save(seller=self.request.user)


class ProductDetailedView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdmin]
    lookup_field = "id"

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
