from django.shortcuts import render, redirect
from core.models import CartOrder, CartOrderItems, Product, Category
from django.db.models import Sum
from userauths.models import User

import datetime


def control_panel(request):
  revenue = CartOrder.objects.aggregate(price=Sum("price"))
  all_products = Product.objects.all()
  all_categories = Category.objects.all()
  new_customers = User.objects.all().order_by("-id")
  recent_orders = CartOrder.objects.all().order_by("-order_date")[:10]

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
    "recent_orders": recent_orders,
    "monthly_revenue": monthly_revenue
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
