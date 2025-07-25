from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.db.models import Count
from userauths.models import User


STATUS_CHOICE = (
  ("processing", "Processing"),
  ("shipped", "Shipped"),
  ("delivered", "Delivered"),
)


STATUS = (
  ("draft", "Draft"),
  ("disabled", "Disabled"),
  ("rejected", "Rejected"),
  ("in review", "In Review"),
  ("published", "Published"),
)


RATING = (
  (1, "⭐☆☆☆☆"),
  (2, "⭐⭐☆☆☆"),
  (3, "⭐⭐⭐☆☆"),
  (4, "⭐⭐⭐⭐☆"),
  (5, "⭐⭐⭐⭐⭐"),
)


def user_directory_path(instance, filename):
  """Эта функция динамически определяет путь загрузки файла на основе связанного идентификатора пользователя."""
  """Каталог пользователя"""
  """User directory"""
  return "user_{0}/{1}".format(instance.user.id, filename)


class Category(models.Model):
  cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefghik123456")
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to="category")

  class Meta:
    verbose_name = "Category"
    verbose_name_plural = "Categories"
  
  def category_image(self):
    return mark_safe("<img src='%s' width='50' height='50' />" % (self.image.url))
  
  def __str__(self):
    return self.title


class Vendor(models.Model):
  vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven", alphabet="abcdefghik123456")
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to=user_directory_path)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

  class Meta:
    verbose_name_plural = "Vendors"
  
  def vendor_image(self):
    return mark_safe("<img src='%s' width='50' height='50' />" % (self.image.url))
  
  def __str__(self):
    return self.title
  

class Product(models.Model):
  pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghik123456")
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
  vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name="product")
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to=user_directory_path)
  description = models.TextField(null=True, blank=True)
  specification = models.TextField(null=True, blank=True)
  price = models.DecimalField(max_digits=19, decimal_places=2)
  old_price = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
  product_status = models.CharField(choices=STATUS, max_length=10, default="in review")
  stock_count = models.CharField(max_length=1000, null=True)
  in_stock = models.BooleanField(default=True)
  date = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(null=True, blank=True)

  class Meta:
    verbose_name_plural = "Products"
  
  def product_image(self):
    return mark_safe("<img src='%s' width='50' height='50' />" % (self.image.url))
  
  def __str__(self):
    return self.title
  
  def get_percentage(self):
    percent = ((self.old_price - self.price) / self.old_price) * 100
    return round(percent)
  

class ProductImages(models.Model):
     image = models.ImageField(upload_to="product-images")
     product = models.ForeignKey(Product, related_name="product_imgs", on_delete=models.SET_NULL, null=True)
     date = models.DateTimeField(auto_now_add=True)

     class Meta:
       verbose_name_plural = "Product iamges"


class CartOrder(models.Model):
  oid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ord", alphabet="abcde123456")
  user = models.ForeignKey(User, related_name="order", on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=19, decimal_places=2)
  paid_status = models.BooleanField(default=False)
  invoice_no = models.CharField(max_length=200, null=True)
  order_date = models.DateTimeField(auto_now_add=True)
  product_status = models.CharField(choices=STATUS_CHOICE, max_length=20, default="processing")
  phone = models.CharField(max_length=50, null=True)
  to_address = models.CharField(max_length=100, null=True)

  class Meta:
       verbose_name_plural = "Cart Order"


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, related_name="order_items", on_delete=models.CASCADE)
    product_status = models.CharField(max_length=100, null=True, blank=True)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
       verbose_name_plural = "Cart Order Items"
    
    def order_image(self):
         return mark_safe("<img src='/media/%s' width='50' height='50' />" % (self.image))


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name="review", on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"
        
    def __str__(self):
      return self.product.title
    
    def get_rating(self):
       return self.rating


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Wish Lists"
        
    def __str__(self):
      return self.product.title


class Address(models.Model):
   user = models.ForeignKey(User, related_name="address", on_delete=models.CASCADE)
   address = models.CharField(max_length=100, null=True, blank=True)
   status = models.BooleanField(default=False)

   class Meta:
        verbose_name_plural = "Address"
