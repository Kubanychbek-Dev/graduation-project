from django.urls import path
from .views import control_panel, order_info, change_order_status, add_product

urlpatterns = [
    path("control_panel/", control_panel, name="control_panel"),
    path("order_info/<str:oid>/", order_info, name="order_info"),
    path("change_order_status/", change_order_status, name="change_order_status"),
    path("add_product/", add_product, name="add_product"),
]