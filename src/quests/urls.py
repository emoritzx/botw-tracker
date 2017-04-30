"""botw-tracker quests app urls

Copyright (c) 2017, Evan Moritz.

botw-tracker is an open source software project released under the MIT License.
See the accompanying LICENSE file for terms.

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='app-views-quests-index'),
]
