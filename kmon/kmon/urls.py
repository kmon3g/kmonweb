"""kmon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^blog/$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login , name='login' , kwargs= {'template_name':'login.html'}),
    url(r'^logout/$', auth_views.logout , name='logout' , kwargs= {'next_page':'settings.LOGIN_URL'}),
    # url(r'^blog/$', views.blog),
    url(r'^blog/search/(?P<query>[\w\-]+)/$', views.search),
    url(r'^blog/search/(?P<query>[\w\-]+)/(?P<page>\d+)/$', views.search),
    url(r'^blog/(?P<category_title>[\w\-]+)/$', views.blog),
    url(r'^blog/(?P<category_title>[\w\-]+)/(?P<page>\d+)/$', views.blog),
    url(r'^blog/(?P<category_title>[\w\-]+)/read/(?P<entry_id>\d+)/$', views.read),
    url(r'^blog/page/(?P<page>\d+)/$', views.blog),
    url(r'^blog/entry/(?P<entry_id>\d+)/$', views.read),
    url(r'^blog/entry/$', views.read, name='read'),
    url(r'^blog/upload/$', views.create),
]
urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)