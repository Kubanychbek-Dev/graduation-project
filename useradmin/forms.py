from django import forms
from django.forms import inlineformset_factory
from core.models import Product, ProductImages


class AddProductForm(forms.ModelForm):
  title = forms.CharField(label="Название продукта", required=True, widget=forms.TextInput(attrs={
    "placeholder": "Название продукта",
    "class": "form-control input",
    "id": "title"
  }))
  price = forms.CharField(label="Текущая цена", required=True, widget=forms.NumberInput(attrs={
    "placeholder": "Текущая цена",
    "class": "form-control input",
    "id": "current-price"
  }))
  old_price = forms.CharField(label="Старая цена", widget=forms.NumberInput(attrs={
    "placeholder": "Введите старую цену, если есть скидка",
    "class": "form-control input",
    "id": "old-price"
  }))
  stock_count = forms.CharField(label="Количество товара", required=True, widget=forms.NumberInput(attrs={
    "placeholder": "Количество товара",
    "class": "form-control input",
    "id": "stock-count"
  }))
  image = forms.ImageField(label="Изображение", required=True, widget=forms.FileInput(attrs={
    "placeholder": "Изображение",
    "class": "form-control input",
    "id": "image"
  }))
  description = forms.CharField(label="Описание продукта", required=True, widget=forms.Textarea(attrs={
    "placeholder": "Описание продукта",
    "class": "form-control input",
    "id": "description"
  }))
  specification = forms.CharField(label="Характеристика продукта", required=True, widget=forms.Textarea(attrs={
    "placeholder": "Характеристика продукта",
    "class": "form-control input",
    "id": "specification"
  }))
    
  class Meta:
    model = Product
    fields = ["title", "price", "old_price", "stock_count", "image", "description", "specification", "category", "vendor"]


class ProductImagesForm(forms.ModelForm):
  class Meta:
    model = ProductImages
    fields = ["image"]


ProductImagesSet = inlineformset_factory(Product, ProductImages, form=ProductImagesForm, extra=4)
