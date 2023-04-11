from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=5000, null=False)

class Plan(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services")
    plan= models.CharField(max_length=256, null=False)
    plan_cost = models.DecimalField(max_digits=256, decimal_places=2, null=False)
    
class PlanDescriptions(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="plans")
    description = models.CharField(max_length=5000, null=False)

