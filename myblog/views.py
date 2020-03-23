from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,viewsets

from .serializers import *
from .models import *

# Create your views here.

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


class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class BusinessAPI(viewsets.ModelViewSet):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()[:5]

class TechnicalAPI(viewsets.ModelViewSet):
    serializer_class = TechnicalSerializer
    queryset = Technical.objects.all()[:5]

class EntertainmentAPI(viewsets.ModelViewSet):
    serializer_class = EntertainmentSerializer
    queryset = Entertainment.objects.all()[:5]

class InternationalAPI(viewsets.ModelViewSet):
    serializer_class = InternationalSerializer
    queryset = International.objects.all()[:5]

class SportsAPI(viewsets.ModelViewSet):
    serializer_class = SportsSerializer
    queryset = Sports.objects.all()[:5]
    
