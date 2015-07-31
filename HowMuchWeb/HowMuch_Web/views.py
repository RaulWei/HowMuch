# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from GrdmsRobot import GrdmsRobot
from models import User
import time
import wechatUtil
import replyMsg

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
    reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', res)
    return HttpResponse(reply, content_type="application/xml")


def qCourse(request):
    return HttpResponse('qCourse')


def bind(request):
    if request.method == 'GET':
        # 跳转到绑定用户界面
        t = loader.get_template("bind.html")
        c = Context({'openid': request.GET.get('openID')})
        return HttpResponse(t.render(c))
    elif request.method == 'POST':
        # 检查数据库是否有此用户 如果没有则存入数据库
        exist = User.objects.filter(openid=request.POST['openid'])
        if exist.exists():
            t = loader.get_template("bindError.html")
            c = Context({})
            return HttpResponse(t.render(c))
        else:
            user = User()
            user.openid = request.POST['openid']
            user.j_username = request.POST['username']
            user.j_password = request.POST['password']
            user.save()
            t = loader.get_template("bindRes.html")
            c = Context({'bindRes': '绑定成功'})
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
            toUserName = dictText['FromUserName']
            fromUserName = dictText['ToUserName']
            if content == '查询成绩':
                return qScore(request, fromUserName, toUserName)
            if content == '查询课表':
                return qCourse(request)
            if content == "绑定":
                exist = User.objects.filter(openid=toUserName)
                if exist.exists():
                    reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', '您已经完成账号绑定，回复“帮助”查看更多')
                    return HttpResponse(reply, content_type="application/xml")
                else:
                    replyContent = "<a href=\"http://1.howmuchbit.sinaapp.com/grdms/bind?openID=" + toUserName + "\">绑定账号</a>"
                    reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', replyContent)
                    return HttpResponse(reply, content_type="application/xml")
            if content == '帮助':
                replyContent = "您可以回复我们来获取信息：\n回复“绑定”将微信号与教务系统账号绑定\n" \
                               "回复“查询成绩”查询研究生阶段所有科目成绩\n回复“帮助”获取本条消息"
                reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', replyContent)
                return HttpResponse(reply, content_type="application/xml")

        if dictText['MsgType'] == 'event':
            # 事件
            event = dictText['Event']
            if event == 'subscribe':
                # 关注
                fromUserName = dictText['ToUserName']
                toUserName = dictText['FromUserName']
                exist = User.objects.filter(openid=toUserName)
                # 已经绑定账号
                if exist.exists():
                    reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())),
                                                  'text', '您已经完成账号绑定，回复“帮助”查看更多')
                    return HttpResponse(reply, content_type="application/xml")
                # 还没绑定账号
                content = "感谢关注，请先<a href=\"http://1.howmuchbit.sinaapp.com/grdms/bind?openID=" \
                          + toUserName + "\">绑定账号</a>\n\n您可以回复我们来获取信息：\n回复“绑定”将微信号与教务系统账号绑定\n" \
                                         "回复“查询成绩”查询研究生阶段所有科目成绩\n回复“帮助”获取本条消息"
                reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', content)
                return HttpResponse(reply, content_type="application/xml")
