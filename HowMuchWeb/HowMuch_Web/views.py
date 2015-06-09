from django.shortcuts import render
from django.http import HttpResponse
from GrdmsRobot import GrdmsRobot

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
        return
    elif request.method == 'POST':
        # 检查数据库是否有此用户 如果没有则存入数据库
        return 