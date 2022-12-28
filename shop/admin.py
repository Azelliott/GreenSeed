from django.contrib import admin
from .models import Category, Product


# CategoryAdmin
class CategoryAdmin(admin.ModelAdmin):
    '''CategoryAdmin'''
    list_display = (
        'name',
        'friendly_name',
        'description',
        'slug',
    )

    ordering = ('name',)
    search_fields = ('name', 'friendly_name', 'description', 'slug')
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)


# ProductAdmin
class ProductAdmin(admin.ModelAdmin):
    '''ProductAdmin'''
    list_display = (
        'category',
        'name',
        'description',
        'price',
        'image',
        'availability',
        'rating',
    )

    ordering = ('name',)
    search_fields = ('name', 'description', 'price', 'availability', 'rating')
    list_per_page = 25


admin.site.register(Product, ProductAdmin)