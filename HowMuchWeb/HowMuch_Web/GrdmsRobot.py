# -*- coding: UTF-8 -*-
__author__ = 'weimw'

j_username = '2120141061'
j_password = 'weimw52578392'

from BeautifulSoup import BeautifulSoup
import requests
import re


class GrdmsRobot:

    def __init__(self, username=0, password=0):
        # 构造函数 登陆教务处并获取cookie
        if username == 0 and password == 0:
            login_data = {
                'loginType': '0',
                'j_username': j_username,
                'j_password': j_password,
            }
        else:
            login_data = {
                'loginType': '0',
                'j_username': username,
                'j_password': password,
            }
        login_headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/42.0.2311.135 Safari/537.36'
        }
        self.login_headers = login_headers
        login_r = requests.post("http://grdms.bit.edu.cn/yjs/login.do", headers=login_headers, data=login_data)
        login_r_soup = BeautifulSoup(''.join(login_r.text))
        if login_r_soup.title.text == u"您的登陆失败！":
            self.login_status = False
        else:
            self.login_status = True
            self.login_cookies = login_r.cookies

        return


    def uni_to_zh(self, str):
        # unicode转中文 返回中文str
        unitozh = {
            'content': str,
            'btn1': 'Unicode 转换 中文',
        }
        unitozh_r = requests.post('http://tool.chinaz.com/Tools/Unicode.aspx', data=unitozh)
        unitozh_soup = BeautifulSoup(''.join(unitozh_r.text), fromEncoding="utf-8")
        return  unitozh_soup.body.findAll('textarea', {'id': 'result'})[0].text

    def query_points(self):
        # 查询成绩 返回成绩表格序列
        points_r = requests.get("http://grdms.bit.edu.cn/yjs/yanyuan/py/pychengji.do?method=enterChaxun",
                                cookies=self.login_cookies)
        points_soup = BeautifulSoup(''.join(points_r.text), fromEncoding="GBK")
        body_content = points_soup.body
        fir_table_content = body_content.table
        sec_table_content = fir_table_content.table

        # 找到学号、姓名、专业信息
        num = sec_table_content.findAll('td')[0].text
        num_content = sec_table_content.findAll('td')[1].text
        name = sec_table_content.findAll('td')[2].text
        name_content = sec_table_content.findAll('td')[3].text
        major = sec_table_content.findAll('td')[6].text
        major_content = sec_table_content.findAll('td')[7].text

        thr_table_content = sec_table_content.table
        points_array = thr_table_content.findAll('tr')
        return points_array

    def query_courses(self, year, term):
        # 查询课程

        # 查询课程的学年 学期
        course_year = 'string:'+year
        course_term = 'string:'+term
        payload_course = {
            'callCount': 1,
            'page': '/yjs/yanyuan/py/pyjxjh.do?method=stdCourseList',
            'httpSessionId': 'yjs-app2~D2B106F71F3ED3771B2E00EEA8D950F1',
            'scriptSessionId': '',
            'c0-scriptName': 'YyPyXkRemoteController',
            'c0-methodName': 'stdSelectedCourseResult',
            'c0-id': 0,
            'c0-param0': course_year,
            'c0-param1': course_term,
            'batchId': 1
        }
        course_r = requests.post('http://grdms.bit.edu.cn/yjs/dwr/call/plaincall/YyPyXkRemoteController.'
                                 'stdSelectedCourseResult.dwr', data=payload_course, headers=self.login_headers, cookies=self.login_cookies)

        str_course_r = course_r.text.encode('utf-8')

        # 统计共有几门课程
        re_str = r'dwr.engine._remoteHandleCallback([^)]*)'
        pattern = re.compile(re_str)
        match = pattern.search(str_course_r)
        course_num = int(match.group(0).encode('utf-8')[match.group(0).encode('utf-8').rfind('s')+1:-1]) + 1
        print(course_num)

        for i in range(course_num):
            # 查找课程代码
            re_str = r's' + str(i) + r'.kcdm=\"[^\"]*\"'
            pattern = re.compile(re_str)
            match = pattern.search(str_course_r)
            kcdm = match.group(0).encode('utf-8')[9:-1]
            print(kcdm)

            # 查找课程名称
            re_str = r's' + str(i) + r'.kczwmc=\"[^\"]*\"'
            pattern = re.compile(re_str)
            match = pattern.search(str_course_r)
            kcmc = GrdmsRobot.uni_to_zh(self, match.group(0).encode('utf-8')[11:-1])
            print(kcmc)

            # 查找学时
            re_str = r's' + str(i) + r'.xs=\"[^\"]*\"'
            pattern = re.compile(re_str)
            match = pattern.search(str_course_r)
            xs = match.group(0).encode('utf-8')[7:-1]
            print(xs)

            # 查找学分
            re_str = r's' + str(i) + r'.xf=\"[^\"]*\"'
            pattern = re.compile(re_str)
            match = pattern.search(str_course_r)
            xf = match.group(0).encode('utf-8')[7:-1]
            print(xf)

            # 查找授课老师
            re_str = r's' + str(i) + r'.skjsxm=\"[^\"]*\"'
            pattern = re.compile(re_str)
            match = pattern.search(str_course_r)
            skjsxm = GrdmsRobot.uni_to_zh(self, match.group(0).encode('utf-8')[11:-1])
            print(skjsxm)

            # 查找上课时间地点
            re_str = r's' + str(i) + r'.sksjdd=\"[^\"]*\"'
            pattern = re.compile(re_str)
            match = pattern.search(str_course_r)
            sksjdd = GrdmsRobot.uni_to_zh(self, match.group(0).encode('utf-8')[11:-1])
            print(sksjdd)

        # 查找用户出生日期
        re_str = r's1.csrq=\"\w*\"'
        pattern = re.compile(re_str)
        match = pattern.search(str_course_r)
        csrq = match.group(0).encode('utf-8')[9:-1]
        print(csrq)

        # 查找用户姓名
        re_str = r's1.czyhxm=\"[^\"]*\"'
        pattern = re.compile(re_str)
        match = pattern.search(str_course_r)
        kczwmc = match.group(0)[11:-1]
        print(GrdmsRobot.uni_to_zh(self, kczwmc))
        return

if __name__ == '__main__':
    grdms_root = GrdmsRobot('2120141061', 'weimw5257839')
    for score in grdms_root.query_points():
        print(score.text)
    grdms_root.query_courses('2014', '第一学期')