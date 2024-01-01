from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.secret_key = "this is the secret key for the app"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    from .api import api
    app.register_blueprint(api, url_prefix="/api")
    db.init_app(app)
    create_database(app)
    return app


def create_database(app):
    if not path.exists('./database.db'):
        with app.app_context():
            db.create_all()
        print("Database created Successfully")
