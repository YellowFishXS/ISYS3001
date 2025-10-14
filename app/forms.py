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
    
    
class AdminDormForm(FlaskForm):
    building_id = SelectField('楼栋', coerce=int, validators=[
        DataRequired('请选择楼栋')
    ])
    room_number = StringField('房间号', validators=[
        DataRequired('请输入房间号')
    ])
    floor = IntegerField('楼层', validators=[
        DataRequired('请输入楼层'),
        NumberRange(1, 20, '楼层必须在1-20之间')
    ])
    total_beds = IntegerField('总床位数', validators=[
        DataRequired('请输入总床位数'),
        NumberRange(1, 8, '床位数必须在1-8之间')
    ])
    room_type = SelectField('房间类型', choices=[
        ('4人间', '4人间'),
        ('6人间', '6人间'),
        ('8人间', '8人间')
    ], validators=[DataRequired('请选择房间类型')])
    price = DecimalField('价格/年', places=2, validators=[
        DataRequired('请输入价格'),
        NumberRange(0, 10000, '价格必须在0-10000之间')
    ])
    status = SelectField('状态', choices=[
        ('available', '可预订'),
        ('full', '已满'),
        ('maintenance', '维修中')
    ], validators=[DataRequired('请选择状态')])
    description = TextAreaField('描述')
    submit = SubmitField('保存')