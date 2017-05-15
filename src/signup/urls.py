"""simple-signup urls

Copyright (c) 2016 Simple is Better Than Complex
Released under MIT license, https://github.com/sibtc/simple-signup/blob/master/LICENSE

Modified to adapt to application configuration

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.signup, name='app-views-signup'),
    url(r'^activation-sent/$', views.account_activation_sent, name='app-views-signup-activation-sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='app-views-signup-activate'),
]
