from rest_framework import serializers
from .models import *

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class WorkDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDescription
        fields = "__all__"

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = "__all__"

class PlansDescription(serializers.ModelSerializer):
    class Meta:
        model= PlanDescription
        fields = "__all__"

class ExampleService(serializers.ModelSerializer):
    class Meta:
        model = ExampleService
        fields = "__all__"

class MiniServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniServices
        fields = "__all__"

class MiniServicesWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniServiceWorkDescription
        fields = "__all__"

