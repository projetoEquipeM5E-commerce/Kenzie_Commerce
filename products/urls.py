from django.urls import path
from .views import ProductView, UserDetailView


urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<int:id>/", UserDetailView.as_view()),
]
