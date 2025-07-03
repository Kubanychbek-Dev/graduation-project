from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from .models import UserProfile

User = settings.AUTH_USER_MODEL


def register_view(request):
  """Аутентификация пользователя и вход в систему"""
  """User Authentication and Login"""
  if request.user.is_authenticated:
    return redirect("core:home")
  
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
      "title": "Создать аккаунт",
      "form": form
    }
  return render(request, "userauths/sign_up.html", context)
    

def login_view(request):
  """Вход в систему"""
  """Login"""
  if request.user.is_authenticated:
    return redirect("core:home")
  
  if request.method =="POST":
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(request, email=email, password=password)

    if user is not None:
      login(request, user)
      messages.success(request, "Вы вошли в систему")
      return redirect("core:home")
    else:
      messages.error(request, "Что-то не так, пожалуйста, введите данные правильно или аккаунт не существует")
  
  context = {"title": "Вход в аккаунт"}
  return render(request, "userauths/login.html", context)


def logout_view(request):
  logout(request)
  messages.warning(request, "Вы успешно вышли из системы")
  return redirect("userauths:login")


def customer_dashboard(request):
  profile = UserProfile.objects.get(user=request.user)
  
  context = {
    "profile": profile
  }
  return render(request, "userauths/customer-dashboard.html", context)


def profile_edit(request):
  pass
