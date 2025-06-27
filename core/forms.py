from django import forms
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
  review = forms.CharField(label="", widget=forms.Textarea(attrs={
    "placeholder": "Написать отзыв"
  }))

  class Meta:
    model = ProductReview
    fields = ["review", "rating"]
