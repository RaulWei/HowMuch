# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from GrdmsRobot import GrdmsRobot
from models import User
import time
import wechatUtil

# Create your views here.

def qScore(request, fromUserName, toUserName):
    # get scores store in res
    grdms_root = GrdmsRobot('2120141061', 'weimw52578392')
    res, count = '', 0
    for score in grdms_root.query_points():
        if count != 0:
            res = res + score.contents[7].string + ', ' + \
                  score.contents[19].string + ', ' + score.contents[23].string + ';\r\n'
        count += 1

    # reply by xml
    extTpl = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
    extTpl = extTpl % (fromUserName, toUserName, str(int(time.time())), 'text', res)
    return HttpResponse(extTpl)
    # context = {
    # 'toUserName': fromUserName,
    # 'fromUserName': toUserName,
    #     'createTime': str(int(time.time())),
    #     'msgType': 'text',
    #     'content': res
    # }
    # reply = loader.render_to_string('replyText.xml', context)
    # print(reply)
    # return HttpResponse(reply)

    # return render(request, 'replyText.xml',
    #               {
    #                   'toUserName': fromUserName,
    #                   'fromUserName': toUserName,
    #                   'createTime': int(time.time()),
    #                   'msgType': 'text',
    #                   'content': res,
    #               },
    #               content_type='application/xml')


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
        if wechatUtil.checkSignature(request):
            return HttpResponse(request.GET.get(u'echostr'), content_type="text/plain")
    if request.method == 'POST':
        dictText = wechatUtil.wechatUtil.parseXml(request)

        if dictText['MsgType'] == 'text':
            # 文本
            content = dictText['Content']
            if content == '查询成绩':
                toUserName = dictText['FromUserName']
                fromUserName = dictText['ToUserName']
                return qScore(request, fromUserName, toUserName)
            if content == '查询课表':
                return qCourse(request)

        if dictText['MsgType'] == 'event':
            # 事件
            event = dictText['Event']
            if event == 'subscribe':
                # 关注
                fromUserName = dictText['ToUserName']
                toUserName = dictText['FromUserName']
                content = '感谢关注，请<a href="/bind">绑定账号</a>'
                return render(request, 'replyText.xml', {
                    'toUserName': toUserName,
                    'fromUserName': fromUserName,
                    'createTime': int(time.time()),
                    'msgType': 'text',
                    'content': content,
                },content_type='application/xml')
