from django.contrib import admin
from .models import User, UserProfile


@admin.register(User)
class userAdmin(admin.ModelAdmin):
  list_display = ("pk", "first_name", "last_name", "email", "is_active")
  list_filter = ("last_name",)


@admin.register(UserProfile)
class userProfileAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "phone")
  list_filter = ("first_name",)
