from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
 

class News(models.Model):
    source = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=5000)
    url=models.URLField(blank=True,null=True)
    urlToImage=models.ImageField(upload_to ='img/',default='img/None/no-img.jpg')
    publishedAt=models.DateTimeField(blank=True,null=True)
    content=models.CharField(max_length=7000)

    def __str__(self):
        return self.title
