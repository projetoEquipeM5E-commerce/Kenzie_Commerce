from .models import Cart
from products.models import Product
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from .serializers import CartSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from users.models import User


class CartListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAccountOwner] 
    queryset = Cart.objects.all()  
    serializer_class = CartSerializer  
        
    def perform_create(self, serializer):
         pk = self.kwargs['products_id']
         product = get_object_or_404(Product, pk=pk)
         serializer.save(product=product,user=self.request.user)
    
       
class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
