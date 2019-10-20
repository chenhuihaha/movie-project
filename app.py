"""
@Time    : 2019/10/20 下午3:33
@Author  : chenhui
@FileName: app.py
@Software: PyCharm
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1 style="color:red">hello world</h1>'


if __name__ == '__main__':
    app.run()
