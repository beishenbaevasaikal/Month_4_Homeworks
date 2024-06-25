from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.RegistrationView.as_view(), name="register"),
    path("login/", views.AuthLoginView.as_view(), name="login"),
    path("logout/", views.AuthLogoutView.as_view(), name="logout"),
    path("profile_list/", views.ProfileListView.as_view(), name="user_list"),
]
