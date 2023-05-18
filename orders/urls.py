from django.urls import path
from .views import *

urlpatterns = [
    path("create_order/", CreateOrder.as_view(), name="create_order")
]