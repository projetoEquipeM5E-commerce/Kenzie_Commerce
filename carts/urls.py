from django.urls import path
from . import views


urlpatterns = [
    path("carts/<int:products_id>/", views.CartListCreateView.as_view()),
    path("carts/<int:products_id>/", views.CartRetrieveUpdateDestroyView.as_view()),
]

