from django.contrib import admin
from .models import Product,Tea

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)


admin.site.register(Tea)