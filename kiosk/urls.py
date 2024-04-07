from django.urls import path

from . import views

urlpatterns = [
    path("", views.menu_category, name="menu_category"),
    path("shoppingcart", views.shoppingcart, name="shoppingcart"), 
    path("<str:ex1>", views.subcategory, name="subcategory"),
       
]