from django.urls import path
from .views import ProductView, ProductDetailedView


urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<int:id>/", ProductDetailedView.as_view()),
]
