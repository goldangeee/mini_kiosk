from django.contrib import admin

from .models import Category,Subcategory,Orders

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Orders)