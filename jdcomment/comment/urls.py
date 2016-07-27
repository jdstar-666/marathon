#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T15:06:20+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-27T19:43:49+08:00


from django.conf.urls import patterns, url
from comment import views

urlpatterns = [
    url(r'^post/$', views.post_comment),
]
    # url((r'^channels/(?P<cid>\w+)/$'), views.channel_updatecollect, name='channel_updatecollect'),
    # url((r'^(?P<app>\w+)/$'), views.channel_getchannelsbyapp, name='channel_getchannelsbyapp'),
    # url((r'^$'),views.index,name ='index'),
# )
