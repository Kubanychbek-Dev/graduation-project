from django.shortcuts import render
# from django.db.models import Count
from .models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address


def index(request):
  # Подсчет всех товаров этой категории
  # categories = Category.objects.all().annotate(product_count=Count("products"))
  categories = Category.objects.all()

  context = {
    "title": "Домашняя страница",
    "categories": categories
  }
  
  return render(request, "core/home.html", context)
