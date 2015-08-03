# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from GrdmsRobot import GrdmsRobot
from models import User
import utilWeChat
import utilText
import utilEvent


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
            return render(request, "bindRes.html", {'bindRes': '您已经绑定账号，无需重复绑定'})
        else:
            # 检查用户名密码是否合法
            j_username = request.POST['username']
            j_password = request.POST['password']
            grd = GrdmsRobot(j_username, j_password)
            if not grd.login_status:
                return render(request, "bindRes.html", {'bindRes': '用户名或密码错误，请返回重新绑定'})

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
        if utilWeChat.checkSignature(request):
            return HttpResponse(request.GET.get(u'echostr'), content_type="text/plain")
    if request.method == 'POST':
        dictText = utilWeChat.parseXml(request)

        if dictText['MsgType'] == 'text':
            # 文本
            content = dictText['Content']
            if content == '查询成绩':
                return utilText.qScore(dictText)
            if content == '查询课表':
                return utilText.qCourse()
            if content == "绑定":
                return utilText.bind(dictText)
            if content == '帮助':
                return utilText.help(dictText)

        if dictText['MsgType'] == 'event':
            # 事件
            event = dictText['Event']
            if event == 'subscribe':
                # 关注
                return utilEvent.subscribe(dictText)
