# HowMuch
北京理工大学研究生教务处机器人

## 功能
* 成绩查询
* 课表查询(暂无)

## 包依赖
* python == 2.7.9
* django == 1.8
* MySQL-python == 1.2.5
* lxml == 3.4.4
* BeautifulSoup == 3.2.1

## 效果展示
<img src='/Effect_Picture/Screenshot_2015-08-01-19-22-48.png' width=250 />
<img src='/Effect_Picture/Screenshot_2015-08-01-19-22-55.png' width=250 />
<img src='/Effect_Picture/Screenshot_2015-08-01-19-23-44.png' width=250 />

## 注
- HowMuchCmd是北京理工大学研究生教务管理系统脚本核心程序
- HowMuchWeb是将上述脚本嵌入Django框架搭建的基于微信公众平台的应用程序
- 本项目部署到SAE的教程详见我的博客园
  + [【解决】Django项目废弃SQLite3拥抱MySQL](http://www.cnblogs.com/raul-ac/p/4181295.html)
  + [【解决】SAE部署Django1.6+MySQL](http://www.cnblogs.com/raul-ac/p/4183400.html)

## 参考项目
* [DWeixin](https://github.com/manyunkai/DWeixin)
* [WeiPython](https://github.com/PegasusWang/WeiPython)
* [littlesnail](https://github.com/liushuaikobe/littlesnail)

## 问题小结
* 微信公众平台接口调用仅支持80端口，本机80端口被sql server reporting services服务占用需关闭
* db.sqlite3 用户名[admin] 密码[admin]
* superuser 用户名[admin] 密码[admin]

## 二维码
![Alt text](/Effect_Picture/qrcode_for_gh_bd2412043977_258.jpg)
