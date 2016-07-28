#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T14:56:29+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-28T10:05:19+08:00



from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from util.db.jddao import dao
from time import time
# Create your views here.

def detail(request):
    item_id = request.GET.get('item_id')
    if item_id is None:
        response = {
            'code': -1,
            'msg': 'No item_id is provided.'
        }
        return HttpResponse(json.dumps(response))

    args = {
        'item_id': int(item_id)
    }
    item, errormsg = dao.get_item_by_id(args)
    if item is  None:
        response = {
            'code': -2,
            'msg': 'No item is found.'
        }
        return HttpResponse(json.dumps(response))
    if errormsg:
        response = {
            'code': -3,
            'msg': errormsg
        }
        return HttpResponse(json.dumps(response))
    response = {
        'code': 0,
        'msg': 'success',
        'item': item
    }
    return HttpResponse(json.dumps(response))

def comments(request):
    item_id = request.GET.get('item_id')
    if item_id is None:
        response = {
            'code': -1,
            'msg': 'No item_id is provided.'
        }
        return HttpResponse(json.dumps(response))

    # page = int(request.GET.get('page', 0))
    dt_from = int(request.GET.get('dt_from', 0))
    dt_to = int(request.GET.get('dt_to', int(time())))
    args = {
        'item_id': int(item_id),
        # 'page': page,
        'dt_from': dt_from,
        'dt_to': dt_to
    }
    if 'page' in request.GET:
        args['page'] = request.GET['page']
    if 'limit' in request.GET:
        args['limit'] = request.GET['limit']
    comments, errormsg = dao.get_item_comments_by_id(args)
    if comments is None:
        response = {
            'code': -2,
            'msg': 'No item is found.'
        }
        return HttpResponse(json.dumps(response))
    if errormsg:
        response = {
            'code': -3,
            'msg': errormsg
        }
        return HttpResponse(json.dumps(response))
    response = {
        'code': 0,
        'msg': 'success',
        'comments': comments
    }
    return HttpResponse(json.dumps(response))

def item(request):
    return render_to_response('jd/item.html')
