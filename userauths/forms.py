from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile


class UserRegisterForm(UserCreationForm):
  username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
    "placeholder": "Username",
    "class": "form-control input",
  }))
  email = forms.EmailField(required=True, label="", widget=forms.EmailInput(attrs={
    "placeholder": "Email",
    "class": "form-control input",
  }))
  first_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
    "placeholder": "Имя",
    "class": "form-control input",
  }))
  last_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
    "placeholder": "Фамилия",
    "class": "form-control input",
  }))
  password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={
    "placeholder": "Пароль",
    "class": "form-control input",
  }))
  password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={
    "placeholder": "Подтверждение пароля",
    "class": "form-control input",
  }))

  class Meta:
    model = User
    fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class UserProfileForm(forms.ModelForm):
  phone = forms.CharField(label="", widget=forms.TextInput(attrs={
    "placeholder": "Телефон"
  }))

  class Meta:
    model = UserProfile
    fields = ["phone", "image"]


class AccountEditForm(forms.ModelForm):
  username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
    "placeholder": "Username",
    "class": "form-control input",
  }))
  email = forms.EmailField(required=True, label="", widget=forms.EmailInput(attrs={
    "placeholder": "Email",
    "class": "form-control input",
  }))
  first_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
    "placeholder": "Имя",
    "class": "form-control input",
  }))
  last_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
    "placeholder": "Фамилия",
    "class": "form-control input",
  }))

  class Meta:
    model = User
    fields = ["username", "email", "first_name", "last_name"]
