from .models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address


def default(request):
  categories = Category.objects.all()

  return {
    "categories": categories
  }
