# -*- coding: UTF-8 -*-
__author__ = 'weimw'

from django.http import HttpResponse
from GrdmsRobot import GrdmsRobot
from models import User
import time
import replyMsg


def qScore(dictText):

    # 先判断是否绑定账号
    toUserName = dictText['FromUserName']
    fromUserName = dictText['ToUserName']
    user = User.objects.filter(openid=toUserName)
    if not user.exists():
        reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', '您未完成账号绑定，请绑定后查询，回复“帮助”查看更多')
        return HttpResponse(reply, content_type="application/xml")

    # get scores store in res
    username = user[0].j_username
    password = user[0].j_password
    grdms_root = GrdmsRobot(username, password)
    res, count = '', 0
    for score in grdms_root.query_points():
        if count == 1:
            res = res + score.contents[7].string + ', ' + score.contents[19].string + ', ' + score.contents[23].string + ';'
        elif count != 0:
            res = res + "\n" + score.contents[7].string + ', ' + score.contents[19].string + ', ' + score.contents[23].string + ';'
        count += 1

    # reply by xml
    reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', res)
    return HttpResponse(reply, content_type="application/xml")


def qCourse():
    return HttpResponse('qCourse')


def bind(dictText):
    toUserName = dictText['FromUserName']
    fromUserName = dictText['ToUserName']
    exist = User.objects.filter(openid=toUserName)
    if exist.exists():
        # 绑定过 则返回提示
        reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', '您已经完成账号绑定，回复“帮助”查看更多')
        return HttpResponse(reply, content_type="application/xml")
    else:
        # 没绑定过 则返回url
        replyContent = "<a href=\"http://howmuchbit.sinaapp.com/grdms/bind?openID=" + toUserName + "\">绑定账号</a>"
        reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', replyContent)
        return HttpResponse(reply, content_type="application/xml")


def help(dictText):
    toUserName = dictText['FromUserName']
    fromUserName = dictText['ToUserName']
    replyContent = "您可以回复我们来获取信息：\n回复“绑定”将微信号与教务系统账号绑定\n回复“查询成绩”查询研究生阶段所有科目成绩\n回复“帮助”获取本条消息"
    reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', replyContent)
    return HttpResponse(reply, content_type="application/xml")
