from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .serializers import *
from django.contrib.auth.models import User
from . models import *
# Create your views here.


class CreateOrder(APIView):

    def post(self, request):
        user = request.user
        service = request.data["service"]
        cost = request.data["cost"]
        service_status = request.data["status"]
        user_data = User.objects.filter(username=user.username).values()
        user_id = user_data[0]["id"]

        if user_id :
            orders = Order.objects.create(user_id=user_id, service=service, cost=cost, status=service_status)
            orders.save()

            return Response(data={
                "success":"order successfully created",
            }, status=status.HTTP_201_CREATED)
        
        return Response(data={
            "error":"user not found"
        }, status=status.HTTP_400_BAD_REQUEST)


class RetrieveTotalOrders(APIView):
    def get(self, request):
        user = request.user
        user_data = User.objects.filter(username = user.username).values()
        if user:
            user_ID = user_data[0]["id"]
            orders =Order.objects.filter(user_id = user_ID)
            total = len(orders)

            return Response(data={
                "total_orders": total
            }, status=status.HTTP_200_OK)
        
        return Response(data={
            "error": "not found"
        }, status=status.HTTP_400_BAD_REQUEST)

class RetreivePendingOrders(APIView):
    def get(self, request):
        user = request.user
        user_data = User.objects.filter(username =user.username).values()
        user_ID = user_data[0]["id"]
        orders = Order.objects.filter(user_id = user_ID).values()
        pending = []
        for x in orders:
            if x["status"] == "Pending":
                pending.append(x)
        total_pending = len(pending)

        return Response(data={
            "pending_orders": total_pending
        }, status=status.HTTP_200_OK)
    

class RetreiveCompletedOrders(APIView):
    def get(self, request):
        user = request.user
        user_data = User.objects.filter(username =user.username).values()
        user_ID = user_data[0]["id"]
        orders = Order.objects.filter(user_id = user_ID).values()
        completed = []
        for x in orders:
            if x["status"] == "Completed":
                completed.append(x)
        total_completed = len(completed)

        return Response(data={
            "completed_orders": total_completed
        }, status=status.HTTP_200_OK)
    

class RetreiveCancelledOrders(APIView):
    def get(self, request):
        user = request.user
        user_data = User.objects.filter(username=user.username).values()
        user_ID = user_data[0]["id"]
        orders = Order.objects.filter(user_id = user_ID).values()
        cancel = []
        for x in orders:
            if x["status"] == "Cancelled":
                cancel.append(x)
        total_cancelled = len(cancel)

        return Response(data={
            "cancelled_orders": total_cancelled
        }, status=status.HTTP_200_OK)
    
class RetrieveAllOrders(APIView):
    def get(self, request):
        user = request.user
        user_data = User.objects.filter(username=user.username).values()
        user_ID = user_data[0]["id"]
        orders = Order.objects.filter(user_id = user_ID).values()
        serializer = OrdersSerializer(orders, context={"request":request}, many=True )
        if serializer:
            return Response(data={
                "orders": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(data = {
            "error": serializer.error
        }, status=status.HTTP_400_BAD_REQUEST)
