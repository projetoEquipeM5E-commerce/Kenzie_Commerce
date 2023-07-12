from django.urls import path

from .views import OrderView


urlpatterns = [
    path("orders/<int:id>/", OrderView.as_view()),
]
