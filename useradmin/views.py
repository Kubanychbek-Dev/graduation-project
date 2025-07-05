from django.shortcuts import render, redirect
from core.models import CartOrder, Product, Category
from django.db.models import Sum
from userauths.models import User

import datetime


def control_panel(request):

  context = {
    "title": "Панель управления"
  }
  return render(request, "useradmin/control-panel.html", context)
