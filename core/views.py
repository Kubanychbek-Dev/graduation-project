from django.shortcuts import render, get_object_or_404
# from django.db.models import Count
from django.db.models import Avg
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


def vendor_products_view(request, vid):
  vendor = Vendor.objects.get(vid=vid)
  products = Product.objects.filter(product_status="published", vendor=vendor)

  context = {
    "title": vendor.title + " - купить товары",
    "products": products
  }
  return render(request, "core/product-list.html", context)


def product_detail_view(request, pid):
  # product = get_object_or_404(Product, pid=pid)
  product = Product.objects.get(pid=pid)
  product_images = product.product_imgs.all()
  reviews = ProductReview.objects.filter(product=product).order_by("-date")
  average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg("rating"))

  context = {
    "title": product.title,
    "product": product,
    "images": product_images,
    "reviews": reviews,
    "average_rating": average_rating
  }
  return render(request, "core/product-detail.html", context)
