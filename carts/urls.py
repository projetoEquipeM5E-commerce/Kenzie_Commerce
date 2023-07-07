from django.urls import path
from . import views

urlpatterns = [
    path("carts/<int:pk>/", views.CartListCreateView.as_view()),
    path("carts/<int:pk>/", views.CartRetrieveUpdateDestroyView.as_view()),
   
    
]
