from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)

class Subcategory(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='default_value')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

class Orders(models.Model):
    pass