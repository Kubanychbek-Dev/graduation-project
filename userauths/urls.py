from django.urls import path
from .views import register_view, login_view, logout_view, customer_dashboard, profile_update, select_address, delete_address, account_edit, change_password

urlpatterns = [
    path("sign-up/", register_view, name="sign-up"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    # Customer Dashboard
    path("customer/", customer_dashboard, name="customer"),
    path("customer/update/", profile_update, name="profile_update"),
    path("select_address/", select_address, name="select_address"),
    path("delete_address/<int:id>/", delete_address, name="delete_address"),
    path("account_edit/<int:id>/", account_edit, name="account_edit"),
    path("change_password/", change_password, name="change_password"),
]
