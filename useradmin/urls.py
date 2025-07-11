from django.urls import path
from .views import control_panel, order_info

urlpatterns = [
    path("control_panel/", control_panel, name="control_panel"),
    path("order_info/<str:oid>/", order_info, name="order_info"),
]