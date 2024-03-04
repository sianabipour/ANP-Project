from django.urls import path
from .views import cart, checkout, single_product, products
urlpatterns = [
    path('',products,name="Products"),
    path('<slug:slug>',single_product,name="Product"),
    path('cart/',cart,name="Cart"),
    path('checkout/',checkout,name="Checkout"),
]
