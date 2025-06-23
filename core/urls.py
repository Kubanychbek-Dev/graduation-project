from django.urls import path
from .views import category_list_view, product_list_view, vendors_list_view

urlpatterns = [
    path('', category_list_view, name="home"),
    path('category_product/<cid>/', product_list_view, name="products"),
    path('vendors/', vendors_list_view, name="vendors"),
]
