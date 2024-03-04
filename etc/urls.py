from django.urls import path
from .views import contact , about , survey , search  , faq

urlpatterns = [
    path('contacts/',contact , name="Contacts"),
    path('about/',about , name="About"),
    path('survey/',survey , name="Survey"),
    path('search/',search , name="Search"),    
    path('faq/',faq , name="Faq"),    
]
