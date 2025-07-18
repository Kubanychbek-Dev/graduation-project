from django.shortcuts import render, get_object_or_404, redirect
# from django.db.models import Count
# from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Avg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
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
  products = Product.objects.filter(product_status="published", in_stock=True, category=category)

  my_sessions = []
  if "cart_data_obj" in request.session:
    for i in request.session["cart_data_obj"]:
      my_sessions.append(i)

  context = {
    "title": category.title,
    "products": products,
    "sessions": my_sessions
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
  if average_rating.get("rating") is not None:
    average_rating_stars_count = int(average_rating.get("rating"))
  else:
    average_rating_stars_count = 0

  my_sessions = []
  if "cart_data_obj" in request.session:
    for i in request.session["cart_data_obj"]:
      my_sessions.append(i)

  context = {
    "title": product.title,
    "product": product,
    "images": product_images,
    "reviews": reviews,
    "average_rating": average_rating,
    "stars_count": average_rating_stars_count,
    "review_form": review_form,
    "sessions": my_sessions
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


def add_to_cart(request):
  cart_product = {}

  cart_product[str(request.GET["id"])] = {
    "pid": request.GET["pid"],
    "title": request.GET["title"],
    "quantity": request.GET["quantity"],
    "price": request.GET["price"],
    "img": request.GET["img"],
  }

  if "cart_data_obj" in request.session:
    if str(request.GET["id"]) in request.session["cart_data_obj"]:
      cart_data = request.session["cart_data_obj"]
      cart_data[str(request.GET["id"])]["quantity"] = int(cart_product[str(request.GET["id"])]["quantity"])
      cart_data.update(cart_data)
      request.session["cart_data_obj"] = cart_data
    else:
        cart_data = request.session["cart_data_obj"]
        cart_data.update(cart_product)
        request.session["cart_data_obj"] = cart_data
  else:
    request.session["cart_data_obj"] = cart_product

  return JsonResponse({
    "data": request.session["cart_data_obj"],
    "totalcartitems": len(request.session["cart_data_obj"])
  })


def cart_view(request):
  if request.user.is_authenticated is not True:
    messages.warning(request, "Пожалуйста, войдите в систему")
    return redirect("userauths:login")
  
  cart_total_amount = 0
  
  if "cart_data_obj" in request.session:
    small_stock = []
    products = Product.objects.all()
    for i in products:
      if i.stock_count == "1":
        small_stock.append(i.pid)

    for p_id, item in request.session["cart_data_obj"].items():
      cart_total_amount += int(item["quantity"]) * float(item["price"])
    return render(request, "core/cart.html", {
      "title": "Корзина",
      "data": request.session["cart_data_obj"],
      "totalcartitems": len(request.session["cart_data_obj"]), 
      "cart_total_amount": cart_total_amount,
      "small_stock": small_stock
    })
  else:
    return render(request, "core/cart.html")


def delete_cart_item(request):
  product_id = str(request.GET.get("id"))
  if "cart_data_obj" in request.session:
    if product_id in request.session["cart_data_obj"]:
      cart_data = request.session["cart_data_obj"]
      del request.session["cart_data_obj"][product_id]
      request.session["cart_data_obj"] = cart_data
  
  cart_total_amount = 0
  
  if "cart_data_obj" in request.session:
    for p_id, item in request.session["cart_data_obj"].items():
      cart_total_amount += int(item["quantity"]) * float(item["price"])

  return JsonResponse({
    "id": product_id,
    "totalcartitems": len(request.session["cart_data_obj"]),
    "cart_total_amount": cart_total_amount
  })


def update_cart_item(request):
  product_id = str(request.GET.get("id"))
  product_quantity = request.GET.get("quantity")

  if "cart_data_obj" in request.session:
    if product_id in request.session["cart_data_obj"]:
      cart_data = request.session["cart_data_obj"]
      cart_data[str(request.GET.get("id"))]["quantity"] = product_quantity
      request.session["cart_data_obj"] = cart_data
  
  cart_total_amount = 0
  
  if "cart_data_obj" in request.session:
    for p_id, item in request.session["cart_data_obj"].items():
      cart_total_amount += int(item["quantity"]) * float(item["price"])
  
  return JsonResponse({
    "data": request.session["cart_data_obj"],
    "id": product_id,
    "totalcartitems": len(request.session["cart_data_obj"]),
    "cart_total_amount": cart_total_amount,
  })


def checkout_cart(request):
  cart_total_amount = 0
  if "cart_data_obj" in request.session:
    for p_id, item in request.session["cart_data_obj"].items():
      cart_total_amount += int(item["quantity"]) * float(item["price"])
    
    context = {
      "title": "Корзина оформления заказа",
      "cart_data": request.session["cart_data_obj"],
      "total_cart_items": len(request.session["cart_data_obj"]),
      "cart_amount": cart_total_amount
    }
    return render(request, "core/checkout-cart.html", context)


def add_to_wishList(request):
  product_id = request.GET.get("id")
  product = Product.objects.get(pid=product_id)
    
  context = {}

  wishlist_count = WishList.objects.filter(product=product, user=request.user).count()

  if wishlist_count > 0:
    context = {
      "response": "Added"
    }
  else:
    new_wishlist = WishList.objects.create(
      user=request.user,
      product=product,
    )
    context = {
      "response": "Add"
    }
  
  return JsonResponse({
    "context": context,
  })


@login_required(login_url="userauths:login")
def wishlist_view(request):
  try:
    wishlist = WishList.objects.filter(user=request.user)
  except:
    wishlist = False
  
  my_sessions = []
  if "cart_data_obj" in request.session:
    for i in request.session["cart_data_obj"]:
      my_sessions.append(i)

  context = {
    "wishlist": wishlist,
    "sessions": my_sessions
  }
  return render(request, "core/wishlist.html", context)


def delete_wishlist(request):
  id = request.GET.get("id")
  wishlist = WishList.objects.filter(user=request.user, id=id)
  wishlist_json = serializers.serialize("json", wishlist)
  wishlist.delete()
  wishlist_count = WishList.objects.filter(user=request.user).count()

  return JsonResponse(
    {
      "wishlist": wishlist_json,
      "count": wishlist_count
    }
  )
