from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from carts.models import Cart
from products.models import Product
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAccountOwner, IsOrderProductOwner


class CreateOrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        id = self.kwargs["id"]
        product = get_object_or_404(Product, id=id)
        get_object_or_404(Cart, products=product)
        serializer.save(product=product, user=self.request.user)
    
    def get_queryset(self):
        id = self.kwargs["id"]
        product = get_object_or_404(Product, id=id)
        return Order.objects.filter(products=product)
    

class ListOrdersSellerViews(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOrderProductOwner]

    serializer_class = OrderSerializer

    def get_queryset(self):
        id = self.kwargs["id"]
        product = get_object_or_404(Product, id=id)
        if product.seller == self.request.user:
            return Order.objects.filter(products=product)
        

class OrdersDetailedView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOrderProductOwner]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "id"
