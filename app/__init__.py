# coding:utf8
from flask import Flask, render_template
import pymysql

from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

app = Flask(__name__)  # 在app中创建主路由

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/movie?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)  # 要在配置之后才能够加载
app.config["SECRET_KEY"] = 'f3f51a457ba04730814f09f264b09773'


app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)  # 将home蓝图注册到主路由
app.register_blueprint(admin_blueprint, url_prefix="/admin")  # 将admin蓝图注册到主路由


@app.errorhandler(404)
def page_not_find(error):
    return render_template('home/404.html'), 404
