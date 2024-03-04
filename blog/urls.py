from django.urls import path
from .views import blogs , single_blog

urlpatterns = [
    path('',blogs , name="Blogs"), 
    path('<slug:slug>',single_blog , name="Blog"),    
       

]
