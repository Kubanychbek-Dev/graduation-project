from django.urls import path
from .views import category_list_view, product_list_view

urlpatterns = [
    path('', category_list_view, name="home"),
    path('category_product/<cid>/', product_list_view, name="products"),
]
