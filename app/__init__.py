#coding:utf-8

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

"""扩展实例"""
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    """工厂函数,传入配置名称,返回flask实例"""
    app = Flask(__name__) # 实例化
    app.config.from_object(config[config_name]) # 传入配置对象

    """扩展关联到程序实例"""
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #这里留空,注册蓝本
    from .main import main as main_blueprint # 导入蓝本
    app.register_blueprint(main_blueprint) # 注册蓝本到app

    return app

