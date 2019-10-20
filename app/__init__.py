"""
@Time    : 2019/10/20 下午3:47
@Author  : chenhui
@FileName: __init__.py.py
@Software: PyCharm
"""

from flask import Flask

app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
