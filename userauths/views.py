from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.conf import settings
from .models import UserProfile, User
from .forms import UserRegisterForm, UserProfileForm, AccountEditForm
from core.models import Address, CartOrder, CartOrderItems

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
  address = Address.objects.filter(user=request.user)
  User = get_user_model()
  user = User.objects.get(id=request.user.id)

  if request.method == "POST":
    get_address = request.POST.get("address")

    new_address = Address.objects.create(
      user=request.user,
      address=get_address,
    )
    messages.success(request, "Адрес добавлен")
    return redirect("userauths:customer")
  
  try:
    orders = CartOrder.objects.filter(user=request.user)
  except:
    orders = False
  
  context = {
    "title": "Панель управления клиента",
    "profile": profile,
    "address": address,
    "user": user,
    "orders": orders
  }
  return render(request, "userauths/customer-dashboard.html", context)


def profile_update(request):
  profile = request.user.profile
  form = UserProfileForm(instance=profile)
  if request.method == "POST":
    form = UserProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
      form.save()
      messages.success(request, "Профиль успешно изменен")
      return redirect("userauths:customer")
  
  context = {
    "title": "Обновление профиля",
    "form": form
  }
  return render(request, "userauths/profile_update.html", context)


def select_address(request):
  id = request.GET.get("id")
  address = request.GET.get("address")
  Address.objects.update(status=False)
  Address.objects.filter(id=id).update(status=True)
  messages.success(request, f"Выбранный адрес: {address}")

  return JsonResponse({
    "boolean": True
  })


def delete_address(request, id):
  address = Address.objects.get(id=id)
  address_name = address.address
  address.delete()
  messages.success(request, f"Адрес {address_name:} удалено")
  return redirect("userauths:customer")


def account_edit(request, id):
  User = get_user_model()
  user = User.objects.get(id=id)
  form = AccountEditForm(instance=user)

  if request.method == "POST":
    form = AccountEditForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      profile = request.user.profile
      profile.full_name = form.cleaned_data["first_name"]+" "+ form.cleaned_data["last_name"]
      profile.save()
      messages.success(request, "Аккаунт изменен")
      return redirect("userauths:customer")

  context = {
    "form": form,
    "title": "Редактирование вашей учетной записи"
  }
  return render(request, "userauths/sign_up.html", context)


def change_password(request):
  user = request.user

  if request.method == "POST":
    old_password = request.POST.get("old-password")
    new_password = request.POST.get("new-password")
    confirm_new_password = request.POST.get("confirm-new-password")

    if confirm_new_password != new_password:
      messages.error(request, "Пароль не совпадает")
      return redirect("userauths:change_password")
    
    if check_password(old_password, user.password):
      user.set_password(new_password)
      user.save()
      messages.success(request, "пароль успешно изменен")
      return redirect("userauths:login")
    else:
      messages.error(request, "Старый пароль неверен")
      return redirect("userauths:change_password")
  
  context = {
    "title": "Изменение пароля"
  }
  return render(request, "userauths/change-password.html", context) 
