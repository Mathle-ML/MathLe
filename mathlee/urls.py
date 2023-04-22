"""mathlee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from mathlee.views import *
from mathlee import dbViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard/', dbViews.dashboard, name='dashboard'),
    path('dashboard/<str:lvl>/', dbViews.temas, name='temas'),
    path('dashboard/<str:lvl>/<str:tma>/', dbViews.actividades, name='actividades'),
    path('login/', loginNoArg, name='login'),
    path('login/<str:rdc>', loginArg, name='login'),
    path('logout/', exit, name='logout'),
    path('register/', regNoArg, name='register'),
    path('register/<str:usr>', regArg, name='register'),

    path('actividad_rush/', actividad_prueba, name='act'),
    path('resultado/<int:r1>/<int:r2>/<int:r3>/<int:r4>/<int:r5>/', resultado, name='resultado'),
    path('actividad_teorica', actividad_T, name='act_t')
]
