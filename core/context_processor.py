from .models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address


def default(request):
  categories = Category.objects.all()
  if request.user.is_authenticated:
    address = Address.objects.get(user=request.user)
  else:
    address = "Адрес не указан"

  return {
    "categories": categories,
    "address": address
  }
