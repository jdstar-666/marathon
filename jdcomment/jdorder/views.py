#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T14:56:35+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-28T04:28:31+08:00



from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import json
from util.db.jddao import dao
from time import time
# Create your views here.



def order(request):
    order_id = request.GET.get('order_id')
    if not order_id:
        response = {
            'code': -1,
            'msg': 'No order id is provided.'
        }
        return HttpResponse(json.dumps(response))

    # page = int(request.GET.get('page', 0))
    # limit = int(request.GET.get('limit', 0))
    args = {
        'order_id': int(order_id),
        # 'page': int(page),
        # 'limit': int(limit)
    }
    items, errormsg = dao.get_items_by_orderid(args)
    if items is None:
        response = {
            'code': -2,
            'msg': 'No item is found.'
        }
        return HttpResponse(json.dumps(response))

    response = {
        'code': 0,
        'msg': 'success',
        'items': items,
        # 'page': page
    }
    return HttpResponse(json.dumps(response))

def all_order(request):
    user_id = request.GET.get('user_id')
    if not user_id:
        response = {
            'code': -1,
            'msg': 'No user_id is provided.'
        }
        return HttpResponse(json.dumps(response))

    dt_from = int(request.GET.get('dt_from', 0))
    dt_to = int(request.GET.get('dt_to', int(time())))
    args = {
        'user_id': user_id,
        # 'limit': limit,
        # 'page': page,
        'dt_from': dt_from,
        'dt_to': dt_to
    }
    if 'page' in request.GET:
        args['page'] = request.GET['page']
    if 'limit' in request.GET:
        args['limit'] = request.GET['limit']
    # page = int(request.GET.get('page', 0))
    # limit =  int(request.GET.get('limit', 0))

    orders, errormsg = dao.get_orders(args)

    if orders is None:
        response = {
            'code': -2,
            'msg': 'No order is found.'
        }
        return HttpResponse(json.dumps(response))
    if errormsg:
        response = {
            'code': -3,
            'msg': errormsg
        }
        return HttpResponse(json.dumps(response))
    # print orders
    response = {
        'code': 0,
        'msg': 'success',
        'orders': orders
    }
    return HttpResponse(json.dumps(response))


def comment(request):
    return render_to_response('jd/comment.html')
