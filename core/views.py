from django.shortcuts import render
from .models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address


def index(request):
  products = Product.objects.all()

  context = {
    "title": "Домашняя страница",
    "products": products
  }
  return render(request, "core/home.html", context)
