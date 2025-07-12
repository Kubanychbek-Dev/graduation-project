from django.contrib import admin
from .models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address


class ProductImagesAdmin(admin.TabularInline):
  model = ProductImages


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  inlines = [ProductImagesAdmin]
  list_display = ["user", "title", "product_image", "price", "category", "vendor", "product_status"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ["title", "category_image"]


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
  list_display = ["title", "vendor_image"]


@admin.register(CartOrder)
class CartOrderAdmin(admin.ModelAdmin):
  list_display = ["user", "price", "paid_status", "invoice_no", "order_date", "product_status", "to_address"]


@admin.register(CartOrderItems)
class CartOrderItemsAdmin(admin.ModelAdmin):
  list_display = ["pk", "order", "item", "quantity", "price", "total"]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
  list_display = ["user", "product", "review", "rating"]


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
  list_display = ["id", "user", "product", "date"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
  list_display = ["user", "address", "status"]
