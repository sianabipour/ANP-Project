from django.urls import path
from .views import  services , single_service 

urlpatterns = [
    path('',services , name="Services"),
    path('<slug:slug>/',single_service , name="Service"),
]
