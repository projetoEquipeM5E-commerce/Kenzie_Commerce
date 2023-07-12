from django.urls import path

from .views import CreateOrderView, OrdersDetailedView, ListOrdersSellerViews


urlpatterns = [
    path("orders/<int:id>/", CreateOrderView.as_view()),
    path("orders_seller/<int:id>/", ListOrdersSellerViews.as_view()),
    path("orders_update_destroy/<int:id>/", OrdersDetailedView.as_view()),

]
