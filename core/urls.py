from django.urls import path
from .views import category_list_view, product_list_view, vendors_list_view, vendor_products_view, product_detail_view, add_review, search_view, add_to_cart, cart_view, delete_cart_item

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
    # Search
    path('search/', search_view, name="search"),
    # Add to cart
    path('add-to-cart/', add_to_cart, name="add-to-cart"),
    # Cart page URL
    path('cart/', cart_view, name="cart"),
    # Delete product from cart
    path('delete_cart_item/', delete_cart_item, name="delete_cart_item"),
]
