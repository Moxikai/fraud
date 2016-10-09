#coding:utf-8
"""
定义数据库模型
"""

from . import db

class User(db.Model):
    """用户模型"""
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,index=True)
    email = db.Column(db.String(64),unique=True)
    password_hash = db.Column(db.String(128)) # 密码签名
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id')) # 定义外键


class Role(db.Model):
    """角色模型"""
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role') # 返回Role实例对应的用户列表

class Case(db.Model):
    """案例模型"""
    __tablename__ = 'cases'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),index=True) # 案例标题
    date = db.Column(db.String(128),index=True) # 时间范围
    location = db.Column(db.String(128),index=True) # 案发地点
    persons_involved = db.Column(db.String(128),index=True) # 涉案人员
    company_involved = db.Column(db.Text) # 涉案公司
    fraud_description = db.Column(db.Text) # 诈骗手法
    victim = db.Column(db.Text) # 被害人相关信息
    momeny_quantity = db.Column(db.String(128)) # 涉案金额
    law_enforcement = db.Column(db.String(128)) # 执法机关
    courts = db.Column(db.Text) # 审理法院
    judgment = db.Column(db.Text) # 判决结果
    key_words = db.Column(db.Text) # 案件关键词

class News(db.Model):
    """新闻资讯模型"""
    __tablename__ = 'newses'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(128),index=True) # 标题
    content = db.Column(db.Text) # 新闻内容
    url = db.Column(db.Text) # 采集网址
    source_url = db.Column(db.Text) # 原始网址
    date_publish = db.Column(db.String(64)) # 发布日期
    date_crawl = db.Column(db.String(64)) # 爬虫收录日期

