from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=256, null=False)
    sub_title = models.CharField(max_length=256, null=False)
    post = models.CharField(max_length=5000, null=False)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="blog_images")

class Interaction(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    comments = models.CharField(max_length=1000, null=False)
