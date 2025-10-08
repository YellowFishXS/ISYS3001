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
    
    
class AdminUserForm(FlaskForm):
    phone = StringField('手机号', validators=[
        DataRequired('请输入手机号'),
        Length(11, 11, '手机号必须是11位')
    ])
    password = PasswordField('密码', validators=[
        DataRequired('请输入密码')
    ])
    name = StringField('姓名', validators=[
        DataRequired('请输入姓名')
    ])
    student_id = StringField('学号', validators=[
        DataRequired('请输入学号')
    ])
    gender = SelectField('性别', choices=[
        ('男', '男'),
        ('女', '女')
    ], validators=[DataRequired('请选择性别')])
    college = StringField('学院', validators=[
        DataRequired('请输入学院')
    ])
    major = StringField('专业', validators=[
        DataRequired('请输入专业')
    ])
    class_name = StringField('班级', validators=[
        DataRequired('请输入班级')
    ])
    status = SelectField('状态', choices=[
        ('active', '正常'),
        ('inactive', '禁用')
    ], validators=[DataRequired('请选择状态')])
    submit = SubmitField('保存')