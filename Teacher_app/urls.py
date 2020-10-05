"""online_exam_app URL Configuration

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
from . import views
urlpatterns = [
    path('teacher_profile', views.teacher_profile, name='teacher_profile'),
    path('teacher', views.teacher, name='teacher'),
    path('create_test', views.create_test, name='create_test'),
    path('creating_test', views.creating_test, name='creating_test'),
    path('check_result', views.check_result, name='check_result'),


]
