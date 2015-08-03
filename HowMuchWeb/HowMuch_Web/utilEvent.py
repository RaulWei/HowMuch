# -*- coding: UTF-8 -*-
__author__ = 'weimw'

from django.http import HttpResponse
from models import User
import time
import replyMsg

def subscribe(dictText):
    fromUserName = dictText['ToUserName']
    toUserName = dictText['FromUserName']
    exist = User.objects.filter(openid=toUserName)
    # 已经绑定账号
    if exist.exists():
        reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', '您已经完成账号绑定，回复“帮助”查看更多')
        return HttpResponse(reply, content_type="application/xml")
    # 还没绑定账号
    content = "感谢关注，请先<a href=\"http://howmuchbit.sinaapp.com/grdms/bind?openID=" + toUserName + "\">绑定账号</a>\n\n您可以回复我们来获取信息：\n回复“绑定”将微信号与教务系统账号绑定\n回复“查询成绩”查询研究生阶段所有科目成绩\n回复“帮助”获取本条消息"
    reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', content)
    return HttpResponse(reply, content_type="application/xml")
