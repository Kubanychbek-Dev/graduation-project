from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  """Расширение модели пользователя"""
  """User Model Extension"""
  email = models.EmailField(unique=True)
  username = models.CharField(unique=False, max_length=100)
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username"]

  def __str__(self):
    return self.username


class UserProfile(models.Model):
  user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
  full_name = models.CharField(max_length=50, null=True, blank=True)
  image = models.ImageField(upload_to="image", null=True, blank=True)
  phone = models.CharField(max_length=50, null=True, blank=True)

  def __str__(self):
    return self.full_name
  