from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^id/(?P<pk>\d+)/$', views.UserProfileView.as_view()),
    url(r'^(?P<slug>[\w.@+-]+)/$', views.UserProfileView.as_view())
]
