from django.contrib import admin
from .models import User


@admin.register(User)
class userAdmin(admin.ModelAdmin):
  list_display = ("pk", "first_name", "last_name", "email", "is_active")
  list_filter = ("last_name",)