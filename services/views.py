from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import *
from django.contrib.auth.models import User
from . models import *
from rest_framework.permissions import IsAuthenticated, AllowAny

class RetrieveService(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ViewService(APIView):
    def get(self, request,  pk):
        service = Service.objects.filter(pk = pk).values()
        serviceId = service[0]["id"]
        plan = Plan.objects.filter(service_id = serviceId)
        service = Service.objects.filter(id = serviceId)
        serializer_service = ServiceSerializer(service, context={"request": request}, many=True)
        planDescriptions = PlanDescriptions.objects.filter(service_id = serviceId)
        # aboutService = AboutService.objects.filter(service_id = serviceId)
        serializer_plan = PlanSerializer(plan, context={"request": request}, many=True)
        serializer_planDescription = PlanDescriptionSerializer(planDescriptions, context={"request": request}, many=True)
        # serializer_aboutService = AboutServiceSerializer(aboutService, context={"request": request}, many=True)
        return Response(data={
            "status": status.HTTP_200_OK,
            "service": serializer_service.data,
            "plans": serializer_plan.data,
            "descriptions": serializer_planDescription.data,
            # "about": serializer_aboutService.data
        })

class ViewPlan(APIView):
    def get(self, request, pk):
        plan = Plan.objects.filter(pk = pk)
        serializer = PlanSerializer(plan, context={"request":request}, many=True)
        return Response(data={
            "status": status.HTTP_200_OK,
            "plan": serializer.data
        })
