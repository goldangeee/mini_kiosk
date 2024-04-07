# from django.http import HttpResponse
from .models import Category,Subcategory,Orders
# from django.template import loader
from django.shortcuts import render
# from django.http import Http404
from django.shortcuts import get_object_or_404

def menu_category(request):
    category_list = Category.objects.all()    
    context = {
        "category_list": category_list,
    }    
    return render(request, "kiosk/menu_category.html", context)

def subcategory(request,ex1):
    category_instance = get_object_or_404(Category, category_name=ex1)
    subcategory_list = Subcategory.objects.filter(category_name = category_instance)
    context = {
        "subcategory_list": subcategory_list,
    }    
    return render(request, "kiosk/subcategory.html", context)

def shoppingcart(request):
    shoppinglist = Subcategory.objects.filter(quantity__gte=1)    
    context = {
        "shoppinglist": shoppinglist,
    }    
    return render(request, "kiosk/shoppingcart.html", context)