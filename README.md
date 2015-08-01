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
* HowMuchCmd和HowMuchWeb是两个相对独立的工程
* HowMuchCmd是核心代码，HowMuchWeb是核心代码的外壳
* HowMuchWeb部分的设计模式学习的是[WeiPython](https://github.com/PegasusWang/WeiPython)，感谢

## 参考项目
* [DWeixin](https://github.com/manyunkai/DWeixin)
* [WeiPython](https://github.com/PegasusWang/WeiPython)
* [littlesnail](https://github.com/liushuaikobe/littlesnail)

### 问题小结
* 因微信需要，Django修改默认端口为80，本机80端口被sql server reporting services服务占用，所以关闭该服务
* db.sqlite3的用户名以及密码均为admin
* superuser的用户名以及密码也均为admin
*

