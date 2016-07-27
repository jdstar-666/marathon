#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T14:56:53+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-27T22:29:25+08:00



from django.http import HttpResponse
from django.shortcuts import render
import json
from util.db.jddao import dao
from django.conf import settings
from PIL import Image
import uuid
import os
# Create your views here.


def post_comment(request):
    item_id = request.POST.get('item_id')
    # print request.FILES['photo']
    pictures = request.FILES
    pic_root = os.path.join(settings.MEDIA_ROOT, 'items', item_id)
    if not os.path.isdir(pic_root):
        os.mkdir(pic_root)
    names = []
    for _, pic in pictures.items():
        image = Image.open(pic)
        # name = '%s/%s.jpg'%uuid.uuid1()
        name = '%s.jpg'%uuid.uuid1()
        imgpath = os.path.join(pic_root, name)
        image.save(imgpath, 'jpeg')
        names.append(name)
    # return
    response = {
        'code': 0,
        'debug': True,
        'msg': 'success',
        'names': names
    }
    return HttpResponse(json.dumps(response))
    args = {
        'pic': ';'.join(names),
        'item_id': int(item_id),
        'user_name': user_name
    }
    errormsg = dao.post_comment(args)
    if errormsg:
        response = {
            'code': -1,
            'msg': errormsg
        }
        return HttpResponse(json.dumps(response))

    response = {
        'code': 0,
        'msg': 'success'
    }
    return HttpResponse(json.dumps(response))
