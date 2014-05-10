from django.contrib import admin
from earthstock.models import Stock

class StockAdmin(admin.ModelAdmin):
    pass
admin.site.register(Stock, StockAdmin)
