from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from myblog.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    #other paths
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]