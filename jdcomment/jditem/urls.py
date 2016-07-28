#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T15:05:45+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-28T09:56:33+08:00
from django.conf.urls import patterns, url
from jditem import views

urlpatterns = [
    url(r'^detail/$', views.detail),
    url(r'^comments/$', views.comments),
    url(r'^item/$', views.item)
]
    # url((r'^channels/(?P<cid>\w+)/$'), views.channel_updatecollect, name='channel_updatecollect'),
    # url((r'^(?P<app>\w+)/$'), views.channel_getchannelsbyapp, name='channel_getchannelsbyapp'),
    # url((r'^$'),views.index,name ='index'),
