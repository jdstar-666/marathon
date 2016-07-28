#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T23:49:35+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-27T23:50:13+08:00

from django.shortcuts import render_to_response

def index(request):
    return render_to_response('jd/index.html')
