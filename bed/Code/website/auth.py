from flask import Blueprint, request, Response, jsonify, current_app
from .models import User
from website import db
from flask_login import login_user, current_user, logout_user
import jwt


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json() or request.form
    username = data["username"]
    password = data["password"]
    if current_user.is_authenticated:
        return jsonify({"success": "false", "message": "user already logged in"})
    user = User.query.filter_by(username=username).all()
    if (user):
        if password == user[0].password:
            login_user(user[0])
            userjwt = jwt.encode(
                payload={"username": username, "role": user[0].role}, key=current_app.config["SECRET_KEY"])
            resp = Response(
                jsonify({"success": "true", "message": 'Login Successful'}))
            resp.headers["set-cookie"] = f"flask_jwt={userjwt}; HttpOnly; Path=/; Max-age=3600"
            return resp
        else:
            return jsonify({"success": "false", "message": 'Password is incorrect'}), 401
    else:
        return jsonify({"success": "false", "message": 'Username is not registered'}), 401


@auth.route("/user", methods=["GET"])
def user():
    if current_user.is_authenticated:
        userId = current_user.user_id
        user = User.query.filter_by(user_id=userId).all()[0]
        return jsonify({"username": user.username, "role": user.role})
    else:
        return jsonify("user not logged in ")


@auth.route("/logout", methods=["GET"])
def logout():
    logout_user()
    Response().set_cookie(key="flask_jwt", value="", expires=0), 200
    return "logged Out"

# @auth.route("/signup", methods=["POST"])
# def signup():
#     data = request.get_json() or request.form
#     username = data["username"]
#     password = data["password"]
#     user = User.query.filter_by(username=username).first()
#     if user is None:
#         user = User(
#             username=username,
#             password=generate_password_hash(password)
#         )
#         db.session.add(user)
#         db.session.commit()
#         access_token = create_access_token(identity=user.user_id)
#         refresh_token = create_refresh_token(identity=user.user_id)

#         response = jsonify()
#         set_access_cookies(response, access_token)
#         set_refresh_cookies(response, refresh_token)

#         return response, 201
#     else:
#         return jsonify(message="Unable to create user."), 400
