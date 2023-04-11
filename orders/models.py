from django.db import models
from users.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    service = models.CharField(max_length=256, null=False)
    cost = models.DecimalField(max_digits=256, decimal_places=2, null=False)
    status = models.CharField(max_length=256, null=False)
    date = models.DateField(auto_now_add=True)