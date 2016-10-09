#coding:utf-8
from flask import Blueprint

main = Blueprint('main',__name__) # 蓝本实例,第一个参数是蓝本名字,第二个默认为__name__

from . import errors,views # 导入包内的模块,只有从这里导入才能使用