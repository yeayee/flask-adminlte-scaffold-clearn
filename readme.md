# flask-adminlte-handler
## 简介
flask-adminlte-handler是一个Python环境下的WEB后台管理系统脚手架，目标是用极少量的代码，快速构建小型WEB应用。

原项目地址：https://github.com/xiiiblue/flask-adminlte-scaffold/tree/master

0. 个人根据项目实际选择对应的数据库
1. 使用较传统的重后端+轻前端的方式，降低总体代码量
2. Web框架使用Flask，默认Jinja模版
3. ORM框架使用Peewee
4. 前端套用基于BootStrap的AdminLTE模板

## 更新说明
- 2023-11-30
  极简打开本项目，体验AdminLTE模板


## 第三方依赖

- flask
- flask-script
- flask-wtf
- flask-login


## 环境配置
### venv虚拟环境安装配置
```
sudo pip3 install virtualenv
virtualenv venv
. venv/bin/activate
```

### 第三方依赖安装
```
pip3 install -r requirements.txt

```
### 系统参数配置
1. 编辑`config.py`， 修改SECRET_KEY及MySQL数据库相关参数
```
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret'
```

2. 编辑log-app.conf，修改日志路径
```
args=('/path/to/log/flask-rest-sample.log','a','utf8')
```

### 数据库初始化
1. 自动建表
直接运行`python3 models.py`

2. 插入管理员用户（默认admin/admin，'管理员', 'admin@intumu.com', '18602931213')
```
初始版本不涉及数据库，个人根据项目实际选择对应的数据库。
```

### 启动应用
```
nohup ./manage.py runserver 2>&1 &
或
./run_app_dev.py (仅限测试)
```


## 项目目录结构

- /app/auth  用户认证相关代码
- /app/main  主要功能点相关代码
- /app/static  JS、CSS等静态文件
- /app/template  页面模版
- /app/models.py  Peewee模型
- /app/utils.py  工具模块
- /conf  系统参数及日志配置


## 相关学习文档
- [https://intumu.com](https://intumu.com)
