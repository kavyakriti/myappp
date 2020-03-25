from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):

  class Meta:
    model = UserProfile
    fields = ('title', 'dob', 'country', 'city')


class UserSerializer(serializers.HyperlinkedModelSerializer):
  profile = UserProfileSerializer(required=True)

  class Meta:
    model = User
    fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    profile_data = validated_data.pop('profile')
    password = validated_data.pop('password')
    user = User(**validated_data)
    user.set_password(password)
    user.save()
    UserProfile.objects.create(user=user, **profile_data)
    return user

  def update(self, instance, validated_data):
    profile_data = validated_data.pop('profile')
    profile = instance.profile
    instance.email = validated_data.get('email', instance.email)
    instance.save()

    profile.title = profile_data.get('title', profile.title)
    profile.dob = profile_data.get('dob', profile.dob)
    profile.country = profile_data.get('country', profile.country)
    profile.city = profile_data.get('city', profile.city)
    profile.save()
    return instance


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