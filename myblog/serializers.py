from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 
            'description',
            'owner'
        )

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields='__all__'