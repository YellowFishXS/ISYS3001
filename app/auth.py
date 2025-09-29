from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import db, login
from app.models import User
from app.forms import LoginForm, RegistrationForm
from datetime import datetime

auth_bp = Blueprint('auth', __name__)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(phone=form.phone.data).first()
        

        if user is None or user.password != form.password.data:
            flash('手机号或密码错误', 'danger')
            return redirect(url_for('auth.login'))
        
        if user.status == 'inactive':
            flash('账号已被禁用，请联系管理员', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user)
        user.last_login_time = datetime.utcnow()
        db.session.commit()
        
        flash(f'欢迎回来，{user.name}！', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('login.html', form=form)
    
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(phone=form.phone.data).first():
            flash('该手机号已被注册', 'danger')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(student_id=form.student_id.data).first():
            flash('该学号已被注册', 'danger')
            return redirect(url_for('auth.register'))
        
        # 创建新用户 
        user = User(
            phone=form.phone.data,
            password=form.password.data,  
            name=form.name.data,
            student_id=form.student_id.data,
            gender=form.gender.data,  
            college=form.college.data,  
            major=form.major.data,  
            class_name=form.class_name.data 
        )
        
        db.session.add(user)
        db.session.commit()
        
        flash('注册成功！请登录', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html', form=form)



@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已成功退出登录', 'info')
    return redirect(url_for('main.index'))