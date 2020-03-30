from django.conf.urls import url
from myblog import views
from django.urls import path,include

urlpatterns = [
     path('',include('djoser.urls')),
     path('',include('djoser.urls.authtoken')),
    
     path('registerdetail/<int:id>/',views.UserAPIView.as_view()),
]