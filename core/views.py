from django.shortcuts import render
# from django.db.models import Count
from .models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address


def category_list_view(request):
  # Подсчет всех товаров этой категории
  # categories = Category.objects.all().annotate(product_count=Count("products"))
  categories = Category.objects.all()

  context = {
    "title": "Домашняя страница",
    "categories": categories
  }
  
  return render(request, "core/home.html", context)


def product_list_view(request, cid):
  category = Category.objects.get(cid=cid)
  products = Product.objects.filter(product_status="published", category=category)

  context = {
    "title": category.title,
    "category": category,
    "products": products
  }
  return render(request, "core/product-list.html", context)


def vendors_list_view(request):
  vendors = Vendor.objects.all()

  context = {
    "title": "Vendors",
    "vendors": vendors
  }
  return render(request, "core/vendors-list.html", context)
