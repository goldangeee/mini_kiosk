from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Subcategory,Orders
from django.template import loader

def menu(request):
    category_list = Category.objects.all()
    output = ", ".join([c.category_name for c in category_list])
    return HttpResponse(output)
    # template = loader.get_template("kiosk/menu.html")
    # return HttpResponse("menu")