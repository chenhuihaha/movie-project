"""
@Time    : 2019/10/20 下午3:50
@Author  : chenhui
@FileName: views.py
@Software: PyCharm
"""

from . import admin


@admin.route("/")
def index():
    return "<h1 style='color:red'>this is admin</h1>"
