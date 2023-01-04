from django.contrib import admin
from .models import Order, OrderItem


# OrderItem admin inline
class OrderItemInline(admin.TabularInline):
    '''Inline admin for OrderItem model'''''
    model = OrderItem
    readonly_fields = ('item_total',)


# Order admin
class OrderAdmin(admin.ModelAdmin):
    '''Admin for Order model'''
    inlines = (OrderItemInline,)

    readonly_fields = ('order_number', 'date_placed', 'delivery_cost',
                       'order_total', 'grand_total',)

    fields = ('order_number', 'date_placed', 'full_name', 'email',
              'phone_number', 'country', 'postcode', 'city',
              'street_address1', 'street_address2', 'county',
              'delivery_cost', 'order_total', 'grand_total',)

    list_display = ('order_number', 'date_placed', 'full_name', 'order_total',
                    'delivery_cost', 'grand_total',)

    ordering = ('-date_placed',)


admin.site.register(Order, OrderAdmin)
