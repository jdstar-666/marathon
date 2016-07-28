#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T13:54:19+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-28T04:11:57+08:00



"""jdcomment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from console import views
from jdcomment import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^jditem/', include('jditem.urls')),
    url(r'^jduser/', include('jduser.urls')),
    url(r'^jdorder/', include('jdorder.urls')),
    url(r'^comment/', include('comment.urls')),
]

urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
