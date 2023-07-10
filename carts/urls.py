from django.urls import path
from . import views


urlpatterns = [
    path("carts/", views.CartListCreateView.as_view()),
    path("carts/<int:id>/", views.CartRetrieveUpdateDestroyView.as_view()),
]

