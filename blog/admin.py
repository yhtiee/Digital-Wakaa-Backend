from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "sub_title", "post", "image"]

admin.site.register(Blog, BlogAdmin)