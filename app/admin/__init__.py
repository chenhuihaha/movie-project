# coding:utf8
from flask import Blueprint

admin = Blueprint('admin', __name__)  # 创建蓝图实例, 'admin'为蓝图名字, __name__表示蓝图所在模块


import app.admin.views  # 将admin蓝图对应的视图导入到蓝图模块中
