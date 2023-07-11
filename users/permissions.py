from rest_framework import permissions
from rest_framework.views import Request, View
from products.models import Product, ProductCart, ProductOrder
from orders.models import Order


class IsAdminOrAccountOwner(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_superuser or request.user.is_authenticated


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_superuser


class IsSellerOrAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_seller or request.user.is_superuser


class IsProductOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Product) -> bool:
        if obj.seller == request.user or request.user.is_superuser:
            return True


class IsOrderProductOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: ProductOrder):
        if obj.product.seller == request.user:
            return True


class IsOrderAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Order):
        if obj.made_by == request.user:
            return True
