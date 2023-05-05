from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=256, null=False)
    image = models.ImageField(upload_to="service_images")
    description = models.CharField(max_length=5000, null=False)

    def __str__(self) -> str:
        return self.name
    
class MiniServices(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="mini_services")
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=5000, null=False)
    image = models.ImageField(upload_to="service_images")

    def __str__(self) -> str:
        return self.name

class MiniServiceWorkDescription(models.Model):
    mini_service = models.ForeignKey(MiniServices, on_delete=models.CASCADE, related_name="mini_service_work")
    Works = models.CharField(max_length=256, null=False)
    WorksDescription = models.CharField(max_length=5000, null=False)  

class WorkDescription(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services_workDescriptions")
    Works = models.CharField(max_length=256, null=False)
    WorksDescription = models.CharField(max_length=5000, null=False)

class Plans(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services_plans")
    plan = models.CharField(max_length=256, null=False)
    plan_cost_mini = models.DecimalField(max_digits=256, decimal_places=2)
    plan_cost_pro = models.DecimalField(max_digits=256, decimal_places=2)
    plan_cost_master = models.DecimalField(max_digits=256, decimal_places=2)

    def __str__(self) -> str:
        return self.plan

class PlanDescription(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services_plan")
    plans = models.ForeignKey(Plans, on_delete=models.CASCADE, related_name="plan_services")
    descriptions = models.CharField(max_length=256, null=False)

class ExampleService(models.Model):
    mini_service = models.ForeignKey(MiniServices, on_delete=models.CASCADE, related_name="services_examples")
    image = models.FileField(upload_to="examples")