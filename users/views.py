from rest_framework import generics
from .serializers import UserSerializer
from drf_spectacular.utils import extend_schema
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="users_post",
        description="Rota de criação de usuário.",
        summary="Criar usuário !",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="users_get",
        description="Rota de listagem de usuários.",
        summary="Listar todos os usuários !",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"

    @extend_schema(
        operation_id="users_patch",
        description="Rota para atualizar um usuário por id.",
        summary="Atualizar um usuário por id",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        operation_id="users_get",
        description="Rota para listar um usuário por id.",
        summary="Listar um usuário por id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="users_delete",
        description="Rota para deletar um usuário por id.",
        summary="Deletar um usuário por id",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
