from flask import Blueprint, render_template, jsonify, request,current_app
from app.models import DormRoom, DormBuilding, User
from app import db

main_bp = Blueprint('main', __name__)

#index room list
@main_bp.route('/')
def index():
    
    # select all楼栋用于筛选
    buildings = DormBuilding.query.all()
    
    query = DormRoom.query.filter_by(status='available')
    
    search = request.args.get('search', '').strip()
    if search:
        query = query.join(DormBuilding).filter(
            or_(
                DormBuilding.building_name.contains(search),
                DormRoom.room_number.contains(search)
            )
        )
    
    available_rooms = query.all()
    return render_template('index.html', rooms=available_rooms,  buildings=buildings)

@main_bp.route('/profile')
@login_required
def profile():
    """用户个人信息页"""
    return render_template('profile.html', user=current_user)
    
# dormitory list
@main_bp.route('/api/rooms')
def api_rooms():
    rooms = DormRoom.query.filter_by(status='available').all()
    result = []
    for room in rooms:
        result.append({
            'id': room.id,
            'building_name': room.building.building_name,
            'room_number': room.room_number,
            'floor': room.floor,
            'total_beds': room.total_beds,
            'available_beds': room.available_beds,
            'room_type': room.room_type,
            'price': float(room.price),
            'description': room.description
        })
    return jsonify(result)

# room detail
@main_bp.route('/room/<int:room_id>')
def room_detail(room_id):
    room = DormRoom.query.get_or_404(room_id)
    return render_template('room_detail.html', room=room)
