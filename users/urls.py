from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *

urlpatterns = [
    path("/register", Register.as_view(), name="register"),
    path("/login", Login.as_view(), name="login"),
    path("/refresh", Refresh.as_view(), name="refresh"),
]
