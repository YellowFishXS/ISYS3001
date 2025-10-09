from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import User, DormBuilding, DormRoom, Bed
from app.forms import AdminUserForm, AdminDormForm
import json

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


def admin_required(f):
    @login_required
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('请先登录', 'danger')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/')
@admin_required
#index
def dashboard():
    user_count = User.query.count()
    building_count = DormBuilding.query.count()
    room_count = DormRoom.query.count()
    available_rooms = DormRoom.query.filter_by(status='available').count()
    
    return render_template('admin/dashboard.html',
                         user_count=user_count,
                         building_count=building_count,
                         room_count=room_count,
                         available_rooms=available_rooms)

@admin_bp.route('/users')
@admin_required
#list
def user_management():
    users = User.query.all()
    return render_template('admin/users.html', users=users)
    
@admin_bp.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
@admin_required
#edit
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = AdminUserForm(obj=user)
    
    if form.validate_on_submit():
        existing_user = User.query.filter_by(phone=form.phone.data).first()
        if existing_user and existing_user.id != user.id:
            flash('该手机号已被其他用户使用', 'danger')
            return redirect(url_for('admin.edit_user', user_id=user_id))
        
        form.populate_obj(user)
        db.session.commit()
        flash('用户信息更新成功', 'success')
        return redirect(url_for('admin.user_management'))
    
    return render_template('admin/user_form.html', form=form, title='编辑用户', user=user)