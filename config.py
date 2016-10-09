#coding:utf-8
import os

baseDir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """基础配置"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'it is my password' # 表单的keygen


class DevelopmentConfig(Config):
    """本地开发配置"""
    DEBUG = True # 调试模式
    #MAIL_SERVER = '' # 邮件服务器
    #MAIL_PORT = '' # 邮件服务器端口
    #MAIL_USE_TLS = '' # 是否使用TLS
    #MAIL_USE_SSL = '' # 是否使用SSL
    #MAIL_USERNAME = '' # 邮箱账户
    #MAIL_PASSWORD = '' # 邮箱密码
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(baseDir,'dev.db') # 数据库地址


class TestingConfig(Config):
    """测试模式"""
    TESTING = True # 测试模式
    SQLALCHEMY_DATABASE_URI = ''

class ProductionConfig(Config):
    """生产环境配置"""
    SQLALCHEMY_DATABASE_URI = ''

# 设置配置字典
config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestingConfig,
    'default':DevelopmentConfig
}

