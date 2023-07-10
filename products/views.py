from rest_framework.views import Response, Request
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from users.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer: ProductSerializer):
        serializer.save(seller=self.request.user)


class ProductDetailedView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
