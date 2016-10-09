#coding:utf-8

"""
主要视图函数
"""
from datetime import datetime
from flask import render_template,session,redirect,url_for

from . import main
from .. import db

@main.route('/')
def index():
    """首页,测试"""
    return '<h1>Hello,World</h1>'