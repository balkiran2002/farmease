from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('id', 'product_id', 'product_name', 'category', 'price', 'quantity', 'seasons', 'soil_type')
    
    # Fields that can be searched in the admin search bar
    search_fields = ('product_id', 'product_name', 'category', 'seasons', 'soil_type', 'crops')
    
    # Filters available on the right sidebar
    list_filter = ('category', 'seasons', 'soil_type')
    
    # Fields to edit directly in the list view
    list_editable = ('price', 'quantity')
    
    # Default ordering in the list view
    ordering = ('product_name',)
    
    # Fields to display when adding or editing an Item
    fieldsets = (
        ('Basic Information', {
            'fields': ('product_id', 'product_name', 'category', 'price', 'quantity')
        }),
        ('Additional Details', {
            'fields': ('seasons', 'crops', 'soil_type', 'photo', 'description')
        }),
    )
