from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = '请先登录'


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/domitory'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app.routes import main_bp
    from app.auth import auth_bp
    from app.admin import admin_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
       app.register_blueprint(admin_bp)

    return app