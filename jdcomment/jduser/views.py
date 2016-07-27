#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T14:56:21+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-27T22:52:45+08:00



from django.shortcuts import render
from django.http import HttpResponse, Http404
import json
# from util.db.jddao import JDDao
from util.db.jddao import dao
# Create your views here.

import md5

def login(request):
    user_name = request.POST.get('user_name')
    user_passwd = request.POST.get('user_passwd')
    if not user_name:
        response = {
            'code': -1,
            'msg': 'No user_name is provided.'
        }
        return HttpResponse(json.dumps(response))
    if not user_passwd:
        response = {
            'code': -2,
            'msg': 'No user_passwd is provided.'
        }
        return HttpResponse(json.dumps(response))
    # md5_user_passwd = md5.new(user_passwd)
    # encryped_passwd = md5_user_passwd.hexdigest()
    encryped_passwd = user_passwd
    args = {
        'user_name': user_name.encode('utf8'),
        'ps': encryped_passwd
    }
    user, errormsg = dao.login(args)
    if not user:
        response = {
            'code': -3,
            'msg': 'No user is found.'
        }
        return HttpResponse(json.dumps(response))
    if errormsg:
        response = {
            'code': -4,
            'msg': errormsg
        }
        return HttpResponse(json.dumps(response))
    del user['ps']
    response = {
        'code': 0,
        'msg': 'success',
        'user': user
    }
    return HttpResponse(json.dumps(response))


def user_get_by_id(request):
    user_id = request.GET['user_id']
    if not user_id:
        response = {
            'code': -5,
            'message': 'No user id is provided.'
        }
        return HttpResponse(json.dumps(response))
    args = {
        'user_id': user_id
    }
    user, errormsg = dao.get_user_by_id(args)

    if not user:
        response = {
            'code': -3,
            'msg': 'No user is found.'
        }
        return HttpResponse(json.dumps(response))
    if errormsg:
        response = {
            'code': -4,
            'msg': errormsg
        }
        return HttpResponse(json.dumps(response))

    del user['ps']
    response = {
        'code': 0,
        'msg': 'success',
        'user': user
    }
    return HttpResponse(json.dumps(response))
