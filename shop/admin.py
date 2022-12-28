from django.contrib import admin
from .models import Category, Product


# CategoryAdmin
class CategoryAdmin(admin.ModelAdmin):
    '''CategoryAdmin'''
    readonly_fields = ('id',)
    list_display = (
        'id',
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

    def category_name(self, obj):
        return obj.category.name
    category_name.admin_order_field = 'category__name'
    category_name.short_description = 'Category'

    list_display = (
        'category_name',
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