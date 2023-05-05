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

class GetService(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "pk"

class GetHowItWOrks(APIView):
    def get(self, request, pk):
        works = WorkDescription.objects.filter(service_id = pk)
        serializer = WorkDescriptionSerializer(works, context={"request":request}, many=True)
        if serializer:
            return Response(data={"status":status.HTTP_200_OK, "howItWorks": serializer.data})
        return Response(data={"status":status.HTTP_400_BAD_REQUEST, "error": "not found"})
    
class RetrieveMiniServices(APIView):
    def get(self, request, pk):
        service = Service.objects.filter(pk = pk).values()
        # print(f"------>{service}")
        mini_services = MiniServices.objects.filter(service_id=service[0]["id"])
        # print(f"------->{mini_services}")
        serializer = MiniServicesSerializer(mini_services, context={"request": request}, many=True)
        if serializer:
            return Response(data={
                "mini_services":serializer.data
            }, status=status.HTTP_200_OK)
        return Response(data={
            "error":"not found"
        }, status=status.HTTP_400_BAD_REQUEST)
    
class RetrieveAllMiniService(generics.ListAPIView):
    queryset = MiniServices.objects.all()
    serializer_class = MiniServicesSerializer

class RetrieveMiniService(generics.RetrieveAPIView):
    queryset = MiniServices.objects.all()
    serializer_class = MiniServicesSerializer
