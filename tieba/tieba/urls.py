"""tieba URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from daxue import views as daxue_views

from . import settings

urlpatterns = [
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}, name='static'),
    url(r'^add/(\d+)/(\d+)/$', daxue_views.add2, name='add2'),
    url(r'^add/$', daxue_views.add),
    url(r'^$', daxue_views.index, name='index'),
    url(r'^index$', daxue_views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catch$', daxue_views.catch, name='catch'),
    url(r'^sex$', daxue_views.sex, name='sex'),
    url(r'^client$', daxue_views.client, name='client'),
    url(r'^month$', daxue_views.month, name='month'),
    url(r'^hour$', daxue_views.hour, name='hour'),
    url(r'^title$', daxue_views.title, name='title'),
    url(r'^post$', daxue_views.post, name='post'),
    url(r'^review$', daxue_views.review, name='review'),
    url(r'^abc$', daxue_views.abc, name='abc'),
]
