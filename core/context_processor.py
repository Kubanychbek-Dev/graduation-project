from django.contrib import messages
from .models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address


def default(request):
  categories = Category.objects.all()
  if request.user.is_authenticated:
    address = Address.objects.filter(user=request.user)
  else:
    address = False
  
  wish_id = []

  try:
      wishlistCount = WishList.objects.filter(user=request.user).count()
      wishlist = WishList.objects.filter(user=request.user)
      for i in wishlist:
        wish_id.append(i.product.pid)
  except:
      wishlistCount = 0

  return {
    "categories": categories,
    "address": address,
    "wishlistCount": wishlistCount,
    "wish_id": wish_id
  }
