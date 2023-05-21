from django.urls import path
from .views import *

urlpatterns = [
    path("create_order/", CreateOrder.as_view(), name="create_order"),
    path("total_orders/", RetrieveTotalOrders.as_view(), name="total_orders"),
    path("completed_orders/", RetreiveCompletedOrders.as_view(), name="completed_orders"),
    path("pending_orders/", RetreivePendingOrders.as_view(), name="prnding_orders"),
    path("cancelled_orders/", RetreiveCancelledOrders.as_view(), name="cancelled_orders"),
    path("all_orders/", RetrieveAllOrders.as_view(), name="all_orders")
]