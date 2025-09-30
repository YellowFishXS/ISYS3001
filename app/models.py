from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    student_id = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.Enum('男', '女'), nullable=False)
    college = db.Column(db.String(100))
    major = db.Column(db.String(100))
    class_name = db.Column(db.String(50))
    status = db.Column(db.Enum('active', 'inactive'), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class DormBuilding(db.Model):
    __tablename__ = 'dorm_buildings'

    id = db.Column(db.BigInteger, primary_key=True)
    building_name = db.Column(db.String(50), nullable=False)
    # building_number = db.Column(db.String(20), unique=True, nullable=False)
    gender = db.Column(db.Enum('男', '女'), nullable=False)
    total_floors = db.Column(db.Integer, nullable=False)
    # description = db.Column(db.Text)
    status = db.Column(db.Enum('active', 'inactive'), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 关系
    rooms = db.relationship('DormRoom', backref='building', lazy=True)


class DormRoom(db.Model):
    __tablename__ = 'dorm_rooms'

    id = db.Column(db.BigInteger, primary_key=True)
    building_id = db.Column(db.BigInteger, db.ForeignKey('dorm_buildings.id'), nullable=False)
    room_number = db.Column(db.String(20), nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    total_beds = db.Column(db.Integer, nullable=False)
    available_beds = db.Column(db.Integer, nullable=False)
    room_type = db.Column(db.Enum('4人间', '6人间', '8人间'), nullable=False)
    price = db.Column(db.Numeric(8, 2), nullable=False)
    status = db.Column(db.Enum('available', 'full', 'maintenance'), default='available')
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    images = db.relationship('DormImage', backref='room', lazy=True)

class DormImage(db.Model):
    __tablename__ = 'dorm_images'

    id = db.Column(db.BigInteger, primary_key=True)
    room_id = db.Column(db.BigInteger, db.ForeignKey('dorm_rooms.id'), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    image_type = db.Column(db.Enum('room', 'environment', 'facility'), default='room')
    sort_order = db.Column(db.Integer, default=0)
    is_primary = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)