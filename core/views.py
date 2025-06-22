from django.shortcuts import render
from .models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address


def index(request):
  categories = Category.objects.all()

  context = {
    "title": "Домашняя страница",
    "categories": categories
  }
  
  return render(request, "core/home.html", context)
