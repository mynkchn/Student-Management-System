"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path
from .import views


urlpatterns = [
    path("list/",views.student_list,name='student_list'),
    path("add/",views.add_student,name='add_student'),
    path("edit/<str:slug>",views.edit_student,name='edit_student'),
    path("students/<str:slug>",views.view_student,name='view_student'),
    path("delete/<str:slug>",views.delete_student,name='delete_student'),
    path('blank/',views.blank,name='blank')
    

]
