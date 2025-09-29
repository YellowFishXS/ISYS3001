from flask import Blueprint, render_template, jsonify, request,current_app
from app.models import DormRoom, DormBuilding, User
from app import db

main_bp = Blueprint('main', __name__)

#index room list
@main_bp.route('/')
def index():
    available_rooms = DormRoom.query.filter_by(status='available').all()
    return render_template('index.html', rooms=available_rooms)

@main_bp.route('/profile')
@login_required
def profile():
    """用户个人信息页"""
    return render_template('profile.html', user=current_user)