"""botw-tracker URL Configuration

Copyright (c) 2017, Evan Moritz.

botw-tracker is an open source software project released under the MIT License.
See the accompanying LICENSE file for terms.

"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from .config_local import USE_SIGNUP

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'admin/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^quests/', include('quests.urls')),
    url(r'^user/', include('user.urls')),
]

if USE_SIGNUP:
    urlpatterns.append(url(r'^signup/', include('signup.urls')))
