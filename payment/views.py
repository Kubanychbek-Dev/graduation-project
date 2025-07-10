from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from core.models import Product, CartOrder, CartOrderItems
from .mock_payment_provider import MockPaymentProvider


def checkout(request):
  user = request.user
  user_phone = request.GET.get("phone")
  user_address = request.GET.get("address")
  cart_subtotal = request.GET.get("subtotal")
  
  order = CartOrder.objects.create(
    user=user,
    price=cart_subtotal,
    phone=user_phone,
    to_address=user_address,
  )

  payment_provider = MockPaymentProvider()
  success, transaction_id = payment_provider.process_payment(order, cart_subtotal, "token123")

  if success:
    order.paid_status = True
    order.invoice_no=transaction_id
    order.product_status = "shipped"
    order.save()

    if "cart_data_obj" in request.session:
      for p_id, item in request.session["cart_data_obj"].items():
        CartOrderItems.objects.create(
          order=order,
          item=item["title"],
          quantity=item["quantity"],
          price=item["price"],
          total=int(item["quantity"]) * float(item["price"]),
        )
        product = Product.objects.get(pid=item["pid"])
        product.stock_count = int(product.stock_count) - int(item["quantity"])
        product.save()
        if product.stock_count == 0:
          product.in_stock = False
          product.save()
        
      request.session["cart_data_obj"] = {}
    
  else:
    order.paid_status = False
    order.invoice_no=transaction_id
    order.save()
    messages.error(request, "Платеж не выполнен")
    # return redirect("core:checkout_cart")
  return JsonResponse({
    "address": user_address,
    "phone": user_phone,
    "subtotal": cart_subtotal,
    "success_url": order.invoice_no
  })


def checkout_success_view(request, id):
  order = CartOrder.objects.get(invoice_no=id)
  order_items = CartOrderItems.objects.filter(order=order)

  context = {
    "title": "Заказ успешно выполнен",
    "transaction_id": order.invoice_no,
    "order": order,
    "items": order_items,
    "total_amount": order.price
  }
  return render(request, "payment/checkout-success.html", context)
