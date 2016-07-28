#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T14:56:53+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-28T13:26:19+08:00



from django.http import HttpResponse
from django.shortcuts import render
import json
from util.db.jddao import dao
from django.conf import settings
from PIL import Image
import uuid
import os
from datetime import datetime
from django.conf import settings
# Create your views here.


def censorship(content):
    if settings.SWITCH['censorship']:
        print type(content)
        if u'哈'in content:
            return False
    return True


def upload_image(request):
    item_id = request.POST.get('item_id')
    print 'item_id', item_id
    if 'picture' not in request.FILES:
        response = {
            'code': -2,
            'msg': 'No picture'
        }
        return HttpResponse(json.dumps(response))

    image = request.FILES['picture']
    # pic_root = os.path.join(settings.MEDIA_ROOT, 'upload', item_id)
    pic_root = os.path.join(settings.MEDIA_ROOT, 'upload')
    if not os.path.isdir(pic_root):
        os.mkdir(pic_root)
    image = Image.open(image)
    name = '%s.jpg'%uuid.uuid1()
    path = os.path.join(pic_root, name)
    image.save(path, 'jpeg')
    response = {
        'code': 0,
        'msg': 'success',
        'name': name
    }
    return HttpResponse(json.dumps(response))


def post_comment(request):
    item_id = request.POST.get('item_id')
    user_id = request.POST.get('user_id')
    # print request.FILES['photo']
    # pictures = request.FILES
    # print pictures
    # pic_root = os.path.join(settings.MEDIA_ROOT, 'items', item_id)
    # if not os.path.isdir(pic_root):
    #     os.mkdir(pic_root)
    # names = []
    # for _, pic in pictures.items():
    #     image = Image.open(pic)
    #     # name = '%s/%s.jpg'%uuid.uuid1()
    #     name = '%s.jpg'%uuid.uuid1()
    #     imgpath = os.path.join(pic_root, name)
    #     image.save(imgpath, 'jpeg')
    #     names.append(name)
    # return
    # response = {
    #     'code': 0,
    #     'debug': True,
    #     'msg': 'success',
    #     'names': names
    # }
    # return HttpResponse(json.dumps(response))
    # print request.POST
    content = request.POST.get('comment')
    print content, censorship(content)
    if not censorship(content):
        response = {
            'code': -2,
            'msg': '评论内容中有不适宜发布的内容，请修改后重新发布~'
        }
        return HttpResponse(json.dumps(response))

    args = {
        # 'pic': ';'.join(names),
        'item_id': item_id,
        'user_id': user_id,
        'score': float(request.POST.get('score')),
        'comment': request.POST.get('comment'),
        'evaluation_time': datetime.now().strftime('%Y-%m-%d %X'),
        'evaluation_pic': ';'.join(request.POST.getlist('pictures[]'))
    }
    dbr, errormsg = dao.post_comment(args)
    if not dbr:
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
