from django.contrib import admin
from .models import Box, InventoryItem

class InventoryItemInline(admin.TabularInline):
    model = InventoryItem
    extra = 1

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('box_number', 'created_at')
    search_fields = ('box_number', 'items__description')
    inlines = [InventoryItemInline]

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'box', 'created_at')
    search_fields = ('description', 'box__box_number')
    list_filter = ('box',)
