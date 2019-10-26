from app.models import Admin, Tag
from . import admin
from flask import render_template, redirect, url_for, flash, session, request
from app.admin import forms
from functools import wraps  # 同一个装饰器同时使用时,需要用到该函数,回复被装饰函数的函数名
from app import db


def admin_login_req(f):
    @wraps(f)  # 重要,主要作用是被装饰的函数名重新命名为自己的函数名,而不是装饰器的名字,当有多个视图函数时
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            # 现在要实现一个需求就是，登录成功跳转到原来的页面，就要是next这个关键字
            # url：/login/?next=/ 跳转到首页,
            return redirect(url_for("admin.login", next=request.url))

        # return redirect(url_for("admin.login"))
        return f(*args, **kwargs)

    return decorated_function


@admin.route("/")
@admin_login_req
def index():
    return render_template('admin/index.html')


@admin.route("/login/", methods=["GET", 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        data = form.data  # 获取表单提交数据
        admin = Admin.query.filter_by(name=data['account']).first()
        if not admin.check_pwd(data['pwd']):
            flash("密码错误")
            return redirect(url_for('admin.login'))
        session['admin'] = data['account']
        #  request.args.get()获取get请求参数,request.form.get()获取POST请求参数
        return redirect(request.args.get("next") or url_for("admin.index"))

    return render_template('admin/login.html', form=form)


@admin.route("/logout/")
@admin_login_req
def logout():
    session.pop('admin', None)
    return redirect(url_for('admin.login'))


@admin.route("/pwd/")
@admin_login_req
def pwd():
    return render_template('admin/pwd.html')


# 添加标签
@admin.route("/tag/add/", methods=["POST", 'GET'])
@admin_login_req
def tag_add():
    form = forms.TagForm()
    if form.validate_on_submit():  # post提交且有值
        data = form.data  # 获取提交的数据
        tag = Tag.query.filter_by(name=data['name']).count()
        if tag == 1:
            flash('标签已经存在!', "err")
            return redirect(url_for('admin.tag_add'))
        tag = Tag(
            name=data["name"]
        )
        db.session.add(tag)
        db.session.commit()
        flash("添加成功", "ok")
        redirect(url_for('admin.tag_add'))
    return render_template('admin/tag_add.html', form=form)


# 标签列表
@admin.route("/tag/list/<int:page>", methods=["GET"])
@admin_login_req
def tag_list(page=None):
    if page is None:
        page = 1
    page_data = Tag.query.order_by(
        Tag.add_time.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/tag_list.html', page_data=page_data)


# del标签
@admin.route("/tag/del/<int:id>", methods=["GET"])
@admin_login_req
def tag_del(id=None):
    tag = Tag.query.filter_by(id=id).first_or_404()
    db.session.delete(tag)
    db.session.commit()
    flash("删除成功", "ok")
    return redirect(url_for('admin.tag_list', page=1))


# 编辑标签
@admin.route("/tag/edit/<int:id>/", methods=["POST", 'GET'])
@admin_login_req
def tag_edit(id=None):
    form = forms.TagForm()
    tag = Tag.query.get_or_404(id)
    # tag = Tag.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():  # post提交且有值
        data = form.data  # 获取提交的数据
        tag_count = Tag.query.filter_by(name=data['name']).count()
        if tag_count == 1:
            flash('标签已经存在!', "err")
            return redirect(url_for('admin.tag_edit', id=id))
        tag.name = data['name']
        db.session.add(tag)
        db.session.commit()
        flash("修改成功", "ok")
        return redirect(url_for('admin.tag_edit', id=id))

    return render_template('admin/tag_edit.html', form=form, tag=tag)


@admin.route("/movie/add/")
@admin_login_req
def movie_add():
    return render_template('admin/movie_add.html')


@admin.route("/movie/list/")
@admin_login_req
def movie_list():
    return render_template('admin/movie_list.html')


@admin.route("/preview/add/")
@admin_login_req
def preview_add():
    return render_template('admin/preview_add.html')


@admin.route("/preview/list/")
@admin_login_req
def preview_list():
    return render_template('admin/preview_list.html')


@admin.route("/user/list/")
@admin_login_req
def user_list():
    return render_template('admin/user_list.html')


@admin.route("/user/view/")
@admin_login_req
def user_view():
    return render_template('admin/user_view.html')


@admin.route("/comment/list/")
@admin_login_req
def comment_list():
    return render_template('admin/comment_list.html')


@admin.route("/moviecol/list/")
@admin_login_req
def moviecol_list():
    return render_template('admin/moviecol_list.html')


@admin.route("/oplog/list/")
@admin_login_req
def oplog_list():
    return render_template('admin/oplog_list.html')


@admin.route("/adminloginlog/list/")
@admin_login_req
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')


@admin.route("/userloginlog/list/")
@admin_login_req
def userloginlog_list():
    return render_template('admin/userloginlog_list.html')


@admin.route("/role/add/")
@admin_login_req
def role_add():
    return render_template('admin/role_add.html')


@admin.route("/role/list/")
@admin_login_req
def role_list():
    return render_template('admin/role_list.html')


@admin.route("/auth/add/")
@admin_login_req
def auth_add():
    return render_template('admin/auth_add.html')


@admin.route("/auth/list/")
@admin_login_req
def auth_list():
    return render_template('admin/auth_list.html')


@admin.route("/admin/add/")
@admin_login_req
def admin_add():
    return render_template('admin/admin_add.html')


@admin.route("/admin/list/")
@admin_login_req
def admin_list():
    return render_template('admin/admin_list.html')
