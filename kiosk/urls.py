from django.urls import path

from . import views

urlpatterns = [
    path("", views.menu_category, name="menu_category"),
    path("coffee", views.subcategory, name="subcategory_c"),
    # path("tea", views.subcategory, name="subcategory_t"),
    # path("beverage", views.subcategory, name="subcategory_b"),
    # path("ade", views.subcategory, name="subcategory_a"),
    # path("ice", views.subcategory, name="subcategory_i"),
]