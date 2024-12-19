from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("",views.index,name='home'),
    path("service",views.math,name='calculator'),
    path("result",views.result,name='result'),
    path("about",views.about,name="about"),
    path("download",views.report,name="report"),
    
    
  
]