from django.urls import path
from .views import register_view

urlpatterns = [
    path("sign-up/", register_view, name="sign-up")
]
