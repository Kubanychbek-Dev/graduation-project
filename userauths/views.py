from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_view(request):
  """Аутентификация пользователя и вход в систему"""
  """User Authentication and Login"""
  form = UserRegisterForm()
  if request.method == "POST":
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get("username")
      email = form.cleaned_data.get("email")
      password = form.cleaned_data.get("password1")
      user = authenticate(username=email, password=password)
      login(request, user)
      messages.success(request, f"Привет {username}, Ваша учетная запись успешно создана")
      return redirect("core:home")
    
  context = {
      "title": "User Sign-Up",
      "form": form
    }
  return render(request, "userauths/sign_up.html", context)
    
