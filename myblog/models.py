from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

 

class News(models.Model):
    category = models.CharField(max_length=1000) 
    source = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    title = models.CharField(max_length=5000)
    description=models.CharField(max_length=5000)
    url=models.URLField(blank=True,null=True)
    urlToImage=models.ImageField(upload_to ='img/',default='img/None/no-img.jpg')
    publishedAt=models.DateTimeField(blank=True,null=True)
    content=models.CharField(max_length=7000)

    def __str__(self):
        return self.title
