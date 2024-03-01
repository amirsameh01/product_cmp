
from django.contrib import admin
from django.forms import NumberInput 
from .models import Product, AttributeDefinition, ProductType, ProductAttribute
from django.db import models

@admin.register(AttributeDefinition)
class AttributeAdmin(admin.ModelAdmin):
  pass


@admin.register(Product)  
class ProductAdmin(admin.ModelAdmin):
  pass


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    pass
