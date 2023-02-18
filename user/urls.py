from django.urls import include, path

from .views import UserCreate, UserLogin

app_name = "users"


urlpatterns = [
    path("register/", UserCreate.as_view(), name="user_create"),
    path("login/", UserLogin.as_view(), name="user_login"),
]
