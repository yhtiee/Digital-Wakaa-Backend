from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class CreatePost(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ListBlogPost(generics.ListAPIView):
    queryset = Blog.objects.all().order_by("-pk")
    serializer_class = BlogSerializer

class RetrieveBlogPost(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"