from django.shortcuts import render
from django.http import HttpResponse

from .models import Category

def index(request):
    return HttpResponse("Hello, world. You're at the kiosk index.")