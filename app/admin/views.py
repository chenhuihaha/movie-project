"""
@Time    : 2019/10/20 下午3:50
@Author  : chenhui
@FileName: views.py
@Software: PyCharm
"""

from . import admin
from flask import render_template, redirect, url_for


@admin.route("/")
def index():
    return "<h1 style='color:red'>this is admin</h1>"


@admin.route("/login/")
def login():
    return render_template('admin/login.html')


@admin.route("/logout/")
def logout():
    return redirect(url_for('admin.login'))

print('text')
