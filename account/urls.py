from django.urls import path
from .views import login_register

urlpatterns = [
    path('login/',login_register,name="Login"),
]
