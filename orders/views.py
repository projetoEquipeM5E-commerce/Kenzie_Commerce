from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from products.models import Product
from django.shortcuts import get_object_or_404


class OrderView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        id = self.kwargs["id"]
        product = get_object_or_404(Product, id=id)
        serializer.save(product=product, user=self.request.user)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
