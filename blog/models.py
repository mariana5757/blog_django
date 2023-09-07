from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=60)
    password = models.CharField(max_length=62)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Reply(models.Model):
    description = models.CharField(max_length=200)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
