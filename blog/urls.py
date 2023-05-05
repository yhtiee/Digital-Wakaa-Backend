from django.urls import path
from .views import *

urlpatterns = [
    path("list_blog_post/", ListBlogPost.as_view()),
    path("retrieve_blog_post/<int:pk>/", RetrieveBlogPost.as_view())
]