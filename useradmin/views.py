from django.shortcuts import render, redirect
from django.http import JsonResponse
from core.models import CartOrder, CartOrderItems, Product, ProductImages, Category
from django.db.models import Sum
from django.contrib import messages

from userauths.models import User
from .forms import AddProductForm, ProductImagesSet

import datetime


def control_panel(request):
  revenue = CartOrder.objects.aggregate(price=Sum("price"))
  all_products = Product.objects.all()
  all_categories = Category.objects.all()
  new_customers = User.objects.all().order_by("-id")
  all_orders = CartOrder.objects.all().order_by("-order_date")
  recent_orders = CartOrder.objects.all().order_by("-order_date")[:10]
  shipped_paid_orders = CartOrder.objects.filter(paid_status=True, product_status="shipped").order_by("-order_date")

  this_month = datetime.datetime.now().month
  monthly_orders = CartOrder.objects.filter(order_date__month=this_month).count()
  monthly_revenue = CartOrder.objects.filter(order_date__month=this_month).aggregate(price=Sum("price"))

  context = {
    "title": "Панель управления",
    "revenue": revenue,
    "monthly_orders": monthly_orders,
    "all_products": all_products,
    "all_categories": all_categories,
    "new_customers": new_customers,
    "all_orders": all_orders,
    "recent_orders": recent_orders,
    "monthly_revenue": monthly_revenue,
    "shipped_paid_orders": shipped_paid_orders
  }
  return render(request, "useradmin/control-panel.html", context)


def order_info(request, oid):
  order = CartOrder.objects.get(oid=oid)
  order_items = CartOrderItems.objects.filter(order=order)

  context = {
    "title": "Информация о заказе",
    "order": order,
    "order_items": order_items
  }
  return render(request, "useradmin/order-info.html", context)


def change_order_status(request):
  order_status = request.GET.get("status")
  order_id = request.GET.get("id")

  order = CartOrder.objects.get(oid=order_id)
  order.product_status = order_status
  order.save()

  return JsonResponse({
    "status": order_status,
    "id": order_id,
  })


def add_product(request):
  product_form = AddProductForm()
  images_set = ProductImagesSet()

  if request.method == "POST":
    product_form = AddProductForm(request.POST, request.FILES)
    images_set = ProductImagesSet(request.POST, request.FILES)
    if product_form.is_valid() and images_set.is_valid():
      product = product_form.save(commit=False)
      product.user = request.user
      product.save()
      for img in images_set:
        if img.has_changed():
          images = img.save(commit=False)
          images.product = product
          images.save()
      return redirect("core:home")

  context = {
    "product_form": product_form,
    "images": images_set
  }
  return render(request, "useradmin/add-product.html", context)
