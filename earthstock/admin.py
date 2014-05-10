from django.contrib import admin
from earthstock.models import Stock, Quote

class QuoteInline(admin.TabularInline):
    model = Quote

class StockAdmin(admin.ModelAdmin):
    model = Stock
    inlines = [
        QuoteInline
    ]

admin.site.register(Stock, StockAdmin)