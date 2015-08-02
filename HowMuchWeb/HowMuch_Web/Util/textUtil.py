# -*- coding: UTF-8 -*-
__author__ = 'weimw'


from django.http import HttpResponse
from GrdmsRobot import GrdmsRobot
from models import User
import time
import replyMsg


def qScore(request, fromUserName, toUserName):
    # 先判断是否绑定账号
    user = User.objects.filter(openid=toUserName)
    if not user.exists():
        reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text',
                                      '您未完成账号绑定，请绑定后查询，回复“帮助”查看更多')
        return HttpResponse(reply, content_type="application/xml")

    # get scores store in res
    username = user[0].j_username
    password = user[0].j_password
    grdms_root = GrdmsRobot(username, password)
    res, count = '', 0
    for score in grdms_root.query_points():
        if count == 1:
            res = res + score.contents[7].string + ', ' + \
                  score.contents[19].string + ', ' + score.contents[23].string + ';'
        elif count != 0:
            res = res + "\n" + score.contents[7].string + ', ' + \
                  score.contents[19].string + ', ' + score.contents[23].string + ';'
        count += 1

    # reply by xml
    reply = replyMsg.replyText % (toUserName, fromUserName, str(int(time.time())), 'text', res)
    return HttpResponse(reply, content_type="application/xml")