#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T15:05:29+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-28T04:27:58+08:00



from django.conf.urls import patterns, url
from jdorder import views

urlpatterns = [
    url(r'^order/$', views.order),
    url(r'^orders/$', views.all_order),
    url(r'^comment/$', views.comment)
]
    # url((r'^channels/(?P<cid>\w+)/$'), views.channel_updatecollect, name='channel_updatecollect'),
    # url((r'^(?P<app>\w+)/$'), views.channel_getchannelsbyapp, name='channel_getchannelsbyapp'),
    # url((r'^$'),views.index,name ='index'),
# )
