from django.urls import path
from .views import control_panel

urlpatterns = [
    path("control_panel/", control_panel, name="control_panel"),
]