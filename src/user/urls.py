"""botw-tracker user app urls

Copyright (c) 2017, Evan Moritz.

botw-tracker is an open source software project released under the MIT License.
See the accompanying LICENSE file for terms.

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='app-views-user-index'),
    url(r'^id/(?P<pk>\d+)/$', views.UserProfileView.as_view(), name='app-views-user-id'),
    url(r'^id/(?P<pk>\d+)/update/$', views.UserProfileUpdate.as_view(), name='app-views-user-update'),
    url(r'^(?P<slug>[\w.@+-]+)/$', views.UserProfileView.as_view(), name='app-views-user'),
]
