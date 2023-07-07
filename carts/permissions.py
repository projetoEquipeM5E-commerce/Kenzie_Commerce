from rest_framework.permissions import BasePermission
from .models import Product

class IsProductInStock(BasePermission):
    def has_permission(self, request, view):
        product_id = view.kwargs.get('id')
        
        try:
            product = Product.objects.get(id=product_id)
            return product.is_in_stock
        except Product.DoesNotExist:
            return False