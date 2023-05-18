from django.contrib import admin
from .models import *
# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
    list_display = ["service", "cost", "status", "date", "user"]

admin.site.register(Order, OrdersAdmin)