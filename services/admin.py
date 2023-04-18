from django.contrib import admin
from .models import *
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "image" ]

admin.site.register(Service, ServicesAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display = [ "plan", "plan_cost", "service" ]

    def service(self, obj):
        return obj.service.name

admin.site.register(Plan, PlanAdmin)

class PlanDescriptionAdmin(admin.ModelAdmin):
    list_display = ["description", "plan", "service" ]

    def service(self, obj):
        return obj.service.name
    
    def plan(self, obj):
        return obj.plan.plan

admin.site.register(PlanDescriptions, PlanDescriptionAdmin)