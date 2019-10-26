# coding:utf8
"""
表单验证admin登录
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from app.models import Admin


class LoginForm(FlaskForm):
    """管理员登录表单"""
    account = StringField(
        label="账号",  # 可以通过{{form.account.label}} 在模板中添加
        validators=[  # 验证器
            DataRequired("请输入账号:")
        ],
        description="账号",  # 描述,用于帮助
        render_kw={  # 在input标签内部,widget
            "class": "form-control",
            "placeholder": "请输入账号!",
            "required": "require"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码:")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码!",
            "required": "require"
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在!")


class TagForm(FlaskForm):
    name = StringField(
        label="名称",  # 可以通过{{form.account.label}} 在模板中添加
        validators=[  # 验证器
            DataRequired("请输入标签:")
        ],
        description="标签",  # 描述,用于帮助
        render_kw={  # 在input标签内部,widget
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入标签名称！"
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )
