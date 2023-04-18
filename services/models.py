from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=256, null=False)
    image = models.ImageField(upload_to="service_images")
    description = models.CharField(max_length=5000, null=False)

    def __str__(self) -> str:
        return self.name

class Plan(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services_plan")
    plan= models.CharField(max_length=256, null=False)
    plan_cost = models.DecimalField(max_digits=256, decimal_places=2, null=False)

    def __str__(self) -> str:
        return self.plan
    
class PlanDescriptions(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services_planDescriptions")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="plan_services")
    description = models.CharField(max_length=5000, null=False)

class AboutService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services_about")
    description = models.CharField(max_length=5000, null=False)
    step_1 = models.CharField(max_length=5000, null=False)
    step_2 = models.CharField(max_length=5000, null=False)
    step_3 = models.CharField(max_length=5000, null=False)


