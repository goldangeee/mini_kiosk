# from django.http import HttpResponse
from .models import Category,Subcategory,Orders
# from django.template import loader
from django.shortcuts import render
# from django.http import Http404

def menu_category(request):
    category_list = Category.objects.all()    
    context = {
        "category_list": category_list,
    }    
    return render(request, "kiosk/menu_category.html", context)

def subcategory(request):
    subcategory_list = Subcategory.objects.filter(category_name_id=1)
    context = {
        "subcategory_list": subcategory_list,
    }    
    return render(request, "kiosk/subcategory.html", context)