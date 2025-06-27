from django.urls import path
from .views import category_list_view, product_list_view, vendors_list_view, vendor_products_view, product_detail_view, add_review

urlpatterns = [
  # categories
    path('', category_list_view, name="home"),
    # Products
    path('category_product/<cid>/', product_list_view, name="products"),
    path('product_detail/<pid>/', product_detail_view, name="product_detail"),
    # Vendors
    path('vendors/', vendors_list_view, name="vendors"),
    path('vendor_products/<vid>/', vendor_products_view, name="vendor-products"),
    # Add review
    path('add_review/<pid>/', add_review, name="add_review"),
]
