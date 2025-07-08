from django import forms
from .models import ProductReview
from userauths.models import User


class ProductReviewForm(forms.ModelForm):
  review = forms.CharField(label="", widget=forms.Textarea(attrs={
    "placeholder": "Написать отзыв"
  }))

  class Meta:
    model = ProductReview
    fields = ["review", "rating"]
