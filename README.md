# <a href="https://github.com/eee555/saolei_website" >开源扫雷网（OPEN MINESWEEPER WEBSITE）</a>

[![saolei_website](https://img.shields.io/badge/saolei_website-v1.7-brightgreen.svg)](https://github.com/eee555/Solvable-Minesweeper)
[![stars](https://img.shields.io/github/stars/eee555/saolei_website)](https://github.com/eee555/saolei_website/stargazers)
[![forks](https://img.shields.io/github/forks/eee555/saolei_website)](https://github.com/eee555/saolei_website/forks)

[English](Readme_en.md)

项目已正式上线！

前端：Vue3 + Ts + Element-ui + wasm  
后端：Django + Mysql + redis  
部署：Nginx + uwsgi + acme.sh  
安全：百度大脑  

## 项目安装流程：

本项目可在windows上开发，在Linux上部署。开发调试步骤如下：首先将项目克隆到本地，例如E://saolei_website下

后端：
1. cd saolei_website\back_end\saolei
1. pip install -r requirements.txt
1. 安装mysql，根据saolei_website\back_end\saolei\saolei\setting.py中的配置，（默认）创建名为saolei的数据库，用户名root，密码123456
1. 新建一个文件夹saolei_website\back_end\saolei\logs（用来存放日志）
1. 新建一个文件夹saolei_website\back_end\saolei\assets（存放录像、头像、文章）
1. （可选，假如需要看文章）在saolei_website\back_end\saolei\assets下执行`git clone https://gitee.com/ee55/saolei_website_article.git`，并将文件夹名由saolei_website_article改为article
1. python manage.py makemigrations
1. python manage.py migrate userprofile
1. python manage.py migrate
1. python manage.py runserver --nostatic
1. （可选，假如要启动定时任务，不做相关功能时可以不启动）
   ```
   python manage.py runapschedulermonitor
   python manage.py runapscheduleruserprofile
   python manage.py runapschedulervideomanager
   ```

前端：
1. 从[https://github.com/eee555/flop-player/releases/download/v1.1/dist.zip](https://github.com/eee555/flop-player/releases/download/v1.1/dist.zip)下载新版flop播放器，并解压到saolei_website\front_end\public\flop下（将文件夹的名称dist修改为flop），使得saolei_website\front_end\public\flop\index.html能够被找到
2. cd saolei_website\front_end
3. 如果使用npm，则npm install；如果知道什么是yarn且使用yarn，则yarn
4. 如果使用npm，则npm run dev；如果知道什么是yarn且使用yarn，则yarn dev

特殊的调试参数：位于`backend\saolei\config\flags.py`

## 链接




## 赞助
感谢您考虑支持我们的开源项目，赞助时请备注您的称呼和赞助的对象。赞助对象分为团队、网站运营、个人，如果没有备注，默认用于网站运营。您的赞助将有助于项目的持续发展和改进，使我们能够继续提高软件的质量。对团队整体的赞助，owner许诺向所有contributor按commit数量比例分配赞助得到的收入。

### 一般赞助者
- 一次性捐款￥10或以上
- 您的名字将出现在项目的贡献者列表中

### 核心赞助者
- 一次性捐款￥50或以上
- 您的名字将出现在项目的贡献者列表中
- 独家定期报告项目进展  

## 贡献者列表

| 赞助人 | 金额 | 时间 | 渠道 | 赞助对象 | 分配情况 |
| :------: | :-----:  | :----------: | :------: | :------:| :------: |
| *翌 | ¥100.00 | 2023-11-11 | 支付宝 | 网站 | 未分配 |

## 网站运营支出

| 项目 | 金额 | 时间 | 
| :------: | :-----:  | :----------: |
| 服务器 | ¥89.14 | 2023-12-03 |
| 域名   | ¥1.00  | 2023-12-11 |

当前账户余额：￥9.86

下期预计时间：2024.12.02

下期预计金额：￥90.00-550.00

![](readme_pic/微信收款码.png) ![](readme_pic/支付宝收款码.png)  

