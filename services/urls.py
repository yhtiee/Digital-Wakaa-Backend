from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("list_service/", RetrieveService.as_view(), name="list_service"),
    path("view_service/<int:pk>/", GetService.as_view(), name="view_service"),
    path("view_works/<int:pk>/", GetHowItWOrks.as_view(), name="view_works"),
    path("mini_services/<int:pk>/", RetrieveMiniServices.as_view(), name="mini_services"),
    path("retrieve_mini_service/", RetrieveAllMiniService.as_view(), name="mini_service"),
    path("retrieve_single_mini_service/<int:pk>/", RetrieveMiniService.as_view(), name="retrieve_single_mini_service"),
]
