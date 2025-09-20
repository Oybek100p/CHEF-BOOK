from django.contrib import admin

from django.contrib import admin
from .models import Category, Chef, Recipe, Main

admin.site.register(Category)
admin.site.register(Chef)
admin.site.register(Recipe)
admin.site.register(Main)

# Register your models here.
