from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 
            'description',
            'owner'
        )

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model=Business
        fields = "__all__"

class TechnicalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Technical
        fields = "__all__"

class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Entertainment
        fields = "__all__"

class InternationalSerializer(serializers.ModelSerializer):
    class Meta:
        model=International
        fields = "__all__"

class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sports
        fields = "__all__"


