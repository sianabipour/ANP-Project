from django.urls import path
from .views import projects, single_project
urlpatterns = [
    path('',projects,name="Projects"),
    path('<slug:slug>',single_project,name="Project")
]
