"""ngurajekadotcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from merdeka.apps.base.views import merdeka_view, user_login
from merdeka.apps.mdk.views import api_view

urlpatterns = [
    url(r'^$', merdeka_view, name='merdeka_view'),
    url(r'^api/user/login/$', user_login, name='user_login'),
    url(r'^api/(?P<model>[-\w]+)/$', api_view, name='api_view'),
    url(r'^api/(?P<model>[-\w]+)$', api_view, name='api_view'),
    url(r'^api', api_view, name='api_view'),
    url(r'^admin/', include(admin.site.urls)),
]
