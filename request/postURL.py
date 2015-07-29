# -*- coding: UTF-8 -*-
__author__ = 'weimw'

import requests
import codecs

f = codecs.open('postText.xml', 'r', 'utf-8')
content = ''.join(f.readlines())
f.close()
res = requests.post('127.0.0.1:8000', data=content.encode('utf-8'))
print(res.text)
