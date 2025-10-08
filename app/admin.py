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
def dashboard():
    """管理后台首页"""
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
def user_management():
    """用户管理"""
    users = User.query.all()
    return render_template('admin/users.html', users=users)