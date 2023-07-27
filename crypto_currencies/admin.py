from django.contrib import admin
from . import models


@admin.register(models.Crypto)
class CryptoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'total_supply', 'market_cap', 'volume_change_24h', 'percent_change_24h']
    list_filter = ['name', 'slug', 'price']
    search_fields = ['name', 'slug']
    ordering = ['name']
