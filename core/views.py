from django.shortcuts import render, get_object_or_404, redirect
# from django.db.models import Count
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Avg
from .models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address
from .forms import ProductReviewForm


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
  review_form = ProductReviewForm()
  average_rating_stars_count = int(average_rating.get("rating"))

  context = {
    "title": product.title,
    "product": product,
    "images": product_images,
    "reviews": reviews,
    "average_rating": average_rating,
    "stars_count": average_rating_stars_count,
    "review_form": review_form
  }
  return render(request, "core/product-detail.html", context)


def add_review(request, pid):
  product = Product.objects.get(pid=pid)
  user = request.user

  review = ProductReview.objects.create(
    user=user,
    product=product,
    review = request.POST["review"],
    rating = request.POST["rating"],
  )

  context = {
    "user": user.username,
    "review": request.POST["review"],
    "rating": request.POST["rating"],
  }

  average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg("rating"))

  return JsonResponse(
    {
      "bool": True,
      "context": context
    }
  )


def search_view(request):
  query = request.GET.get("q")
  products = Product.objects.filter(title__icontains=query).order_by("-date")

  context = {
    "title": "Поиск продукта",
    "products": products,
    "query": query
  }
  return render(request, "core/search.html", context)
