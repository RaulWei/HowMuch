# -*- coding: UTF-8 -*-
__author__ = 'weimw'

import hashlib
from lxml import etree

def checkSignature(request):
    signature = request.GET.get(u'signature', None)
    timestamp = request.GET.get(u'timestamp', None)
    nonce = request.GET.get(u'nonce', None)
    token = u'weixin'    # your wechat token

    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    tmpstr = '%s%s%s' % tuple(tmplist)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()

    if tmpstr == signature:
        return True
    return False

class wechatUtil(object):

    def __init__(self):
        pass

    @ staticmethod
    def parseXml(request):
        raw_xml = request.body.decode(u'UTF-8')
        xmlstr = etree.fromstring(raw_xml)
        dict_xml = {}
        for child in xmlstr:
            dict_xml[child.tag] = child.text.encode(u'UTF-8')    # note
        return dict_xml



