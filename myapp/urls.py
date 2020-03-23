"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from myblog.views import TestView
from rest_framework import routers
from myblog import views

router = routers.DefaultRouter()

router.register('Business', views.BusinessAPI)
router.register('Technical', views.TechnicalAPI)
router.register('International', views.InternationalAPI)
router.register('Entertainment', views.EntertainmentAPI)
router.register('Sports', views.SportsAPI)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('app/', TestView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('', include(router.urls)),
]
