from flask import Blueprint, Response, current_app, request
from flask_restful import Resource
from website.util import Message
from .models import User
from website import db
from flask_login import login_user, current_user, logout_user
import jwt


auth = Blueprint("auth", __name__)


class Login(Resource):
    def post(self):
        data = request.get_json()["body"] or request.form()["body"]
        username = data["username"]
        password = data["password"]
        if current_user.is_authenticated:
            return Message(False, 'User already logged in')
        user = User.query.filter_by(username=username).all()
        if (user):
            if password == user[0].password:
                login_user(user[0])
                userjwt = jwt.encode(
                    payload={"username": username, "role": user[0].role}, key=current_app.config["SECRET_KEY"])
                resp = Response("Ok")
                resp.headers["set-cookie"] = f"flask_jwt={userjwt}; HttpOnly; Path=/; Max-age=3600"
                resp.status_code = 200
                resp.content_type = "application/json"
                return Message(True, 'User Logged In')
            else:
                return Message(False, "Invalid password")
        else:
            return Message(False, 'User does Not exist')


class CurrentUser(Resource):
    def get(self):
        if current_user.is_authenticated:
            userId = current_user.user_id
            user = User.query.filter_by(user_id=userId).all()[0]
            return Message(True, {"username": user.username, "role": user.role})
        else:
            return Message(False, 'User not Logged in')


class Logout(Resource):
    def get(self):
        logout_user()
        Response().set_cookie(key="flask_jwt", value="", expires=0), 200
        Response().delete_cookie("flask_jwt")
        return Message(True, "User logged out")


def initialize_auth(api):
    api.add_resource(Login, '/login')
    api.add_resource(CurrentUser, '/user')
    api.add_resource(Logout, '/logout')
