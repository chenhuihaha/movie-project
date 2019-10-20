"""
@Time    : 2019/10/20 下午3:49
@Author  : chenhui
@FileName: __init__.py.py
@Software: PyCharm
"""

from flask import Blueprint

# 定义蓝图
admin = Blueprint("admin", __name__)
import app.admin.views
