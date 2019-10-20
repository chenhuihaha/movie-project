"""
@Time    : 2019/10/20 下午3:50
@Author  : chenhui
@FileName: views.py
@Software: PyCharm
"""

from . import home


@home.route("/")
def index():
    return "<h1 style='color:green'>this is home</h1>"
