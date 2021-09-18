from django.contrib import admin

from .models import Shop, StockReading

admin.site.register((Shop, StockReading))
