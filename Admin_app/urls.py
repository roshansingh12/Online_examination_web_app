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
    path('main_admin', views.main_admin, name='main_admin'),
    path('create_teacher', views.create_teacher, name='create_teacher'),
    path('add_teacher', views.add_teacher, name='add_teacher'),
    path('create_student', views.create_student, name='create_student'),
    path('add_student', views.add_student, name='add_student'),
    path('create_class', views.create_class, name='create_class'),
    path('add_class', views.add_class, name='add_class'),

]
