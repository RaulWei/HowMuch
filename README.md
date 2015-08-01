# HowMuch
北京理工大学研究生教务处机器人

## 功能
* 成绩查询
* 课表查询


## 注
* HowMuchCmd和HowMuchWeb是两个相对独立的工程
* HowMuchCmd是核心代码，HowMuchWeb是核心代码的外壳
* HowMuchWeb部分的设计模式学习的是[WeiPython](https://github.com/PegasusWang/WeiPython)，感谢

### 问题小结
* 因微信需要，Django修改默认端口为80，本机80端口被sql server reporting services服务占用，所以关闭该服务
* db.sqlite3的用户名以及密码均为admin
* superuser的用户名以及密码也均为admin
