from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'full_name',
        'phone',
        'city',
        'total_price',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
        'city'
    )

    search_fields = (
        'full_name',
        'phone',
        'city'
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)