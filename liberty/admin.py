from django.contrib import admin

from django.contrib import admin
from .models import Author, Category, Item



@admin.register(Item)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'bid', 'owner', 'owner_username']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']