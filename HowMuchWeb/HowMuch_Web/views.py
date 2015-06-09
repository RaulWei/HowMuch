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