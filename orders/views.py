from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from drf_spectacular.utils import extend_schema


class OrderView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @extend_schema(
        operation_id="orders_post",
        description="Rota para a criação de um pedido.",
        summary="Criar pedido.",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="orders_get",
        description="Rota para a listagem de todos os pedidos.",
        summary="Listar pedidos.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
