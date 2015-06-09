# HowMuch
北京理工大学研究生教务处机器人

## 功能
* 成绩查询
* 课表查询

>一个悲伤的故事是当我的爬虫还在龟速开发中，官方版本出来了，一下子就没有了开发动力，不过善始善终吧，继续开发它，直到它成为一个确实能称得上是个程序的时候吧，也算是给自己一个交代。

## 注
* HowMuchCmd和HowMuchWeb是两个相对独立的工程
* HowMuchCmd是核心代码，HowMuchWeb是核心代码的外壳
* HowMuchWeb部分的设计模式学习的是[WeiPython](https://github.com/PegasusWang/WeiPython)，感谢

### 问题小结
* 因微信需要，Django修改默认端口为80，本机80端口被sql server reporting services占用，遂解除其占用
* 备注 db.sqlite3 用户名 / 密码为 admin / admin
