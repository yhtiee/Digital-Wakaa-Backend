from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("list_service/", RetrieveService.as_view(), name="list_service"),
    path("view_service/<int:pk>/", ViewService.as_view(), name="view_service"),
    path("view_plan/<int:pk>/", ViewPlan.as_view(), name="view_plan")
]