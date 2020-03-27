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
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from django.views.decorators.csrf import csrf_exempt
from newsapi import NewsApiClient
from rest_framework.pagination import LimitOffsetPagination
from myblog import dbconnect
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from myapp.permissions import IsLoggedInUserOrAdmin, IsAdminUser

from .serializers import *
from .models import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
  def get_permissions(self):
    permission_classes = []
    if self.action == 'create':
      permission_classes = [AllowAny]
    elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
      permission_classes = [IsLoggedInUserOrAdmin]
    elif self.action == 'list' or self.action == 'destroy':
      permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]


class TestView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
        # serializer = PostSerializer(qs, many=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PostView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, id=None):
        return self.update(request,id)

    def delete(self, request):
        return self.destroy(request,id)


class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
           

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class NewsViewPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 30

class NewscategoriesAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsViewPagination





