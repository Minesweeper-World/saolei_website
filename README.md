# saolei_website
# 新扫雷网

前端：Vue3 + Ts + Element-ui + wasm-bindgen  
后端：Django + Mysql + redis  
部署：Nginx + uwsgi  

## 最新进展
:white_check_mark: 开发核心功能  
:white_check_mark: 租赁服务器  
:white_check_mark: 初步部署  
:white_check_mark: 租赁域名  
:white_check_mark: 备案  
:black_square_button: 删档内测  
:black_square_button: 删档公测  
:black_square_button: 上线  


## 项目安装流程：

本项目可在windows上开发，在Linux上部署。开发调试步骤如下：首先将项目克隆到本地，例如E://saolei_website下

后端：
1. cd saolei_website\back_end\saolei
1. pip install -r requirements.txt
1. 安装mysql，根据saolei_website\back_end\saolei\saolei\setting.py中的配置，（默认）创建名为saolei的数据库，用户名root，密码123456
1. 建立一个文件夹saolei_website\back_end\saolei\logs（用来存放日志）
1. python manage.py makemigrations
1. python manage.py migrate
1. python manage.py runserver

前端：
1. 从[https://github.com/hgraceb/flop-player/releases](https://github.com/hgraceb/flop-player/releases)下载flop播放器，并解压到saolei_website\front_end\public\flop下，使得saolei_website\front_end\public\flop\index.html能够被找到
1. cd saolei_website\front_end
1. npm install
1. npm run serve

## 赞助
感谢您考虑支持我们的开源项目，赞助时请备注您的称呼。您的赞助将有助于项目的持续发展和改进，使我们能够继续提高软件的质量（owner许诺向所有contributor按合理的比例分配赞助得到的收入）。  
### 一般赞助者
- 一次性捐款￥10或以上
- 您的名字将出现在项目的贡献者列表中

### 核心赞助者
- 一次性捐款￥50或以上
- 您的名字将出现在项目的贡献者列表中
- 独家定期报告项目进展  

![](readme_pic/微信收款码.png) ![](readme_pic/支付宝收款码.png)  

