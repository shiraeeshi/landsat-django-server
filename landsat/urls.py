from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^(?P<zoom>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+)/?$', views.zxy, name='zxy'),
        ]
