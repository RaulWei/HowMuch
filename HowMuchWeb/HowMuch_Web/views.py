# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from GrdmsRobot import GrdmsRobot
from models import User

# Create your views here.

def qScore(request):
    grdms_root = GrdmsRobot('2120141061', 'weimw52578392')
    res = ''
    for score in grdms_root.query_points():
        res = res + score.text + '\n'

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
        if exist == '':
            user = User()
            user.j_username = request.POST['username']
            user.j_password = request.POST['password']
            user.save()
            return HttpResponse('绑定成功')
        return HttpResponse('用户已存在')

def grdms(request):
    return