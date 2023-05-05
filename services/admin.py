from django.contrib import admin
from .models import *
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "image" ]

admin.site.register(Service, ServicesAdmin)

class MiniServicesAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "image", "service" ]

    def service(self, obj):
        return obj.services.name

admin.site.register(MiniServices, MiniServicesAdmin)

class MiniServiceWorksAdmin(admin.ModelAdmin):
    list_display = ["Works", "WorksDescription", "mini_service"]

    def miniservice(self, obj):
        return obj.miniservices.name

admin.site.register(MiniServiceWorkDescription, MiniServiceWorksAdmin)

class WorksAdmin(admin.ModelAdmin):
    list_display = ["Works", "WorksDescription", "service"]

    def service(self, obj):
        return obj.services.name

admin.site.register(WorkDescription, WorksAdmin)

class ExampleServiceAdmin(admin.ModelAdmin):
    list_display = ["image", "mini_service"]

    def miniservice(self, obj):
        return obj.miniservices.name

admin.site.register(ExampleService, ExampleServiceAdmin)