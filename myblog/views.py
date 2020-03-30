from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse,HttpResponse
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,viewsets
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.csrf import csrf_exempt
from newsapi import NewsApiClient
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from myblog import dbconnect
from djoser.views import TokenDestroyView

from .serializers import *
from .models import *

# Create your views here.

class UserAPIView(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserCreateSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = self.get_object(id)
        serializer = UserCreateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = self.get_object(id)
        user.delete()
        return Response(data="Deleted",status=status.HTTP_204_NO_CONTENT)

           

class NewsViewPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3

class NewscategoriesAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsViewPagination





