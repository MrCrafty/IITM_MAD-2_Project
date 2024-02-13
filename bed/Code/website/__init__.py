from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SECRET_KEY"] = "IITM_MAD_Project_2"
    from .api import api
    app.register_blueprint(api, url_prefix="/api")
    from .auth import auth
    app.register_blueprint(auth, url_prefix="/auth")
    db.init_app(app)
    create_database(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user):
        return User.query.get(int(user))

    with app.app_context():
        from .models import User
        admin = User.query.filter_by(username="admin").first()
        if admin is None:
            db.session.add(
                User(username="admin", password="admin", role="admin"))
            db.session.commit()
            print("Admin User created")
    return app


def create_database(app):
    if not path.exists('./database.db'):
        with app.app_context():
            db.create_all()
        print("Database created Successfully")
