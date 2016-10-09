#coding:utf-8

"""
启动脚本
"""
import os

from app import create_app,db # 导入工厂函数
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default') # 传入配置名称,返回app实例
manager = Manager(app) # 脚本管理扩展初始化
migrate = Migrate(app,db) # 数据库迁移扩展,传入app实例,数据库

def make_shell_context():
    """上下文"""

if __name__ == '__main__':
    manager.run()