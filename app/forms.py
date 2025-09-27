from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    phone = StringField('手机号', validators=[
        DataRequired('请输入手机号'),
        Length(11, 11, '手机号必须是11位')
    ])
    password = PasswordField('密码', validators=[
        DataRequired('请输入密码')
    ])
    submit = SubmitField('登录')

class RegistrationForm(FlaskForm):
    phone = StringField('手机号', validators=[
        DataRequired('请输入手机号'),
        Length(11, 11, '手机号必须是11位')
    ])
    password = PasswordField('密码', validators=[
        DataRequired('请输入密码')
    ])
    password2 = PasswordField('确认密码', validators=[
        DataRequired('请确认密码'),
        EqualTo('password', '两次密码不一致')
    ])
    name = StringField('姓名', validators=[
        DataRequired('请输入姓名')
    ])
    student_id = StringField('学号', validators=[
        DataRequired('请输入学号')
    ])
    submit = SubmitField('注册')