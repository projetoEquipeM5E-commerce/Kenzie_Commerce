from .models import Cart
from products.models import Product
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from .serializers import CartSerializer

class CartListCreateView(generics.ListCreateAPIView):
    # Definição da classe de view baseada em classe para listar e criar objetos Cart
    queryset = Cart.objects.all()  # Define o queryset como todos os objetos Cart
    serializer_class = CartSerializer  # Define a classe de serializer a ser usada
    authentication_classes = [JWTAuthentication]  # Define as classes de autenticação
    permission_classes = [IsAuthenticatedOrReadOnly]  # Define as classes de permissão

    def perform_create(self, serializer):
        # Método chamado quando um objeto Cart é criado
        user = self.request.user  # Obtém o usuário atual da requisição
        cart = Cart.objects.filter(user=user).first()  # Filtra o Cart associado ao usuário

        if cart is None:
            cart = Cart.objects.create(user=user)  # Cria um novo Cart se não existir

        product_id = self.kwargs.get('product_id')  # Obtém o ID do produto da URL
        product = get_object_or_404(Product, id=product_id)  # Obtém o objeto Product pelo ID

        if product.stock < 1:
            raise ValidationError("Estoque insuficiente para o produto.")  # Lança um erro se o estoque for insuficiente

        cart.products.add(product)  # Adiciona o produto ao campo products do Cart
        cart.total += product.price  # Atualiza o campo total do Cart com o preço do produto
        cart.save()  
       
class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
