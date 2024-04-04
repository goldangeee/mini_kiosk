from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=200)

class Subcategory(models.Model):
    subcategory = models.ForeignKey(Category, on_delete=models.CASCADE)