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
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to="image")
  first_name = models.CharField(max_length=50, null=True, blank=True)
  last_name = models.CharField(max_length=50, null=True, blank=True)
  phone = models.CharField(max_length=50, null=True, blank=True)

  def __str__(self):
    return self.first_name