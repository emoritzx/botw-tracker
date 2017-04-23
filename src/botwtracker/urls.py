"""botwtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/

"""
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^quests/', include('quests.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^admin/', admin.site.urls),
]
