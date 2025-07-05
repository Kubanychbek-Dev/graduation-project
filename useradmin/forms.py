from django import forms
from core.models import Product


class AddProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = [
      "title",
      "image",
      "description",
      "specification",
      "price",
      "old_price",
      "category",
      "stock_count"
    ]
    