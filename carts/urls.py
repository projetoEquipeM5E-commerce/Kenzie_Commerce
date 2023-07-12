from django.urls import path
from .views import CartCreateView, CartListView, CartDetailedView


urlpatterns = [
    path("carts/<int:id>/", CartCreateView.as_view()),
    path("carts/<int:id>/", CartDetailedView.as_view()),
    path("carts/", CartListView.as_view()),
]
