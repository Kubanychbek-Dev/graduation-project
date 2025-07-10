from django.urls import path
from .views import checkout, checkout_success_view

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("checkout_success/<str:id>/", checkout_success_view, name="checkout_success"),
]