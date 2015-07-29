# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from GrdmsRobot import GrdmsRobot
from models import User
import wechatUtil

# Create your views here.

def qScore(request):
    grdms_root = GrdmsRobot('2120141061', 'weimw52578392')
    res = ''
    for score in grdms_root.query_points():
        res = res + score.text + '\r\n'

    return HttpResponse(res)

def qCourse(request):
    return HttpResponse('qCourse')

def bind(request):
    if request.method == 'GET':
        # 跳转到绑定用户界面
        t = loader.get_template("bind.html")
        c = Context({})
        return HttpResponse(t.render(c))
    elif request.method == 'POST':
        # 检查数据库是否有此用户 如果没有则存入数据库
        exist = User.objects.filter(j_username=request.POST['username'])
        if exist.exists():
            t = loader.get_template("bindError.html")
            c = Context({})
            return HttpResponse(t.render(c))
        else:
            user = User()
            user.j_username = request.POST['username']
            user.j_password = request.POST['password']
            user.save()
            t = loader.get_template("bindSuccess.html")
            c = Context({})
            return HttpResponse(t.render(c))

def grdms(request):
    if request.method == 'GET':
        return HttpResponse(wechatUtil.checkSignature(request), content_type="text/plain")
    if request.method == 'POST':
        return HttpResponse() # to do
    return