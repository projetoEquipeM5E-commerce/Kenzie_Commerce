
from .models import Cart
from .serializers import CartSerializer
from products.models import Product
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Cart, Product
from .serializers import CartSerializer
from rest_framework import generics
from .serializers import CartSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Cart
from rest_framework.exceptions import ValidationError
from .serializers import CartSerializer

class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        # pego meu carrinho criado com usuario logado
        cart = Cart.objects.filter(user= self.request.user)
        total = cart.total.get()#se não funcionar bota cart["total"] pega meu total
        products_ordered = cart.products.get()#se não funcionar bota cart["products"] pega meus 
        #products
        
        
        # pego o id da url do produto
        product_id = self.kwargs['product_id']
        
        # procuro esse id no product se não achar vai das 400 por causa da função get_object_or_404
        product = get_object_or_404(Product, id=product_id)
        
        # Verifico se há estoque suficiente
        if product.stock < 1:
            raise ValidationError("Estoque insuficiente para o produto.")
        cart.products.add(product)
        total += product.price
        
        # Salvar as alterações no carrinho
        cart.save()
       
class CartRetrieveUpdateDestroyView(generics.UpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
