from rest_framework import serializers
from .models import *

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ( "id", "service", "cost", "status", "date" )